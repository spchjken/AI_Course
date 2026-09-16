"""Lexical search over indexed sources without storing per-file keywords."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable

try:
    from index_core import IndexErrorBase, classify_path, ensure_within_root, load_config, normalize_relpath, normalized_text, validate_index
except ImportError:  # pragma: no cover
    from .index_core import IndexErrorBase, classify_path, ensure_within_root, load_config, normalize_relpath, normalized_text, validate_index


TOKEN_RE = re.compile(r"[\w\-]+", re.UNICODE)


def _load_index(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        index = json.load(handle)
    errors = validate_index(index)
    if errors:
        raise ValueError("invalid index: " + "; ".join(errors[:5]))
    return index


def _fold(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(char for char in decomposed if not unicodedata.combining(char)).casefold()


def _tokens(value: str) -> list[str]:
    return [_fold(token) for token in TOKEN_RE.findall(value)]


def _snippet(text: str, query: str, width: int = 180) -> str:
    folded = _fold(text)
    position = folded.find(_fold(query))
    if position < 0:
        query_tokens = _tokens(query)
        for token in query_tokens:
            position = folded.find(token)
            if position >= 0:
                break
    if position < 0:
        return " ".join(text.split())[:width]
    start = max(0, position - width // 3)
    return " ".join(text[start : start + width].split())


def _rg_paths(root: Path, query: str, paths: Iterable[str]) -> set[str] | None:
    rg = shutil.which("rg")
    if not rg:
        return None
    path_list = sorted(paths)
    if not path_list:
        return set()
    # Python scoring is accent-folded and token-aware. Keep rg as a safe
    # accelerator only for queries whose spelling it can represent; otherwise
    # the stdlib path is the correctness fallback.
    if _fold(query) != query.casefold():
        return None
    matches: set[str] = set()
    # ripgrep releases differ on whether ``--files-from`` exists. Explicit
    # paths work across versions; batch them to stay below Windows argv limits.
    terms = _tokens(query) or [query]
    for term in terms:
        for offset in range(0, len(path_list), 80):
            command = [rg, "--json", "--no-heading", "--color", "never", "--fixed-strings", "--ignore-case", term, "--", *path_list[offset : offset + 80]]
            try:
                result = subprocess.run(
                    command,
                    cwd=root,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    check=False,
                )
            except OSError:
                return None
            if result.returncode not in {0, 1}:
                return None
            for line in result.stdout.splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") != "match":
                    continue
                path = event.get("data", {}).get("path", {}).get("text")
                if path:
                    try:
                        matches.add(normalize_relpath(path))
                    except Exception:
                        continue
    return matches


def search(
    *,
    root: Path,
    index_path: Path,
    config_path: Path,
    query: str,
    authority: str | None = None,
    source_type: str | None = None,
    source_status: str | None = None,
    include_operational: bool = False,
    top: int = 20,
    backend: str = "auto",
) -> dict[str, Any]:
    if not query.strip():
        raise ValueError("query must not be empty")
    index_path = ensure_within_root(root, index_path)
    index = _load_index(index_path)
    config = load_config(ensure_within_root(root, config_path))
    entries = []
    for entry in index["entries"]:
        expected = classify_path(str(entry["path"]), config)
        if any(entry.get(field) != expected.get(field) for field in ("type", "authority", "source_status", "default_search")):
            raise ValueError(f"index classification is stale or tampered: {entry['path']}")
        if not include_operational and not entry.get("default_search", True):
            continue
        if authority and entry.get("authority") != authority:
            continue
        if source_type and entry.get("type") != source_type:
            continue
        if source_status and entry.get("source_status") != source_status:
            continue
        entries.append(entry)
    candidate_paths = [str(entry["path"]) for entry in entries]
    used_backend = "python"
    rg_matches: set[str] | None = None
    if backend in {"auto", "rg"}:
        rg_matches = _rg_paths(root, query, candidate_paths)
        if rg_matches is not None:
            used_backend = "rg"
    results: list[dict[str, Any]] = []
    query_folded = _fold(query)
    query_tokens = set(_tokens(query))
    for entry in entries:
        path = str(entry["path"])
        if rg_matches is not None and path not in rg_matches:
            continue
        source_path = root / Path(*path.split("/"))
        try:
            text = normalized_text(source_path)
        except OSError:
            continue
        except Exception:
            continue
        folded = _fold(text)
        title_folded = _fold(str(entry.get("title", "")))
        title_tokens = set(_tokens(str(entry.get("title", ""))))
        occurrences = folded.count(query_folded)
        matching_tokens = sum(folded.count(token) for token in query_tokens)
        score = occurrences * 30 + matching_tokens * 3
        if query_folded in title_folded:
            score += 100
        score += len(query_tokens & title_tokens) * 20
        if score <= 0:
            continue
        try:
            from index_core import content_hash_for_path
        except ImportError:  # pragma: no cover
            from .index_core import content_hash_for_path
        try:
            current_hash = content_hash_for_path(source_path)
        except Exception:
            current_hash = None
        results.append(
            {
                "path": path,
                "title": entry.get("title", ""),
                "type": entry.get("type", ""),
                "authority": entry.get("authority", ""),
                "source_status": entry.get("source_status", "unknown"),
                "content_hash": entry.get("content_hash", ""),
                "source_current": current_hash == entry.get("content_hash"),
                "score": score,
                "snippet": _snippet(text, query),
            }
        )
    results.sort(key=lambda result: (-int(result["score"]), str(result["path"])))
    return {
        "query": query,
        "backend": used_backend,
        "index_tree_fingerprint": index["tree_fingerprint"],
        "result_count": len(results[:top]),
        "results": results[:top],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--index", type=Path, default=Path(".agents/generated/context-index.json"))
    parser.add_argument("--config", type=Path, default=Path(".agents/indexing/index-config.json"))
    parser.add_argument("--authority")
    parser.add_argument("--type", dest="source_type")
    parser.add_argument("--source-status")
    parser.add_argument("--include-operational", action="store_true")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--backend", choices=("auto", "python", "rg"), default="auto")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    root = args.root.resolve()
    index_path = args.index if args.index.is_absolute() else root / args.index
    config_path = args.config if args.config.is_absolute() else root / args.config
    try:
        result = search(
            root=root,
            index_path=index_path,
            config_path=config_path,
            query=args.query,
            authority=args.authority,
            source_type=args.source_type,
            source_status=args.source_status,
            include_operational=args.include_operational,
            top=max(args.top, 1),
            backend=args.backend,
        )
    except (OSError, ValueError, IndexErrorBase) as exc:
        print(f"search_index: error: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
