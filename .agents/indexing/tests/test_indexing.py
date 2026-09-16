from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import build_context_package  # noqa: E402
import index_core  # noqa: E402
import search_index  # noqa: E402
import sync_index  # noqa: E402


class IndexFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.config = self.root / "config.json"
        self.index = self.root / "index.json"
        self.cache = self.root / "cache.json"
        self.lock = self.root / "lock"
        self.config.write_text(
            json.dumps(
                {
                    "include": ["*.md"],
                    "exclude": ["generated/**", ".context-index-cache.json"],
                    "classification_rules": [
                        {
                            "glob": "ops/**",
                            "type": "operational-evidence",
                            "authority": "operational",
                            "source_status": "unknown",
                            "default_search": False,
                        },
                        {
                            "glob": "canonical/**",
                            "type": "rule",
                            "authority": "canonical",
                            "source_status": "active",
                            "default_search": True,
                        },
                    ],
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def run_sync(self, mode: str = "update") -> tuple[int, dict]:
        report = self.root / "report.json"
        code = sync_index.sync(
            root=self.root,
            config_path=self.config,
            index_path=self.index,
            cache_path=self.cache,
            lock_path=self.lock,
            mode=mode,
            report_path=report,
            baseline_commit="fixture",
        )
        return code, json.loads(report.read_text(encoding="utf-8"))

    def read_index(self) -> dict:
        return json.loads(self.index.read_text(encoding="utf-8"))

    def test_hashes_and_normalization(self) -> None:
        self.assertEqual(index_core.normalize_relpath("a\\b.md"), "a/b.md")
        self.assertEqual(index_core.normalize_relpath("é.md"), index_core.normalize_relpath("e\u0301.md"))
        digest = index_core.content_hash_for_bytes("a\n".encode())
        self.assertEqual(len(index_core.entry_hash_for(digest, "a.md")), 64)
        with self.assertRaises(index_core.UnsafePathError):
            index_core.normalize_relpath("../escape.md")

    def test_lifecycle_move_edit_delete_and_determinism(self) -> None:
        source = self.root / "canonical" / "note.md"
        source.parent.mkdir()
        source.write_text("# Original\nalpha\n", encoding="utf-8")
        code, report = self.run_sync("full")
        self.assertEqual(code, 0)
        self.assertEqual(report["entry_count"], 1)
        first_bytes = self.index.read_bytes()

        code, no_op = self.run_sync("update")
        self.assertEqual(code, 0)
        self.assertEqual(no_op["reused_count"], 1)
        self.assertFalse(no_op["events"])
        self.assertEqual(self.index.read_bytes(), first_bytes)

        original_stat = source.stat()
        source.write_text("# Original\nALPHA\n", encoding="utf-8")
        source.touch()
        # Simulate an external editor preserving the old metadata.
        os.utime(source, ns=(original_stat.st_atime_ns, original_stat.st_mtime_ns))
        check_code, check_report = self.run_sync("check")
        self.assertEqual(check_code, 2)
        self.assertEqual(check_report["status"], "stale")
        source.write_text("# Original\nbeta\n", encoding="utf-8")
        _, edited = self.run_sync("update")
        self.assertEqual([event["kind"] for event in edited["events"]], ["modified"])

        moved = self.root / "canonical" / "renamed.md"
        source.rename(moved)
        _, moved_report = self.run_sync("update")
        self.assertEqual([event["kind"] for event in moved_report["events"]], ["moved"])
        self.assertEqual(self.read_index()["entries"][0]["path"], "canonical/renamed.md")

        moved.write_text("# Changed while moving\ngamma\n", encoding="utf-8")
        edited_move = self.root / "canonical" / "edited.md"
        moved.rename(edited_move)
        _, move_edit_report = self.run_sync("update")
        self.assertEqual({event["kind"] for event in move_edit_report["events"]}, {"created", "deleted"})

        stable_bytes = self.index.read_bytes()
        self.run_sync("full")
        self.assertEqual(self.index.read_bytes(), stable_bytes)

        edited_move.unlink()
        _, deleted = self.run_sync("update")
        self.assertEqual([event["kind"] for event in deleted["events"]], ["deleted"])

    def test_duplicate_content_is_not_guessed_as_move(self) -> None:
        first = self.root / "canonical" / "one.md"
        first.parent.mkdir()
        first.write_text("same\n", encoding="utf-8")
        self.run_sync("full")
        second = self.root / "canonical" / "two.md"
        second.write_text("same\n", encoding="utf-8")
        _, copied = self.run_sync("update")
        self.assertEqual([event["kind"] for event in copied["events"]], ["copied"])
        first.unlink()
        _, duplicate_delete = self.run_sync("update")
        self.assertEqual([event["kind"] for event in duplicate_delete["events"]], ["deleted"])

    def test_case_only_rename_is_a_move(self) -> None:
        source = self.root / "canonical" / "Case.md"
        source.parent.mkdir()
        source.write_text("stable\n", encoding="utf-8")
        self.run_sync("full")
        renamed = self.root / "canonical" / "case.md"
        source.rename(renamed)
        _, report = self.run_sync("update")
        self.assertEqual([event["kind"] for event in report["events"]], ["moved"])

    def test_duplicate_hash_blocks_move_inference(self) -> None:
        original = self.root / "canonical" / "original.md"
        duplicate = self.root / "canonical" / "duplicate.md"
        replacement = self.root / "canonical" / "replacement.md"
        original.parent.mkdir()
        original.write_text("same\n", encoding="utf-8")
        self.run_sync("full")
        duplicate.write_text("same\n", encoding="utf-8")
        self.run_sync("update")
        original.unlink()
        replacement.write_text("same\n", encoding="utf-8")
        _, report = self.run_sync("update")
        self.assertNotIn("moved", {event["kind"] for event in report["events"]})
        self.assertIn("deleted", {event["kind"] for event in report["events"]})

    def test_unstable_read_retries_and_generated_cache_are_excluded(self) -> None:
        source = self.root / "canonical" / "retry.md"
        source.parent.mkdir()
        source.write_text("first\n", encoding="utf-8")
        generated = self.root / "generated"
        generated.mkdir()
        (generated / "ignored.md").write_text("ignore\n", encoding="utf-8")
        (self.root / ".context-index-cache.json").write_text("ignore\n", encoding="utf-8")
        self.run_sync("full")
        source.write_text("second\n", encoding="utf-8")
        real_hash = sync_index.content_hash_for_path
        with patch.object(sync_index, "content_hash_for_path", side_effect=[index_core.IndexErrorBase("transient"), real_hash(source)]):
            _, report = self.run_sync("update")
        self.assertEqual(report["hashed_count"], 2)
        paths = {entry["path"] for entry in self.read_index()["entries"]}
        self.assertEqual(paths, {"canonical/retry.md"})

    def test_search_rejects_tampered_authority_and_paths(self) -> None:
        source = self.root / "canonical" / "rules.md"
        source.parent.mkdir()
        source.write_text("# Quality gate\n", encoding="utf-8")
        self.run_sync("full")
        tampered = self.read_index()
        tampered["entries"][0]["authority"] = "supporting"
        tampered["tree_fingerprint"] = index_core.tree_fingerprint(tampered["entries"])
        self.index.write_text(json.dumps(tampered), encoding="utf-8")
        with self.assertRaises(ValueError):
            search_index.search(
                root=self.root, index_path=self.index, config_path=self.config, query="quality gate", backend="python"
            )
        with self.assertRaises(index_core.UnsafePathError):
            index_core.ensure_within_root(self.root, self.root.parent / "outside.json")

    def test_search_filters_operational_and_package_verification(self) -> None:
        canonical = self.root / "canonical" / "rules.md"
        operational = self.root / "ops" / "run.md"
        canonical.parent.mkdir()
        operational.parent.mkdir()
        canonical.write_text("# Quality gate\nUse the quality gate.\n", encoding="utf-8")
        operational.write_text("# Quality gate evidence\n", encoding="utf-8")
        self.run_sync("full")
        default_result = search_index.search(
            root=self.root, index_path=self.index, config_path=self.config, query="quality gate", backend="python"
        )
        self.assertEqual([item["path"] for item in default_result["results"]], ["canonical/rules.md"])
        all_result = search_index.search(
            root=self.root,
            index_path=self.index,
            config_path=self.config,
            query="quality gate",
            backend="python",
            include_operational=True,
        )
        self.assertEqual({item["path"] for item in all_result["results"]}, {"canonical/rules.md", "ops/run.md"})

        package = build_context_package.build_package(
            root=self.root,
            index_path=self.index,
            config_path=self.config,
            query="quality gate",
            task="fixture",
            role="worker",
            top=1,
        )
        self.assertTrue(package["source_verification"]["all_current"])
        canonical.write_text("# Changed\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            build_context_package.build_package(
                root=self.root,
                index_path=self.index,
                config_path=self.config,
                query="quality gate",
                task="fixture",
                role="worker",
                top=1,
            )


if __name__ == "__main__":
    unittest.main()
