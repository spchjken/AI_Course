from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "skill_trace.py"
SPEC = importlib.util.spec_from_file_location("skill_trace", SCRIPT)
skill_trace = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(skill_trace)


def schema_accepts(value, schema, root):
    if "$ref" in schema:
        target = root
        for part in schema["$ref"].removeprefix("#/").split("/"):
            target = target[part]
        return schema_accepts(value, target, root)
    if "anyOf" in schema and not any(schema_accepts(value, item, root) for item in schema["anyOf"]):
        return False
    if "oneOf" in schema and sum(schema_accepts(value, item, root) for item in schema["oneOf"]) != 1:
        return False
    if "const" in schema and value != schema["const"]:
        return False
    if "enum" in schema and value not in schema["enum"]:
        return False
    kinds = schema.get("type")
    if kinds:
        kinds = [kinds] if isinstance(kinds, str) else kinds
        matches = {
            "object": isinstance(value, dict), "array": isinstance(value, list),
            "string": isinstance(value, str), "null": value is None,
            "boolean": isinstance(value, bool),
            "integer": isinstance(value, int) and not isinstance(value, bool),
        }
        if not any(matches.get(kind, False) for kind in kinds):
            return False
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0) or len(value) > schema.get("maxLength", 10**9):
            return False
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            return False
    if isinstance(value, int) and not isinstance(value, bool) and value < schema.get("minimum", value):
        return False
    if isinstance(value, dict):
        if any(key not in value for key in schema.get("required", [])):
            return False
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False and any(key not in properties for key in value):
            return False
        if any(not schema_accepts(item, properties[key], root) for key, item in value.items() if key in properties):
            return False
    if isinstance(value, list) and "items" in schema:
        return all(schema_accepts(item, schema["items"], root) for item in value)
    return True


class SkillTraceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        skill = self.root / ".agents" / "skills" / "demo-skill"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: demo-skill\ndescription: Demo.\n---\n", encoding="utf-8")
        runtime = self.root / ".agent-execution-runs"
        runtime.mkdir()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def start_args(self, **overrides):
        values = {
            "root": str(self.root),
            "skill": "demo-skill",
            "summary": "Run the demo skill",
            "input_ref": ["README.md"],
            "parent_workflow_run": None,
            "agent_id": "/root/test",
            "retention_days": 30,
        }
        values.update(overrides)
        return argparse.Namespace(**values)

    def test_full_lifecycle_and_version_hash(self) -> None:
        with patch.object(skill_trace, "git_state", return_value=("a" * 40, True)):
            started = skill_trace.create_trace(self.start_args())
        directory = self.root / started["trace_path"]
        manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["skill"]["name"], "demo-skill")
        self.assertEqual(len(manifest["skill"]["sha256"]), 64)

        skill_trace.record_event(
            argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="check", summary="Check passed", ref=[])
        )
        skill_trace.finish_trace(
            argparse.Namespace(
                root=str(self.root),
                trace=started["trace_path"],
                outcome="completed",
                summary="Completed",
                output_ref=["output.md"],
            )
        )
        result = skill_trace.validate_trace(directory, self.root, 24)
        self.assertTrue(result["valid"])
        self.assertEqual(result["outcome"], "completed")

    def test_event_types_and_second_terminal_are_rejected(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        events_path = self.root / started["trace_path"] / "events.jsonl"
        prefix = events_path.read_bytes()
        for event_type in ("artifact", "check", "correction", "retry", "limitation", "note"):
            skill_trace.record_event(
                argparse.Namespace(
                    root=str(self.root), trace=started["trace_path"], type=event_type, summary=event_type, ref=[]
                )
            )
        self.assertTrue(events_path.read_bytes().startswith(prefix))
        finish = argparse.Namespace(
            root=str(self.root), trace=started["trace_path"], outcome="failed", summary="Failed safely", output_ref=[]
        )
        skill_trace.finish_trace(finish)
        before = (self.root / started["trace_path"] / "events.jsonl").read_bytes()
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.finish_trace(finish)
        self.assertEqual(before, (self.root / started["trace_path"] / "events.jsonl").read_bytes())

    def test_same_second_ids_are_unique(self) -> None:
        fixed = skill_trace.datetime(2026, 9, 24, 12, 0, tzinfo=skill_trace.timezone.utc)
        with patch.object(skill_trace, "utc_now", return_value=fixed):
            first = skill_trace.create_trace(self.start_args())
            second = skill_trace.create_trace(self.start_args())
        self.assertNotEqual(first["execution_id"], second["execution_id"])

    def test_concurrent_process_ids_are_unique(self) -> None:
        command = [str(SCRIPT), "--root", str(self.root), "start", "--skill", "demo-skill", "--summary", "Concurrent"]
        def invoke(_):
            result = subprocess.run([os.sys.executable, "-X", "utf8", *command], capture_output=True, text=True, check=True)
            return json.loads(result.stdout)["execution_id"]
        with ThreadPoolExecutor(max_workers=6) as pool:
            ids = list(pool.map(invoke, range(12)))
        self.assertEqual(len(ids), len(set(ids)))

    def test_invalid_skill_refs_summary_and_escape_are_rejected(self) -> None:
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.create_trace(self.start_args(skill="missing-skill"))
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.create_trace(self.start_args(summary="x" * 501))
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.create_trace(self.start_args(input_ref=["../outside.md"]))
        for ref in (r"C:\outside.md", r"\\server\share\outside.md"):
            with self.assertRaises(skill_trace.TraceError):
                skill_trace.create_trace(self.start_args(input_ref=[ref]))
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.create_trace(self.start_args(summary="token sk-abcdefghijklmnopqrstuvwxyz123456"))
        outside = self.root.parent / "outside"
        outside.mkdir(exist_ok=True)
        try:
            with self.assertRaises(skill_trace.TraceError):
                skill_trace.trace_dir_from_arg(self.root, str(outside))
        finally:
            outside.rmdir()

    def test_all_terminal_outcomes_validate(self) -> None:
        for outcome in sorted(skill_trace.OUTCOMES):
            started = skill_trace.create_trace(self.start_args(summary=f"Run {outcome}"))
            skill_trace.finish_trace(
                argparse.Namespace(
                    root=str(self.root), trace=started["trace_path"], outcome=outcome, summary=outcome, output_ref=[]
                )
            )
            result = skill_trace.validate_trace(self.root / started["trace_path"], self.root, 24)
            self.assertTrue(result["valid"])
            self.assertEqual(result["outcome"], outcome)

    def test_aggregate_contains_counts_not_content(self) -> None:
        started = skill_trace.create_trace(self.start_args(summary="Sensitive-free request summary"))
        skill_trace.record_event(
            argparse.Namespace(
                root=str(self.root), trace=started["trace_path"], type="correction", summary="Corrected scope", ref=[]
            )
        )
        skill_trace.finish_trace(
            argparse.Namespace(
                root=str(self.root), trace=started["trace_path"], outcome="completed", summary="Done", output_ref=[]
            )
        )
        args = argparse.Namespace(
            root=str(self.root), output="aggregate.json", max_open_hours=24, force=False
        )
        result = skill_trace.aggregate_command(args)
        serialized = json.dumps(result)
        self.assertNotIn("Sensitive-free request summary", serialized)
        self.assertNotIn("Corrected scope", serialized)
        self.assertEqual(result["skills"]["demo-skill"]["outcome:completed"], 1)
        self.assertEqual(len(result["skill_versions"]["demo-skill"]), 1)
        self.assertEqual(result["event_totals"]["correction"], 1)
        self.assertNotIn("output.md", serialized)

    def test_schema_lifecycle_tampering_is_rejected(self) -> None:
        mutations = (
            lambda m, e: m.update(request_summary=7),
            lambda m, e: m.update(input_refs=[7]),
            lambda m, e: m["skill"].update(extra="x"),
            lambda m, e: m.update(parent_workflow_run={"bad": True}),
            lambda m, e: e.append(dict(e[0], seq=2)),
            lambda m, e: e[0].update(at="2020-01-01T00:00:00Z"),
            lambda m, e: e[0].update(seq=True),
            lambda m, e: e[0].update(seq=1.0),
        )
        for mutation in mutations:
            started = skill_trace.create_trace(self.start_args())
            directory = self.root / started["trace_path"]
            manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
            events = skill_trace.read_events(directory / "events.jsonl")
            mutation(manifest, events)
            (directory / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            (directory / "events.jsonl").write_text("".join(json.dumps(e) + "\n" for e in events), encoding="utf-8")
            self.assertFalse(skill_trace.validate_trace(directory, self.root, 24)["valid"])

    def test_committed_schemas_accept_generated_data_and_reject_type_tampering(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        directory = self.root / started["trace_path"]
        manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
        events = skill_trace.read_events(directory / "events.jsonl")
        manifest_schema = json.loads((SCRIPT.parent / "skill-trace.schema.json").read_text(encoding="utf-8"))
        event_schema = json.loads((SCRIPT.parent / "skill-event.schema.json").read_text(encoding="utf-8"))
        self.assertTrue(schema_accepts(manifest, manifest_schema, manifest_schema))
        self.assertTrue(all(schema_accepts(event, event_schema, event_schema) for event in events))
        for bad_seq in (True, 1.0):
            tampered = dict(events[0], seq=bad_seq)
            self.assertFalse(schema_accepts(tampered, event_schema, event_schema))
        tampered_manifest = dict(manifest, request_summary=7)
        self.assertFalse(schema_accepts(tampered_manifest, manifest_schema, manifest_schema))
        for bad_ref in ("ftp://example.com/file", r"..\outside.md", "https://user:pass@example.com/file", "https://example.com/file?q=1"):
            tampered_manifest = dict(manifest, input_refs=[bad_ref])
            self.assertFalse(schema_accepts(tampered_manifest, manifest_schema, manifest_schema), bad_ref)
            tampered_event = dict(events[0], refs=[bad_ref])
            self.assertFalse(schema_accepts(tampered_event, event_schema, event_schema), bad_ref)
        tampered_manifest = dict(manifest, parent_workflow_run="../outside")
        self.assertFalse(schema_accepts(tampered_manifest, manifest_schema, manifest_schema))

    def test_invalid_trace_dimensions_never_reach_aggregate(self) -> None:
        marker = "PRIVATE_MARKER_DO_NOT_EXPORT"
        started = skill_trace.create_trace(self.start_args())
        manifest_path = self.root / started["trace_path"] / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["skill"]["name"] = marker
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        result = skill_trace.aggregate_command(argparse.Namespace(root=str(self.root), output="aggregate.json", max_open_hours=24, force=False))
        self.assertNotIn(marker, json.dumps(result))
        self.assertEqual(result["invalid_count"], 1)

    def test_active_lock_blocks_and_stale_dead_lock_recovers(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        directory = self.root / started["trace_path"]
        lock = directory / ".append.lock"
        lock.mkdir()
        (lock / "owner.json").write_text(json.dumps({"pid": os.getpid(), "created": 0}), encoding="utf-8")
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.acquire_lock(lock, wait_seconds=0.05)
        (lock / "owner.json").write_text(json.dumps({"pid": 2147483647, "created": 0}), encoding="utf-8")
        os.utime(lock, (0, 0))
        skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary="recovered", ref=[]))
        self.assertFalse(lock.exists())
        lock.mkdir()
        (lock / "owner.json").write_text("", encoding="utf-8")
        os.utime(lock, (0, 0))
        skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary="recovered malformed", ref=[]))

    def test_concurrent_writers_are_serialized_without_event_loss(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        def append(index):
            skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary=f"note {index}", ref=[]))
        with ThreadPoolExecutor(max_workers=12) as pool:
            list(pool.map(append, range(24)))
        events = skill_trace.read_events(self.root / started["trace_path"] / "events.jsonl")
        self.assertEqual([event["seq"] for event in events], list(range(1, 26)))

    def test_concurrent_process_writers_are_serialized_without_event_loss(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        def append(index):
            command = [os.sys.executable, "-X", "utf8", str(SCRIPT), "--root", str(self.root), "event", "--trace", started["trace_path"], "--type", "note", "--summary", f"process {index}"]
            return subprocess.run(command, capture_output=True, text=True, timeout=35)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(append, range(12)))
        self.assertTrue(all(result.returncode == 0 for result in results), [result.stderr for result in results])
        events = skill_trace.read_events(self.root / started["trace_path"] / "events.jsonl")
        self.assertEqual([event["seq"] for event in events], list(range(1, 14)))
        self.assertFalse((self.root / started["trace_path"] / ".append.lock").exists())

    def test_hardlinked_events_file_is_rejected_without_external_write(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        events = self.root / started["trace_path"] / "events.jsonl"
        outside = self.root.parent / f"outside-{os.getpid()}.jsonl"
        original = events.read_bytes()
        events.unlink()
        outside.write_bytes(original)
        try:
            os.link(outside, events)
            with self.assertRaises(skill_trace.TraceError):
                skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary="blocked", ref=[]))
            self.assertEqual(outside.read_bytes(), original)
        finally:
            if events.exists():
                events.unlink()
            outside.unlink(missing_ok=True)

    @unittest.skipUnless(os.name == "nt", "Windows junction behavior")
    def test_junction_trace_root_is_rejected_without_outside_write(self) -> None:
        runtime = self.root / ".agent-execution-runs"
        runtime.rmdir()
        outside = Path(tempfile.mkdtemp())
        try:
            subprocess.run(["cmd", "/c", "mklink", "/J", str(runtime), str(outside)], check=True, capture_output=True)
            with self.assertRaises(skill_trace.TraceError):
                skill_trace.create_trace(self.start_args())
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            if runtime.exists():
                subprocess.run(["cmd", "/c", "rmdir", str(runtime)], check=True)
            outside.rmdir()

    @unittest.skipUnless(os.name == "nt", "Windows nested junction behavior")
    def test_nested_junction_trace_directory_is_rejected(self) -> None:
        outside = Path(tempfile.mkdtemp())
        linked = self.root / ".agent-execution-runs" / "linked"
        try:
            subprocess.run(["cmd", "/c", "mklink", "/J", str(linked), str(outside)], check=True, capture_output=True)
            with self.assertRaises(skill_trace.TraceError):
                skill_trace.trace_dir_from_arg(self.root, str(linked))
        finally:
            if linked.exists():
                subprocess.run(["cmd", "/c", "rmdir", str(linked)], check=True)
            outside.rmdir()

    def test_validator_rejects_unexpected_sensitive_field_and_malformed_directory(self) -> None:
        started = skill_trace.create_trace(self.start_args())
        directory = self.root / started["trace_path"]
        manifest_path = directory / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["raw_prompt"] = "must never be accepted"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        result = skill_trace.validate_trace(directory, self.root, 24)
        self.assertFalse(result["valid"])
        self.assertTrue(any("unexpected manifest fields" in error for error in result["errors"]))

        malformed = self.root / ".agent-execution-runs" / "malformed"
        malformed.mkdir()
        directories = skill_trace.iter_trace_dirs(self.root)
        self.assertIn(malformed, directories)


if __name__ == "__main__":
    unittest.main()
