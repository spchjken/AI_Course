"""Build and incrementally synchronize the repository derived context index."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

try:  # Support both ``python .agents/indexing/sync_index.py`` and imports.
    from index_core import (
        IndexErrorBase,
        build_index,
        content_hash_for_path,
        iter_candidate_files,
        load_config,
        make_entry,
        ensure_within_root,
        validate_index,
        write_json_atomic,
    )
except ImportError:  # pragma: no cover - package-style import fallback
    from .index_core import (
        IndexErrorBase,
        build_index,
        content_hash_for_path,
        iter_candidate_files,
        load_config,
        make_entry,
        ensure_within_root,
        validate_index,
        write_json_atomic,
    )


TOOL_VERSION = "0.1"


def _json_load(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _config_revision(config: dict[str, Any]) -> str:
    import hashlib

    payload = json.dumps(config, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _git_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
        )
        return result.stdout.strip() or "working-tree"
    except (OSError, subprocess.CalledProcessError):
        return "working-tree"


def _load_index(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    value = _json_load(path, None)
    if not isinstance(value, dict):
        raise ValueError(f"index must be a JSON object: {path}")
    errors = validate_index(value)
    if errors:
        raise ValueError("invalid index: " + "; ".join(errors[:5]))
    return value


def _load_cache(path: Path) -> dict[str, Any]:
    value = _json_load(path, {})
    if not isinstance(value, dict):
        return {}
    if not isinstance(value.get("files", {}), dict):
        value["files"] = {}
    return value


def _write_lock(lock_path: Path) -> int:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise RuntimeError(f"index lock already exists: {lock_path}") from exc
    os.write(descriptor, f"pid={os.getpid()}\n".encode("ascii"))
    return descriptor


def _release_lock(lock_path: Path, descriptor: int | None) -> None:
    if descriptor is not None:
        os.close(descriptor)
    try:
        lock_path.unlink()
    except FileNotFoundError:
        pass


def _entry_map(index: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not index:
        return {}
    return {str(entry["path"]): dict(entry) for entry in index.get("entries", [])}


def _current_snapshot(root: Path, config: dict[str, Any], old_index: dict[str, Any] | None, cache: dict[str, Any], force_full: bool, strict_check: bool = False) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    old_entries = _entry_map(old_index)
    old_files = cache.get("files", {}) if not force_full else {}
    current_entries: list[dict[str, Any]] = []
    next_files: dict[str, Any] = {}
    stats = {"hashed_count": 0, "parsed_count": 0, "reused_count": 0, "unstable_count": 0}
    can_reuse_metadata = strict_check and cache.get("config_revision") == _config_revision(config)
    for relpath, path in iter_candidate_files(root, config):
        file_stat = path.stat()
        signature = {"size": file_stat.st_size, "mtime_ns": file_stat.st_mtime_ns}
        cached = old_files.get(relpath)
        old_entry = old_entries.get(relpath)
        if (
            cached
            and old_entry
            and cached.get("size") == file_stat.st_size
            and cached.get("mtime_ns") == file_stat.st_mtime_ns
            and cached.get("content_hash") == old_entry.get("content_hash")
            and old_entry.get("index_state") == "current"
        ):
            entry = dict(old_entry)
            current_entries.append(entry)
            next_files[relpath] = {**signature, "content_hash": entry["content_hash"]}
            stats["reused_count"] += 1
            continue
        entry = None
        for attempt in range(2):
            stats["hashed_count"] += 1
            try:
                before_hash_stat = file_stat
                content_hash = content_hash_for_path(path)
                after_hash_stat = path.stat()
                if (before_hash_stat.st_mtime_ns, before_hash_stat.st_size) != (after_hash_stat.st_mtime_ns, after_hash_stat.st_size):
                    raise IndexErrorBase(f"content changed during hashing {relpath}")
                if can_reuse_metadata and old_entry and old_entry.get("content_hash") == content_hash:
                    entry = dict(old_entry)
                else:
                    stats["parsed_count"] += 1
                    entry = make_entry(root, relpath, config, content_hash=content_hash)
                break
            except IndexErrorBase:
                if attempt == 1:
                    stats["unstable_count"] += 1
                    raise
        if entry is None:  # defensive; both attempts either set or raise
            raise RuntimeError(f"could not index {relpath}")
        current_entries.append(entry)
        next_files[relpath] = {**signature, "content_hash": entry["content_hash"]}
    return current_entries, {**stats, "files": next_files}, {"old_entries": old_entries}


def _events(old_index: dict[str, Any] | None, entries: list[dict[str, Any]]) -> list[dict[str, str]]:
    old = _entry_map(old_index)
    current = {entry["path"]: entry for entry in entries}
    old_paths = set(old)
    current_paths = set(current)
    deleted = old_paths - current_paths
    created = current_paths - old_paths
    modified = {
        path
        for path in old_paths & current_paths
        if old[path].get("content_hash") != current[path].get("content_hash")
    }
    events: list[dict[str, str]] = []
    old_by_hash: dict[str, list[str]] = defaultdict(list)
    new_by_hash: dict[str, list[str]] = defaultdict(list)
    old_all_by_hash: dict[str, int] = defaultdict(int)
    current_all_by_hash: dict[str, int] = defaultdict(int)
    for entry in old.values():
        old_all_by_hash[str(entry.get("content_hash"))] += 1
    for entry in current.values():
        current_all_by_hash[str(entry.get("content_hash"))] += 1
    for path in deleted:
        old_by_hash[str(old[path].get("content_hash"))].append(path)
    for path in created:
        new_by_hash[str(current[path].get("content_hash"))].append(path)
    moved_old: set[str] = set()
    moved_new: set[str] = set()
    for digest in sorted(old_by_hash):
        old_paths_for_hash = old_by_hash[digest]
        new_paths_for_hash = new_by_hash.get(digest, [])
        # Do not claim a move when another path carries the same content. In
        # that case the event is intentionally left as delete/create/copy.
        if (
            len(old_paths_for_hash) == len(new_paths_for_hash) == 1
            and old_all_by_hash[digest] == 1
            and current_all_by_hash[digest] == 1
        ):
            old_path = old_paths_for_hash[0]
            new_path = new_paths_for_hash[0]
            moved_old.add(old_path)
            moved_new.add(new_path)
            events.append({"kind": "moved", "from": old_path, "path": new_path, "content_hash": digest})
    for path in sorted(modified):
        events.append({"kind": "modified", "path": path, "content_hash": str(current[path]["content_hash"])})
    for path in sorted(created - moved_new):
        same_hash_existing = any(current[path]["content_hash"] == current[other]["content_hash"] for other in current_paths if other != path)
        events.append({"kind": "copied" if same_hash_existing else "created", "path": path, "content_hash": str(current[path]["content_hash"])})
    for path in sorted(deleted - moved_old):
        events.append({"kind": "deleted", "path": path, "content_hash": str(old[path]["content_hash"])})
    return events


def sync(*, root: Path, config_path: Path, index_path: Path, cache_path: Path, lock_path: Path, mode: str, report_path: Path | None, baseline_commit: str | None) -> int:
    started = time.perf_counter()
    root = root.resolve()
    config_path = ensure_within_root(root, config_path)
    index_path = ensure_within_root(root, index_path)
    cache_path = ensure_within_root(root, cache_path)
    lock_path = ensure_within_root(root, lock_path)
    if report_path is not None:
        report_path = ensure_within_root(root, report_path)
    config = load_config(config_path)
    try:
        existing = _load_index(index_path)
    except ValueError:
        # A full rebuild is the migration path for a schema/fingerprint change;
        # incremental and check modes must still fail closed on a bad index.
        if mode == "full":
            existing = None
        else:
            raise
    cache = _load_cache(cache_path)
    # ``--check`` is the integrity path: hash every eligible file so an edit
    # made by another process is detected even when its size/mtime happen to
    # remain unchanged. ``--update`` keeps the stat cache fast and ``--full``
    # rebuilds and writes every entry.
    force_full = mode in {"full", "check"}
    if cache.get("config_revision") != _config_revision(config):
        force_full = True
    if existing is None:
        force_full = True
    lock_descriptor: int | None = None
    if mode in {"update", "full"}:
        lock_descriptor = _write_lock(lock_path)
    try:
        entries, next_cache, _ = _current_snapshot(root, config, existing, cache, force_full, strict_check=mode == "check")
        commit = baseline_commit or (existing or {}).get("baseline_commit") or _git_commit(root)
        candidate = build_index(entries, baseline_commit=commit)
        errors = validate_index(candidate)
        if errors:
            raise ValueError("generated index is invalid: " + "; ".join(errors))
        events = _events(existing, entries)
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        summary = {
            "tool_version": TOOL_VERSION,
            "mode": mode,
            "status": "current" if existing and candidate == existing else "stale" if mode == "check" else "updated",
            "entry_count": len(entries),
            "events": events,
            "duration_ms": elapsed_ms,
            "hashed_count": next_cache.get("hashed_count", 0),
            "parsed_count": next_cache.get("parsed_count", 0),
            "reused_count": next_cache.get("reused_count", 0),
            "unstable_count": next_cache.get("unstable_count", 0),
            "config_revision": _config_revision(config),
            "tree_fingerprint": candidate["tree_fingerprint"],
        }
        if report_path:
            write_json_atomic(report_path, summary)
        if mode == "check":
            return 0 if summary["status"] == "current" else 2
        write_json_atomic(index_path, candidate)
        next_cache["schema_version"] = "1.0"
        next_cache["config_revision"] = _config_revision(config)
        next_cache.pop("hashed_count", None)
        next_cache.pop("parsed_count", None)
        next_cache.pop("reused_count", None)
        next_cache.pop("unstable_count", None)
        write_json_atomic(cache_path, next_cache)
        return 0
    finally:
        _release_lock(lock_path, lock_descriptor)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_const", const="check", dest="mode", help="scan without writing; exit 2 when stale")
    mode.add_argument("--update", action="store_const", const="update", dest="mode", help="incrementally update the index")
    mode.add_argument("--full", action="store_const", const="full", dest="mode", help="rebuild every eligible source")
    parser.set_defaults(mode="update")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--config", type=Path, default=Path(".agents/indexing/index-config.json"))
    parser.add_argument("--index", type=Path, default=Path(".agents/generated/context-index.json"))
    parser.add_argument("--cache", type=Path, default=Path(".context-index-cache.json"))
    parser.add_argument("--lock", type=Path, default=Path(".context-index-lock"))
    parser.add_argument("--report", type=Path)
    parser.add_argument("--baseline-commit")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    root = args.root.resolve()
    paths = [args.config, args.index, args.cache, args.lock]
    resolved: list[Path] = []
    for path in paths:
        resolved.append(path if path.is_absolute() else root / path)
    config_path, index_path, cache_path, lock_path = resolved
    try:
        config_path = ensure_within_root(root, config_path)
        index_path = ensure_within_root(root, index_path)
        cache_path = ensure_within_root(root, cache_path)
        lock_path = ensure_within_root(root, lock_path)
    except IndexErrorBase as exc:
        print(f"sync_index: error: {exc}", file=sys.stderr)
        return 3
    report_path = None if args.report is None else (args.report if args.report.is_absolute() else root / args.report)
    if report_path is not None:
        try:
            report_path = ensure_within_root(root, report_path)
        except IndexErrorBase as exc:
            print(f"sync_index: error: {exc}", file=sys.stderr)
            return 3
    try:
        code = sync(
            root=root,
            config_path=config_path,
            index_path=index_path,
            cache_path=cache_path,
            lock_path=lock_path,
            mode=args.mode,
            report_path=report_path,
            baseline_commit=args.baseline_commit,
        )
    except (OSError, ValueError, RuntimeError, IndexErrorBase) as exc:
        print(f"sync_index: error: {exc}", file=sys.stderr)
        return 3
    if report_path:
        print(json.dumps(_json_load(report_path, {}), ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
