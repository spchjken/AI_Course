#!/usr/bin/env python3
"""Read-only scan of local volatile-claim ledgers.

The script intentionally does not fetch sources or modify references.md. It finds
claim ledgers, validates their minimum machine-readable metadata, and renders a
derived queue for refresh-volatile-content.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from dataclasses import dataclass
from pathlib import Path


CLAIM_HEADERS = [
    "Mã khẳng định",
    "Khẳng định",
    "Loại khẳng định",
    "Độ cập nhật cần thiết",
    "Tác động quyết định",
    "Mức rủi ro",
    "Phán quyết",
    "Ngày kiểm tra",
    "Phiên bản/phạm vi",
    "Vị trí sử dụng",
    "Điều kiện kiểm tra lại",
    "Ngày kiểm tra tiếp theo",
]

EVIDENCE_HEADERS = [
    "Mã khẳng định",
    "Mã nguồn",
    "Nguồn",
    "Thẩm quyền",
    "Ngày công bố/cập nhật",
    "Ngày kiểm tra",
    "Phiên bản/phạm vi",
    "Chiều bằng chứng",
    "Phần được hỗ trợ",
    "Giới hạn",
]

ALLOWED_CURRENCY = {"Stable", "Version-bound", "Rapidly changing"}
ALLOWED_RISK = {"Low", "Medium", "High", "Critical"}
ALLOWED_VERDICTS = {
    "Supported",
    "Partially supported",
    "Not supported",
    "Contradicted",
    "Inconclusive",
}
ALLOWED_EVIDENCE_DIRECTIONS = {"Supporting", "Falsifying", "Limiting"}
EMPTY_VALUES = {"", "-", "—"}
RISK_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
LESSON_PACKAGE_MARKERS = {
    "lesson.md",
    "practice.md",
    "instructor-guide.md",
    "assessment.md",
    "pilot-feedback-form.md",
}


@dataclass
class Claim:
    path: Path
    line: int
    values: dict[str, str]


@dataclass
class Evidence:
    path: Path
    line: int
    values: dict[str, str]


@dataclass
class Issue:
    path: Path
    line: int
    claim_id: str
    message: str


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    cells = split_row(line)
    return bool(cells) and all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def markdown_tables(lines: list[str]):
    index = 0
    while index + 1 < len(lines):
        if "|" not in lines[index] or "|" not in lines[index + 1] or not is_separator(lines[index + 1]):
            index += 1
            continue
        header = split_row(lines[index])
        rows: list[tuple[int, list[str]]] = []
        cursor = index + 2
        while cursor < len(lines) and "|" in lines[cursor] and lines[cursor].strip():
            rows.append((cursor + 1, split_row(lines[cursor])))
            cursor += 1
        yield index + 1, header, rows
        index = cursor


def parse_iso_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def collect_ledgers(root: Path) -> tuple[list[Claim], list[Evidence], list[Issue], int]:
    claims: list[Claim] = []
    evidence: list[Evidence] = []
    issues: list[Issue] = []
    ledger_count = 0
    for path in sorted(root.rglob("references.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        found_claim_ledger = False
        found_evidence_ledger = False
        for header_line, header, rows in markdown_tables(lines):
            if "Mã khẳng định" in header and "Khẳng định" in header:
                found_claim_ledger = True
                missing = [name for name in CLAIM_HEADERS if name not in header]
                if missing:
                    issues.append(Issue(path, header_line, "", f"Sổ khẳng định thiếu cột: {', '.join(missing)}"))
                    continue
                for line, row in rows:
                    if len(row) != len(header):
                        issues.append(Issue(path, line, "", "Số ô không khớp số cột trong sổ khẳng định."))
                        continue
                    claims.append(Claim(path, line, dict(zip(header, row, strict=True))))
            elif "Mã khẳng định" in header and "Mã nguồn" in header:
                found_evidence_ledger = True
                missing = [name for name in EVIDENCE_HEADERS if name not in header]
                if missing:
                    issues.append(Issue(path, header_line, "", f"Sổ bằng chứng thiếu cột: {', '.join(missing)}"))
                    continue
                for line, row in rows:
                    if len(row) != len(header):
                        issues.append(Issue(path, line, "", "Số ô không khớp số cột trong sổ bằng chứng."))
                        continue
                    evidence.append(Evidence(path, line, dict(zip(header, row, strict=True))))
        if found_claim_ledger:
            ledger_count += 1
        else:
            issues.append(Issue(path, 1, "", "Không tìm thấy bảng `Sổ khẳng định` có các cột nhận diện."))
        if not found_evidence_ledger:
            issues.append(Issue(path, 1, "", "Không tìm thấy bảng `Sổ bằng chứng` có các cột nhận diện."))
    return claims, evidence, issues, ledger_count


def validate_claim(claim: Claim, as_of: dt.date) -> tuple[list[Issue], list[str]]:
    values = claim.values
    claim_id = values["Mã khẳng định"]
    issues: list[Issue] = []
    reasons: list[str] = []

    required = [
        "Mã khẳng định",
        "Khẳng định",
        "Loại khẳng định",
        "Độ cập nhật cần thiết",
        "Tác động quyết định",
        "Mức rủi ro",
        "Phán quyết",
        "Ngày kiểm tra",
        "Phiên bản/phạm vi",
        "Vị trí sử dụng",
        "Điều kiện kiểm tra lại",
    ]
    for field in required:
        if values[field] in EMPTY_VALUES:
            issues.append(Issue(claim.path, claim.line, claim_id, f"Thiếu `{field}`."))

    currency = values["Độ cập nhật cần thiết"]
    if currency not in ALLOWED_CURRENCY:
        issues.append(Issue(claim.path, claim.line, claim_id, "`Độ cập nhật cần thiết` không hợp lệ."))
    risk = values["Mức rủi ro"]
    if risk not in ALLOWED_RISK:
        issues.append(Issue(claim.path, claim.line, claim_id, "`Mức rủi ro` không hợp lệ."))
    verdict = values["Phán quyết"]
    if verdict not in ALLOWED_VERDICTS:
        issues.append(Issue(claim.path, claim.line, claim_id, "`Phán quyết` không hợp lệ."))

    checked = values["Ngày kiểm tra"]
    if checked not in EMPTY_VALUES and parse_iso_date(checked) is None:
        issues.append(Issue(claim.path, claim.line, claim_id, "`Ngày kiểm tra` phải dùng YYYY-MM-DD."))

    next_check = values["Ngày kiểm tra tiếp theo"]
    if next_check not in EMPTY_VALUES:
        next_date = parse_iso_date(next_check)
        if next_date is None:
            issues.append(Issue(claim.path, claim.line, claim_id, "`Ngày kiểm tra tiếp theo` phải dùng YYYY-MM-DD hoặc —."))
        elif next_date <= as_of:
            reasons.append(f"Đến hạn {next_check}")
    elif currency == "Rapidly changing" and "trước" not in values["Điều kiện kiểm tra lại"].lower():
        issues.append(Issue(claim.path, claim.line, claim_id, "Claim thay đổi nhanh phải có ngày kiểm tra tiếp theo hoặc điều kiện trước khi sử dụng."))
        reasons.append("Thay đổi nhanh nhưng thiếu lịch hoặc điều kiện trước sử dụng")

    if verdict in {"Contradicted", "Not supported", "Inconclusive"}:
        reasons.append(f"Phán quyết hiện tại: {verdict}")
    return issues, reasons


def validate_evidence(claims: list[Claim], evidence: list[Evidence]) -> list[Issue]:
    issues: list[Issue] = []
    claims_by_file: dict[Path, set[str]] = {}
    evidence_by_claim: set[tuple[Path, str]] = set()
    seen_pairs: set[tuple[Path, str, str]] = set()
    source_targets: dict[tuple[Path, str], str] = {}

    for claim in claims:
        claims_by_file.setdefault(claim.path, set()).add(claim.values["Mã khẳng định"])

    required = [
        "Mã khẳng định",
        "Mã nguồn",
        "Nguồn",
        "Thẩm quyền",
        "Ngày kiểm tra",
        "Phiên bản/phạm vi",
        "Chiều bằng chứng",
        "Phần được hỗ trợ",
    ]
    for row in evidence:
        values = row.values
        claim_id = values["Mã khẳng định"]
        source_id = values["Mã nguồn"]
        for field in required:
            if values[field] in EMPTY_VALUES:
                issues.append(Issue(row.path, row.line, claim_id, f"Bằng chứng thiếu `{field}`."))

        checked = values["Ngày kiểm tra"]
        if checked not in EMPTY_VALUES and parse_iso_date(checked) is None:
            issues.append(Issue(row.path, row.line, claim_id, "`Ngày kiểm tra` của bằng chứng phải dùng YYYY-MM-DD."))
        published = values["Ngày công bố/cập nhật"]
        if published not in EMPTY_VALUES and parse_iso_date(published) is None:
            issues.append(Issue(row.path, row.line, claim_id, "`Ngày công bố/cập nhật` phải dùng YYYY-MM-DD hoặc —."))
        if values["Chiều bằng chứng"] not in ALLOWED_EVIDENCE_DIRECTIONS:
            issues.append(Issue(row.path, row.line, claim_id, "`Chiều bằng chứng` không hợp lệ."))
        if claim_id not in claims_by_file.get(row.path, set()):
            issues.append(Issue(row.path, row.line, claim_id, "Bằng chứng trỏ tới claim không tồn tại trong cùng tệp."))

        pair = (row.path, claim_id, source_id)
        if pair in seen_pairs:
            issues.append(Issue(row.path, row.line, claim_id, f"Trùng cặp claim–source `{source_id}`."))
        seen_pairs.add(pair)
        source_key = (row.path, source_id)
        previous_target = source_targets.get(source_key)
        if previous_target is not None and previous_target != values["Nguồn"]:
            issues.append(Issue(row.path, row.line, claim_id, f"Mã nguồn `{source_id}` ánh xạ tới nhiều nguồn khác nhau."))
        else:
            source_targets[source_key] = values["Nguồn"]
        evidence_by_claim.add((row.path, claim_id))

    for claim in claims:
        claim_id = claim.values["Mã khẳng định"]
        if (claim.path, claim_id) not in evidence_by_claim:
            issues.append(Issue(claim.path, claim.line, claim_id, "Claim không có hàng bằng chứng liên kết."))
    return issues


def audit_release_coverage(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    candidate_dirs = {path.parent for name in LESSON_PACKAGE_MARKERS for path in root.rglob(name)}
    for directory in sorted(candidate_dirs):
        if not (directory / "references.md").exists():
            issues.append(Issue(directory, 1, "", "Coverage not verified: gói bài học đã soạn nhưng thiếu `references.md`."))
    return issues


def render_markdown(
    claims: list[Claim],
    evidence: list[Evidence],
    issues: list[Issue],
    due_rows: list[tuple[Claim, list[str]]],
    as_of: dt.date,
    ledger_count: int,
    release_sweep: bool,
) -> str:
    lines = [
        "# Hàng đợi khẳng định dễ lỗi thời",
        "",
        f"- Ngày tham chiếu: {as_of.isoformat()}",
        f"- Chế độ: {'Rà soát trước phát hành' if release_sweep else 'Làm mới có mục tiêu'}",
        f"- Sổ khẳng định tìm thấy: {ledger_count}",
        f"- Khẳng định tìm thấy: {len(claims)}",
        f"- Hàng bằng chứng tìm thấy: {len(evidence)}",
        f"- Lỗi cấu trúc hoặc siêu dữ liệu: {len(issues)}",
        f"- Khẳng định cần xử lý: {len(due_rows)}",
        "",
        "## Khẳng định cần xử lý",
        "",
        "| Mức rủi ro | Mã khẳng định | Tệp | Dòng | Lý do | Phán quyết | Vị trí sử dụng |",
        "|---|---|---|---:|---|---|---|",
    ]
    for claim, reasons in due_rows:
        values = claim.values
        reason = "; ".join(reasons)
        lines.append(
            f"| {values['Mức rủi ro']} | {values['Mã khẳng định']} | `{claim.path.as_posix()}` | {claim.line} | {reason} | {values['Phán quyết']} | {values['Vị trí sử dụng']} |"
        )
    if not due_rows:
        lines.append("| — | — | — | — | Không có khẳng định đến hạn trong phạm vi quét. | — | — |")

    lines.extend(["", "## Lỗi cấu trúc hoặc siêu dữ liệu", "", "| Tệp | Dòng | Mã khẳng định | Vấn đề |", "|---|---:|---|---|"])
    for issue in issues:
        lines.append(f"| `{issue.path.as_posix()}` | {issue.line} | {issue.claim_id or '—'} | {issue.message} |")
    if not issues:
        lines.append("| — | — | — | Không có lỗi được phát hiện. |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan local volatile-claim ledgers without network access.")
    parser.add_argument("--root", type=Path, default=Path("ai-native-builder"), help="Directory to scan for references.md")
    parser.add_argument("--as-of", type=str, default=dt.date.today().isoformat(), help="Reference date in YYYY-MM-DD")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path")
    parser.add_argument("--strict", action="store_true", help="Return nonzero when schema or metadata issues are found")
    parser.add_argument("--release-sweep", action="store_true", help="Also check authored lesson packages for ledger coverage")
    args = parser.parse_args()

    as_of = parse_iso_date(args.as_of)
    if as_of is None:
        parser.error("--as-of must use YYYY-MM-DD")
    root = args.root.resolve()
    if not root.exists():
        parser.error(f"Scan root does not exist: {root}")

    claims, evidence, issues, ledger_count = collect_ledgers(root)
    issues.extend(validate_evidence(claims, evidence))
    if args.release_sweep:
        issues.extend(audit_release_coverage(root))
    due_rows: list[tuple[Claim, list[str]]] = []
    seen_ids: dict[str, Claim] = {}
    for claim in claims:
        claim_id = claim.values["Mã khẳng định"]
        if claim_id in seen_ids:
            issues.append(Issue(claim.path, claim.line, claim_id, f"Trùng mã với {seen_ids[claim_id].path.as_posix()}:{seen_ids[claim_id].line}."))
        else:
            seen_ids[claim_id] = claim
        claim_issues, reasons = validate_claim(claim, as_of)
        issues.extend(claim_issues)
        if reasons:
            due_rows.append((claim, reasons))

    due_rows.sort(key=lambda row: (RISK_ORDER.get(row[0].values["Mức rủi ro"], 99), row[0].values["Mã khẳng định"]))
    report = render_markdown(claims, evidence, issues, due_rows, as_of, ledger_count, args.release_sweep)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(report)
    return 1 if args.strict and issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
