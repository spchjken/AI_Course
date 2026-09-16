"""Build a small, task-scoped context package from the derived index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from index_core import IndexErrorBase, content_hash_for_path, ensure_within_root, normalize_relpath, write_json_atomic
    from search_index import search
except ImportError:  # pragma: no cover
    from .index_core import IndexErrorBase, content_hash_for_path, ensure_within_root, normalize_relpath, write_json_atomic
    from .search_index import search


PACKAGE_SCHEMA_VERSION = "1.0"


def build_package(
    *,
    root: Path,
    index_path: Path,
    config_path: Path,
    query: str,
    task: str,
    role: str,
    top: int,
    output_path: Path | None = None,
    allowed_writes: list[str] | None = None,
    include_operational: bool = False,
    allow_stale: bool = False,
) -> dict[str, Any]:
    search_result = search(
        root=root,
        index_path=index_path,
        config_path=config_path,
        query=query,
        top=top,
        include_operational=include_operational,
        backend="python",
    )
    selected: list[dict[str, Any]] = []
    stale: list[str] = []
    for result in search_result["results"]:
        source = root / Path(*str(result["path"]).split("/"))
        try:
            current_hash = content_hash_for_path(source)
        except OSError:
            current_hash = None
        if current_hash != result.get("content_hash"):
            stale.append(str(result["path"]))
        selected.append(
            {
                "path": result["path"],
                "title": result["title"],
                "type": result["type"],
                "authority": result["authority"],
                "source_status": result["source_status"],
                "content_hash": result["content_hash"],
                "snippet": result["snippet"],
            }
        )
    if stale and not allow_stale:
        raise ValueError("selected source changed after indexing: " + ", ".join(stale))
    normalized_writes = sorted({normalize_relpath(item) for item in (allowed_writes or [])})
    package = {
        "schema_version": PACKAGE_SCHEMA_VERSION,
        "task": task,
        "role": role,
        "query": query,
        "index_tree_fingerprint": search_result["index_tree_fingerprint"],
        "source_verification": {"stale_paths": stale, "all_current": not stale},
        "sources": selected,
        "read_allowlist": [item["path"] for item in selected],
        "write_allowlist": normalized_writes,
        "out_of_scope": [
            "Do not treat snippets as a substitute for reading the source file.",
            "Do not edit canonical sources outside the explicitly approved work unit.",
            "Do not promote this task package or the derived index to canonical authority.",
        ],
    }
    if output_path:
        write_json_atomic(ensure_within_root(root, output_path), package)
    return package


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--role", default="worker")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--index", type=Path, default=Path(".agents/generated/context-index.json"))
    parser.add_argument("--config", type=Path, default=Path(".agents/indexing/index-config.json"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allowed-write", action="append", default=[])
    parser.add_argument("--include-operational", action="store_true")
    parser.add_argument("--allow-stale", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    root = args.root.resolve()
    index_path = args.index if args.index.is_absolute() else root / args.index
    config_path = args.config if args.config.is_absolute() else root / args.config
    output_path = None if args.output is None else (args.output if args.output.is_absolute() else root / args.output)
    try:
        package = build_package(
            root=root,
            index_path=index_path,
            config_path=config_path,
            query=args.query,
            task=args.task,
            role=args.role,
            top=max(args.top, 1),
            output_path=output_path,
            allowed_writes=args.allowed_write,
            include_operational=args.include_operational,
            allow_stale=args.allow_stale,
        )
    except (OSError, ValueError, IndexErrorBase) as exc:
        print(f"build_context_package: error: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(package, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
