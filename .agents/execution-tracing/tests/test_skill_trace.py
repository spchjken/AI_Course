from __future__ import annotations

import argparse
import importlib.util
import json
import os
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
        for event_type in ("artifact", "check", "correction", "retry", "limitation", "note"):
            skill_trace.record_event(
                argparse.Namespace(
                    root=str(self.root), trace=started["trace_path"], type=event_type, summary=event_type, ref=[]
                )
            )
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
        lock.write_text(json.dumps({"pid": os.getpid(), "created": 0}), encoding="utf-8")
        with self.assertRaises(skill_trace.TraceError):
            skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary="blocked", ref=[]))
        lock.write_text(json.dumps({"pid": 2147483647, "created": 0}), encoding="utf-8")
        skill_trace.record_event(argparse.Namespace(root=str(self.root), trace=started["trace_path"], type="note", summary="recovered", ref=[]))
        self.assertFalse(lock.exists())

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
