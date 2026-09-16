"""Core primitives for the repository derived context index.

The index is deliberately structural.  It stores paths, classifications and
content fingerprints, but it does not try to maintain a lossy keyword list.
Lexical search reads the current source files when a query is made.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import posixpath
import re
import tempfile
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Iterator, Mapping


SCHEMA_VERSION = "1.0"
GENERATOR_VERSION = "0.1"
TEXT_SUFFIXES = {
    ".md",
    ".markdown",
    ".txt",
    ".py",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".csv",
    ".tsv",
}
LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]*\])\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)


class IndexErrorBase(Exception):
    """Base class for predictable index errors."""


class UnsafePathError(IndexErrorBase):
    """A path escaped the repository root or used an unsupported form."""


class UnreadableSourceError(IndexErrorBase):
    """A candidate source could not be read as UTF-8 text."""


def normalize_relpath(value: str | os.PathLike[str]) -> str:
    """Return a stable, NFC-normalized POSIX repository-relative path."""

    raw = os.fspath(value).replace("\\", "/")
    raw = unicodedata.normalize("NFC", raw)
    if not raw or raw.startswith("/") or re.match(r"^[A-Za-z]:/", raw):
        raise UnsafePathError(f"path is not repository-relative: {value!r}")
    normalized = posixpath.normpath(raw)
    if normalized in {"", "."} or normalized == ".." or normalized.startswith("../"):
        raise UnsafePathError(f"path escapes repository root: {value!r}")
    return normalized


def repo_relpath(root: Path, path: Path) -> str:
    """Resolve *path* beneath *root* and return its normalized relative path."""

    root_resolved = root.resolve()
    path_resolved = path.resolve()
    try:
        relative = path_resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise UnsafePathError(f"source is outside repository root: {path}") from exc
    return normalize_relpath(relative)


def ensure_within_root(root: Path, path: Path) -> Path:
    """Resolve a target and reject writes outside the declared repository."""

    root_resolved = root.resolve()
    candidate = path.resolve(strict=False)
    try:
        candidate.relative_to(root_resolved)
    except ValueError as exc:
        raise UnsafePathError(f"target is outside repository root: {path}") from exc
    return candidate


def glob_matches(path: str, pattern: str) -> bool:
    """Match repository POSIX paths with familiar glob semantics.

    ``fnmatch`` is intentionally combined with ``PurePosixPath.match`` so a
    pattern such as ``.agents/workflow-runs/**`` behaves as expected on both
    Windows and POSIX hosts.
    """

    path = normalize_relpath(path)
    pattern = unicodedata.normalize("NFC", pattern.replace("\\", "/"))
    if fnmatch.fnmatchcase(path, pattern):
        return True
    try:
        if PurePosixPath(path).match(pattern):
            return True
    except Exception:
        return False
    return False


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)
    if not isinstance(config, dict):
        raise ValueError("index config must be a JSON object")
    config.setdefault("include", ["**/*.md"])
    config.setdefault("exclude", [])
    config.setdefault("classification_rules", [])
    return config


def is_excluded(path: str, config: Mapping[str, Any]) -> bool:
    return any(glob_matches(path, str(pattern)) for pattern in config.get("exclude", []))


def is_included(path: str, config: Mapping[str, Any]) -> bool:
    if is_excluded(path, config):
        return False
    include = config.get("include", [])
    return not include or any(glob_matches(path, str(pattern)) for pattern in include)


def iter_candidate_files(root: Path, config: Mapping[str, Any]) -> Iterator[tuple[str, Path]]:
    """Yield eligible files in deterministic path order.

    Symlinks are ignored to keep the index confined to the declared root.
    ``os.walk`` is used instead of globbing so excluded directories are not
    traversed at all.
    """

    root = root.resolve()
    candidates: list[tuple[str, Path]] = []
    for current, dirnames, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)
        kept_dirs: list[str] = []
        for dirname in dirnames:
            candidate = current_path / dirname
            if candidate.is_symlink():
                continue
            # ``os.walk`` already guarantees that this directory is beneath
            # root and symlink directories were removed above; avoid a second
            # filesystem resolve on every directory during a no-op check.
            rel = normalize_relpath(candidate.relative_to(root))
            if is_excluded(rel + "/placeholder", config):
                continue
            kept_dirs.append(dirname)
        dirnames[:] = kept_dirs
        for filename in filenames:
            candidate = current_path / filename
            if candidate.is_symlink() or not candidate.is_file():
                continue
            rel = normalize_relpath(candidate.relative_to(root))
            if is_included(rel, config):
                candidates.append((rel, candidate))
    for rel, path in sorted(candidates, key=lambda pair: pair[0]):
        yield rel, path


def normalized_text(path: Path) -> str:
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise UnreadableSourceError(f"cannot read {path}: {exc}") from exc
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise UnreadableSourceError(f"source is not UTF-8 text: {path}") from exc


def normalized_bytes(path: Path) -> bytes:
    return normalized_text(path).encode("utf-8")


def content_hash_for_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def content_hash_for_path(path: Path) -> str:
    return content_hash_for_bytes(normalized_bytes(path))


def entry_hash_for(content_hash: str, relpath: str) -> str:
    normalized_path = normalize_relpath(relpath).encode("utf-8")
    return hashlib.sha256(content_hash.encode("ascii") + b"\0" + normalized_path).hexdigest()


def extract_title(relpath: str, text: str) -> str:
    match = HEADING_RE.search(text) if relpath.lower().endswith((".md", ".markdown")) else None
    if match:
        title = re.sub(r"[*_`~]", "", match.group(1)).strip()
        if title:
            return title
    return Path(relpath).stem


def extract_links(relpath: str, text: str) -> list[str]:
    if not relpath.lower().endswith((".md", ".markdown")):
        return []
    links: set[str] = set()
    for target in LINK_RE.findall(text):
        target = target.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "/", "\\")):
            continue
        try:
            base = posixpath.dirname(normalize_relpath(relpath))
            resolved = normalize_relpath(posixpath.join(base, target))
        except UnsafePathError:
            continue
        links.add(resolved)
    return sorted(links)


def _rule_specificity(glob: str) -> tuple[int, int]:
    literal = sum(1 for char in glob if char not in "*?[]")
    return literal, len(glob)


def classify_path(relpath: str, config: Mapping[str, Any]) -> dict[str, Any]:
    rules = [
        rule
        for rule in config.get("classification_rules", [])
        if isinstance(rule, Mapping) and glob_matches(relpath, str(rule.get("glob", "")))
    ]
    rules.sort(key=lambda rule: _rule_specificity(str(rule.get("glob", ""))), reverse=True)
    if rules:
        selected = rules[0]
        return {
            "type": str(selected.get("type", "supporting")),
            "authority": str(selected.get("authority", "supporting")),
            "source_status": str(selected.get("source_status", "unknown")),
            "default_search": bool(selected.get("default_search", True)),
        }
    return {
        "type": "supporting",
        "authority": "supporting",
        "source_status": "unknown",
        "default_search": True,
    }


def make_entry(root: Path, relpath: str, config: Mapping[str, Any], *, content_hash: str | None = None) -> dict[str, Any]:
    relpath = normalize_relpath(relpath)
    path = root / Path(*relpath.split("/"))
    before = path.stat()
    text = normalized_text(path)
    normalized = text.encode("utf-8")
    calculated_hash = content_hash_for_bytes(normalized)
    if content_hash is not None and content_hash != calculated_hash:
        raise UnreadableSourceError(f"content changed while indexing {relpath}")
    after = path.stat()
    if (before.st_mtime_ns, before.st_size) != (after.st_mtime_ns, after.st_size):
        raise UnreadableSourceError(f"content changed during indexing {relpath}")
    classification = classify_path(relpath, config)
    return {
        "path": relpath,
        "title": extract_title(relpath, text),
        "type": classification["type"],
        "authority": classification["authority"],
        "source_status": classification["source_status"],
        "default_search": classification["default_search"],
        "index_state": "current",
        "content_hash": calculated_hash,
        "entry_hash": entry_hash_for(calculated_hash, relpath),
        "links": extract_links(relpath, text),
    }


def tree_fingerprint(entries: Iterable[Mapping[str, Any]]) -> str:
    digest = hashlib.sha256()
    for entry in sorted(entries, key=lambda item: str(item["path"])):
        fingerprint_fields = {
            "path": entry.get("path"),
            "entry_hash": entry.get("entry_hash"),
            "type": entry.get("type"),
            "authority": entry.get("authority"),
            "source_status": entry.get("source_status"),
            "default_search": entry.get("default_search"),
            "links": entry.get("links", []),
        }
        digest.update(json.dumps(fingerprint_fields, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def build_index(entries: Iterable[Mapping[str, Any]], *, baseline_commit: str | None = None) -> dict[str, Any]:
    ordered = sorted((dict(entry) for entry in entries), key=lambda item: item["path"])
    index: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generator_version": GENERATOR_VERSION,
        "derived": True,
        "canonical": False,
        "baseline_commit": baseline_commit or "unknown",
        "tree_fingerprint": tree_fingerprint(ordered),
        "entries": ordered,
    }
    return index


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(json_bytes(value))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def validate_index(index: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    for required in ("schema_version", "generator_version", "derived", "canonical", "tree_fingerprint", "entries"):
        if required not in index:
            errors.append(f"missing top-level field: {required}")
    if index.get("derived") is not True or index.get("canonical") is not False:
        errors.append("derived index must have derived=true and canonical=false")
    entries = index.get("entries")
    if not isinstance(entries, list):
        return errors + ["entries must be an array"]
    paths: set[str] = set()
    for position, entry in enumerate(entries):
        if not isinstance(entry, Mapping):
            errors.append(f"entry {position} is not an object")
            continue
        for required in ("path", "title", "type", "authority", "source_status", "default_search", "index_state", "content_hash", "entry_hash", "links"):
            if required not in entry:
                errors.append(f"entry {position} missing field: {required}")
        try:
            path = normalize_relpath(str(entry.get("path", "")))
        except UnsafePathError:
            errors.append(f"entry {position} has unsafe path")
            continue
        if path in paths:
            errors.append(f"duplicate path: {path}")
        paths.add(path)
        if entry.get("entry_hash") != entry_hash_for(str(entry.get("content_hash", "")), path):
            errors.append(f"entry hash mismatch: {path}")
    if isinstance(entries, list) and index.get("tree_fingerprint") != tree_fingerprint(entries):
        errors.append("tree_fingerprint does not match entries")
    return errors
