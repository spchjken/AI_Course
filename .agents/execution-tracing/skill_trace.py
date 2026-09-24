from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import urlsplit


SCHEMA_VERSION = "1.0"
DEFAULT_RETENTION_DAYS = 30
DEFAULT_MAX_OPEN_HOURS = 24
SUMMARY_LIMIT = 500
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXECUTION_ID_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z-[a-z0-9-]+-[0-9a-f]{8}$")
EVENT_TYPES = {"artifact", "check", "correction", "retry", "limitation", "note"}
OUTCOMES = {"completed", "failed", "cancelled", "not-verified"}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"[?&](?:access_?token|api_?key|secret|token)=[^&\s]+", re.IGNORECASE),
)


class TraceError(ValueError):
    pass


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(moment: datetime | None = None) -> str:
    return (moment or utc_now()).isoformat(timespec="seconds").replace("+00:00", "Z")


def repository_root(override: str | None = None) -> Path:
    root = Path(override).resolve() if override else Path(__file__).resolve().parents[2]
    if not (root / ".agents" / "skills").is_dir():
        raise TraceError(f"repository root does not contain .agents/skills: {root}")
    return root


def trace_root(root: Path) -> Path:
    candidate = root / ".agent-execution-runs"
    if candidate.is_symlink():
        raise TraceError("trace root must not be a symlink")
    return candidate.resolve()


def ensure_within(parent: Path, candidate: Path) -> Path:
    parent_resolved = parent.resolve()
    candidate_resolved = candidate.resolve()
    try:
        candidate_resolved.relative_to(parent_resolved)
    except ValueError as exc:
        raise TraceError(f"path escapes allowed root: {candidate}") from exc
    return candidate_resolved


def normalize_summary(value: str, field: str = "summary") -> str:
    normalized = " ".join(value.split())
    if not normalized:
        raise TraceError(f"{field} must not be empty")
    if len(normalized) > SUMMARY_LIMIT:
        raise TraceError(f"{field} exceeds {SUMMARY_LIMIT} characters")
    for pattern in SECRET_PATTERNS:
        if pattern.search(normalized):
            raise TraceError(f"{field} resembles sensitive data and was rejected")
    return normalized


def normalize_ref(value: str, root: Path) -> str:
    raw = value.strip()
    if not raw:
        raise TraceError("reference must not be empty")
    parsed = urlsplit(raw)
    if parsed.scheme:
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise TraceError("external reference must be an HTTP(S) URL")
        if parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise TraceError("external URL must not contain credentials, query or fragment")
        return raw

    normalized = raw.replace("\\", "/")
    posix = PurePosixPath(normalized)
    windows = PureWindowsPath(raw)
    if posix.is_absolute() or windows.is_absolute() or windows.drive or ".." in posix.parts:
        raise TraceError(f"reference must be repository-relative: {value}")
    candidate = ensure_within(root, root / Path(*posix.parts))
    return candidate.relative_to(root).as_posix()


def validate_slug(value: str | None, field: str) -> str | None:
    if value is None:
        return None
    normalized = value.strip()
    if not normalized or len(normalized) > 160 or not re.fullmatch(r"[A-Za-z0-9._/-]+", normalized):
        raise TraceError(f"invalid {field}")
    if ".." in PurePosixPath(normalized.replace("\\", "/")).parts:
        raise TraceError(f"invalid {field}")
    return normalized


def git_state(root: Path) -> tuple[str | None, bool | None]:
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
        ).stdout.strip()
        dirty = bool(
            subprocess.run(
                ["git", "status", "--porcelain"], cwd=root, check=True, capture_output=True, text=True
            ).stdout.strip()
        )
        return head, dirty
    except (OSError, subprocess.CalledProcessError):
        return None, None


def atomic_json_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{secrets.token_hex(4)}.tmp")
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def read_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise TraceError(f"cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise TraceError(f"expected JSON object in {path}")
    return value


def trace_dir_from_arg(root: Path, value: str) -> Path:
    raw = Path(value)
    candidate = raw if raw.is_absolute() else root / raw
    resolved = ensure_within(trace_root(root), candidate)
    if not resolved.is_dir():
        raise TraceError(f"trace directory does not exist: {value}")
    return resolved


def read_events(path: Path) -> list[dict]:
    events: list[dict] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise TraceError(f"event line {line_number} is not an object")
                events.append(value)
    except (OSError, json.JSONDecodeError) as exc:
        raise TraceError(f"cannot read events from {path}: {exc}") from exc
    return events


def append_event(directory: Path, event: dict) -> None:
    lock = directory / ".append.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise TraceError("trace is currently locked by another writer") from exc
    os.close(descriptor)
    try:
        events_path = directory / "events.jsonl"
        events = read_events(events_path) if events_path.exists() else []
        if events and events[-1].get("event") == "finished":
            raise TraceError("trace already has a terminal event")
        event["seq"] = len(events) + 1
        encoded = (json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
        with events_path.open("ab") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def create_trace(args: argparse.Namespace) -> dict:
    root = repository_root(args.root)
    if args.retention_days < 1:
        raise TraceError("retention-days must be positive")
    if not SKILL_NAME_RE.fullmatch(args.skill):
        raise TraceError("skill name must use lowercase hyphen-case")
    skill_path = root / ".agents" / "skills" / args.skill / "SKILL.md"
    if not skill_path.is_file():
        raise TraceError(f"unknown repository-local skill: {args.skill}")
    summary = normalize_summary(args.summary, "request summary")
    input_refs = [normalize_ref(value, root) for value in args.input_ref]
    parent = validate_slug(args.parent_workflow_run, "parent workflow run")
    agent_id = validate_slug(args.agent_id, "agent id")
    now = utc_now()
    base_id = f"{now.strftime('%Y%m%dT%H%M%SZ')}-{args.skill}-{secrets.token_hex(4)}"
    directory = trace_root(root) / base_id
    directory.mkdir(parents=True, exist_ok=False)
    head, dirty = git_state(root)
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "execution_id": base_id,
        "execution_kind": "skill",
        "skill": {
            "name": args.skill,
            "path": skill_path.relative_to(root).as_posix(),
            "sha256": hashlib.sha256(skill_path.read_bytes()).hexdigest(),
        },
        "repository": {"head": head, "dirty": dirty},
        "started_at": iso_utc(now),
        "request_summary": summary,
        "input_refs": input_refs,
        "parent_workflow_run": parent,
        "agent_id": agent_id,
        "retention_days": args.retention_days,
        "privacy": {
            "raw_prompt": False,
            "chain_of_thought": False,
            "secrets": False,
            "personal_data": False,
        },
    }
    atomic_json_write(directory / "manifest.json", manifest)
    append_event(
        directory,
        {"event": "started", "at": manifest["started_at"], "summary": "Skill execution started", "refs": []},
    )
    return {"execution_id": base_id, "trace_path": directory.relative_to(root).as_posix()}


def record_event(args: argparse.Namespace) -> dict:
    root = repository_root(args.root)
    directory = trace_dir_from_arg(root, args.trace)
    summary = normalize_summary(args.summary)
    refs = [normalize_ref(value, root) for value in args.ref]
    append_event(directory, {"event": args.type, "at": iso_utc(), "summary": summary, "refs": refs})
    return {"execution_id": directory.name, "event": args.type, "recorded": True}


def finish_trace(args: argparse.Namespace) -> dict:
    root = repository_root(args.root)
    directory = trace_dir_from_arg(root, args.trace)
    summary = normalize_summary(args.summary, "outcome summary")
    refs = [normalize_ref(value, root) for value in args.output_ref]
    append_event(
        directory,
        {"event": "finished", "at": iso_utc(), "outcome": args.outcome, "summary": summary, "refs": refs},
    )
    return {"execution_id": directory.name, "outcome": args.outcome, "closed": True}


def parse_timestamp(value: object, field: str) -> datetime:
    if not isinstance(value, str):
        raise TraceError(f"{field} must be a timestamp string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise TraceError(f"invalid timestamp in {field}") from exc
    if parsed.tzinfo is None:
        raise TraceError(f"timestamp in {field} must include timezone")
    return parsed.astimezone(timezone.utc)


def validate_trace(directory: Path, root: Path, max_open_hours: int) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        manifest = read_json(directory / "manifest.json")
        events = read_events(directory / "events.jsonl")
    except TraceError as exc:
        return {"trace": directory.relative_to(root).as_posix(), "valid": False, "status": "invalid", "errors": [str(exc)]}

    required = {
        "schema_version",
        "execution_id",
        "execution_kind",
        "skill",
        "repository",
        "started_at",
        "request_summary",
        "input_refs",
        "retention_days",
        "privacy",
    }
    allowed_manifest = required | {"parent_workflow_run", "agent_id"}
    missing = sorted(required - set(manifest))
    if missing:
        errors.append(f"missing manifest fields: {', '.join(missing)}")
    extra = sorted(set(manifest) - allowed_manifest)
    if extra:
        errors.append(f"unexpected manifest fields: {', '.join(extra)}")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append("unsupported schema_version")
    if manifest.get("execution_id") != directory.name or not EXECUTION_ID_RE.fullmatch(directory.name):
        errors.append("execution_id does not match trace directory")
    if manifest.get("execution_kind") != "skill":
        errors.append("execution_kind must be skill")
    try:
        normalize_summary(str(manifest.get("request_summary", "")), "request summary")
    except TraceError as exc:
        errors.append(str(exc))
    input_refs = manifest.get("input_refs")
    if not isinstance(input_refs, list):
        errors.append("input_refs must be a list")
    else:
        for value in input_refs:
            try:
                normalize_ref(str(value), root)
            except TraceError as exc:
                errors.append(str(exc))

    skill = manifest.get("skill")
    if not isinstance(skill, dict) or not {"name", "path", "sha256"}.issubset(skill):
        errors.append("skill object is incomplete")
    elif not re.fullmatch(r"[0-9a-f]{64}", str(skill.get("sha256", ""))):
        errors.append("skill sha256 is invalid")
    else:
        skill_name = str(skill.get("name", ""))
        skill_path = str(skill.get("path", ""))
        if not SKILL_NAME_RE.fullmatch(skill_name):
            errors.append("skill name is invalid")
        try:
            normalized_skill_path = normalize_ref(skill_path, root)
            expected_path = f".agents/skills/{skill_name}/SKILL.md"
            if normalized_skill_path != expected_path:
                errors.append("skill path does not match skill name")
            current_path = root / normalized_skill_path
            if not current_path.is_file():
                warnings.append("skill source is no longer present")
            elif hashlib.sha256(current_path.read_bytes()).hexdigest() != skill.get("sha256"):
                warnings.append("skill source has changed since this execution")
        except TraceError as exc:
            errors.append(str(exc))

    repository = manifest.get("repository")
    if not isinstance(repository, dict) or set(repository) != {"head", "dirty"}:
        errors.append("repository object must contain only head and dirty")
    elif repository.get("head") is not None and not re.fullmatch(r"[0-9a-f]{40}", str(repository.get("head"))):
        errors.append("repository head must be a full SHA or null")
    elif repository.get("dirty") is not None and not isinstance(repository.get("dirty"), bool):
        errors.append("repository dirty must be boolean or null")

    privacy = manifest.get("privacy")
    privacy_keys = {"raw_prompt", "chain_of_thought", "secrets", "personal_data"}
    if not isinstance(privacy, dict) or set(privacy) != privacy_keys or any(privacy.get(key) is not False for key in privacy_keys):
        errors.append("privacy flags must all be false")

    retention_days = manifest.get("retention_days")
    if not isinstance(retention_days, int) or isinstance(retention_days, bool) or retention_days < 1:
        errors.append("retention_days must be a positive integer")

    if not events or events[0].get("event") != "started":
        errors.append("first event must be started")
    terminal_count = sum(event.get("event") == "finished" for event in events)
    if terminal_count > 1:
        errors.append("trace contains multiple terminal events")
    if terminal_count == 1 and events[-1].get("event") != "finished":
        errors.append("terminal event must be last")
    for index, event in enumerate(events, 1):
        allowed_event = {"seq", "event", "at", "summary", "refs"}
        if event.get("event") == "finished":
            allowed_event.add("outcome")
        extra_event = sorted(set(event) - allowed_event)
        if extra_event:
            errors.append(f"unexpected fields in event {index}: {', '.join(extra_event)}")
        if event.get("seq") != index:
            errors.append(f"event sequence mismatch at {index}")
        try:
            parse_timestamp(event.get("at"), f"event {index}")
            normalize_summary(str(event.get("summary", "")), f"event {index} summary")
        except TraceError as exc:
            errors.append(str(exc))
        refs = event.get("refs")
        if not isinstance(refs, list):
            errors.append(f"event {index} refs must be a list")
        else:
            for value in refs:
                try:
                    normalize_ref(str(value), root)
                except TraceError as exc:
                    errors.append(str(exc))
        event_type = event.get("event")
        if event_type not in EVENT_TYPES | {"started", "finished"}:
            errors.append(f"unknown event type at {index}")
        if event_type == "finished" and event.get("outcome") not in OUTCOMES:
            errors.append("terminal outcome is invalid")

    try:
        started = parse_timestamp(manifest.get("started_at"), "started_at")
    except TraceError as exc:
        errors.append(str(exc))
        started = utc_now()
    is_open = terminal_count == 0
    open_age = utc_now() - started
    expired_open = is_open and open_age > timedelta(hours=max_open_hours)
    if expired_open:
        errors.append(f"trace is open longer than {max_open_hours} hours")
    elif is_open:
        warnings.append("trace is still open")

    expired_retention = isinstance(retention_days, int) and utc_now() - started > timedelta(days=retention_days)
    if expired_retention:
        warnings.append("trace is older than its retention policy")
    outcome = events[-1].get("outcome") if events and events[-1].get("event") == "finished" else None
    return {
        "trace": directory.relative_to(root).as_posix(),
        "valid": not errors,
        "status": "invalid" if errors else ("open" if is_open else "closed"),
        "outcome": outcome,
        "skill": skill.get("name") if isinstance(skill, dict) else None,
        "skill_sha256": skill.get("sha256") if isinstance(skill, dict) else None,
        "event_counts": dict(Counter(str(event.get("event")) for event in events)),
        "expired_retention": expired_retention,
        "errors": errors,
        "warnings": warnings,
    }


def iter_trace_dirs(root: Path) -> list[Path]:
    runtime = trace_root(root)
    if not runtime.exists():
        return []
    return sorted(path for path in runtime.iterdir() if path.is_dir())


def validate_command(args: argparse.Namespace) -> tuple[dict, int]:
    root = repository_root(args.root)
    directories = [trace_dir_from_arg(root, args.trace)] if args.trace else iter_trace_dirs(root)
    results = [validate_trace(directory, root, args.max_open_hours) for directory in directories]
    invalid = sum(not item["valid"] for item in results)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "trace_count": len(results),
        "valid_count": len(results) - invalid,
        "invalid_count": invalid,
        "results": results,
    }
    return payload, 2 if invalid else 0


def aggregate_command(args: argparse.Namespace) -> dict:
    root = repository_root(args.root)
    results = [validate_trace(directory, root, args.max_open_hours) for directory in iter_trace_dirs(root)]
    by_skill: dict[str, Counter] = defaultdict(Counter)
    by_skill_version: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))
    event_totals: Counter = Counter()
    for item in results:
        skill = item.get("skill") or "unknown"
        by_skill[skill][item["status"]] += 1
        if item.get("outcome"):
            by_skill[skill][f"outcome:{item['outcome']}"] += 1
        version = item.get("skill_sha256") or "unknown"
        by_skill_version[skill][version][item["status"]] += 1
        if item.get("outcome"):
            by_skill_version[skill][version][f"outcome:{item['outcome']}"] += 1
        event_totals.update(item.get("event_counts", {}))
    payload = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": iso_utc(),
        "source": ".agent-execution-runs",
        "privacy": "counts-only; no summaries or refs",
        "trace_count": len(results),
        "valid_count": sum(item["valid"] for item in results),
        "invalid_count": sum(not item["valid"] for item in results),
        "open_count": sum(item["status"] == "open" for item in results),
        "expired_retention_count": sum(item.get("expired_retention", False) for item in results),
        "event_totals": dict(sorted(event_totals.items())),
        "skills": {skill: dict(sorted(counts.items())) for skill, counts in sorted(by_skill.items())},
        "skill_versions": {
            skill: {version: dict(sorted(counts.items())) for version, counts in sorted(versions.items())}
            for skill, versions in sorted(by_skill_version.items())
        },
    }
    output_ref = normalize_ref(args.output, root)
    if output_ref.startswith(("http://", "https://")):
        raise TraceError("aggregate output must be a repository-relative path")
    output = ensure_within(root, root / output_ref)
    if output.exists() and not args.force:
        raise TraceError(f"aggregate output already exists: {output_ref}; use --force to replace")
    atomic_json_write(output, payload)
    return {"output": output_ref, **payload}


def parser() -> argparse.ArgumentParser:
    root_parser = argparse.ArgumentParser(description="Record and validate repository-local skill execution traces.")
    root_parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    commands = root_parser.add_subparsers(dest="command", required=True)

    start = commands.add_parser("start", help="Create a new skill execution trace.")
    start.add_argument("--skill", required=True)
    start.add_argument("--summary", required=True)
    start.add_argument("--input-ref", action="append", default=[])
    start.add_argument("--parent-workflow-run")
    start.add_argument("--agent-id")
    start.add_argument("--retention-days", type=int, default=DEFAULT_RETENTION_DAYS)

    event = commands.add_parser("event", help="Append a bounded event to an open trace.")
    event.add_argument("--trace", required=True)
    event.add_argument("--type", required=True, choices=sorted(EVENT_TYPES))
    event.add_argument("--summary", required=True)
    event.add_argument("--ref", action="append", default=[])

    finish = commands.add_parser("finish", help="Close an open trace.")
    finish.add_argument("--trace", required=True)
    finish.add_argument("--outcome", required=True, choices=sorted(OUTCOMES))
    finish.add_argument("--summary", required=True)
    finish.add_argument("--output-ref", action="append", default=[])

    validate = commands.add_parser("validate", help="Validate one trace or all local traces.")
    target = validate.add_mutually_exclusive_group(required=True)
    target.add_argument("--trace")
    target.add_argument("--all", action="store_true")
    validate.add_argument("--max-open-hours", type=int, default=DEFAULT_MAX_OPEN_HOURS)

    aggregate = commands.add_parser("aggregate", help="Write a counts-only aggregate for audit/discovery.")
    aggregate.add_argument("--output", required=True)
    aggregate.add_argument("--max-open-hours", type=int, default=DEFAULT_MAX_OPEN_HOURS)
    aggregate.add_argument("--force", action="store_true")
    return root_parser


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "start":
            payload, code = create_trace(args), 0
        elif args.command == "event":
            payload, code = record_event(args), 0
        elif args.command == "finish":
            payload, code = finish_trace(args), 0
        elif args.command == "validate":
            payload, code = validate_command(args)
        elif args.command == "aggregate":
            payload, code = aggregate_command(args), 0
        else:
            raise TraceError("unknown command")
    except (TraceError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
