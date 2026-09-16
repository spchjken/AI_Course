"""Validate a derived index, its source hashes, authority rules and links."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from index_core import classify_path, content_hash_for_path, glob_matches, load_config, validate_index
except ImportError:  # pragma: no cover
    from .index_core import classify_path, content_hash_for_path, glob_matches, load_config, validate_index


def validate(*, root: Path, index_path: Path, config_path: Path) -> dict[str, Any]:
    with index_path.open("r", encoding="utf-8") as handle:
        index = json.load(handle)
    errors = validate_index(index)
    config = load_config(config_path)
    missing_sources: list[str] = []
    stale_sources: list[str] = []
    authority_mismatches: list[str] = []
    missing_links: list[dict[str, str]] = []
    exempt_links: list[dict[str, str]] = []
    for entry in index.get("entries", []):
        relpath = str(entry.get("path", ""))
        source = root / Path(*relpath.split("/"))
        if not source.is_file():
            missing_sources.append(relpath)
            continue
        try:
            if content_hash_for_path(source) != entry.get("content_hash"):
                stale_sources.append(relpath)
        except OSError:
            stale_sources.append(relpath)
        expected = classify_path(relpath, config)
        for field in ("type", "authority", "source_status", "default_search"):
            if entry.get(field) != expected.get(field):
                authority_mismatches.append(f"{relpath}:{field}")
                break
        for link in entry.get("links", []):
            target = root / Path(*str(link).split("/"))
            if not target.exists() and not target.with_suffix(".md").exists():
                exceptions = [
                    item
                    for item in config.get("link_exceptions", [])
                    if isinstance(item, dict) and glob_matches(str(link), str(item.get("glob", "")))
                ]
                if exceptions:
                    exempt_links.append(
                        {
                            "source": relpath,
                            "target": str(link),
                            "reason": str(exceptions[0].get("reason", "configured exception")),
                        }
                    )
                else:
                    missing_links.append({"source": relpath, "target": str(link)})
    return {
        "valid_schema": not errors,
        "schema_errors": errors,
        "entry_count": len(index.get("entries", [])),
        "missing_sources": missing_sources,
        "stale_sources": stale_sources,
        "authority_mismatches": authority_mismatches,
        "missing_links": missing_links,
        "exempt_links": exempt_links,
        "false_canonical_count": sum(
            1
            for entry in index.get("entries", [])
            if entry.get("authority") == "canonical"
            and classify_path(str(entry.get("path", "")), config).get("authority") != "canonical"
        ),
        "pass": not (errors or missing_sources or stale_sources or authority_mismatches or missing_links),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--index", type=Path, default=Path(".agents/generated/context-index.json"))
    parser.add_argument("--config", type=Path, default=Path(".agents/indexing/index-config.json"))
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    root = args.root.resolve()
    index_path = args.index if args.index.is_absolute() else root / args.index
    config_path = args.config if args.config.is_absolute() else root / args.config
    try:
        report = validate(root=root, index_path=index_path, config_path=config_path)
    except (OSError, ValueError) as exc:
        print(f"validate_index: error: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["pass"] else 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
