# Kiểm định quản trị độc lập

- **Reviewer:** `/root/skill_execution_traces_governance_review`
- **Baseline:** `a65e86caff89feb4e7c065fa5a22443a83d4d23e`
- **Candidate evidence commit:** `cd811a4d8ff8fb6d0374d16985d6f13f60758f63`
- **Phán quyết:** `Fail`
- **Lý do:** còn bốn finding `Major` chưa được disposition và sửa: `STE-001` đến `STE-004`. Theo cổng giai đoạn H, candidate chưa đủ điều kiện `Pass` hoặc `Ratify`.

## Phạm vi và tính độc lập

Reviewer đọc trực tiếp nguồn chuẩn, workflow/giao thức, ba `SKILL.md` bị sửa, toàn bộ implementation/schema/tests, decision record, hồ sơ lượt chạy, Git diff/log/status, raw trace local và tài liệu portable hiện có. Kết luận không dựa vào phán quyết tự đánh giá trong `validation-report.md`; reviewer chỉ ghi `governance-review.md` và `review-findings.md`, không sửa implementation.

## Kết quả theo tiêu chí

| Tiêu chí | Kết quả | Bằng chứng chính |
|---|---|---|
| An toàn đường dẫn và Windows | `Fail` | `skill_trace.py:53-57` chỉ chặn symlink, không chặn Windows junction. Fixture trên Python 3.14 báo `is_symlink=False`, `is_junction=True`; `start` đã tạo execution directory trong target ngoài repository root rồi lỗi `ValueError` tại `skill_trace.py:247`. Xem `STE-001`. |
| Schema, validator và lifecycle | `Fail` | Schema yêu cầu kiểu chuỗi và `additionalProperties: false` tại `skill-trace.schema.json:18-46`; validator ép kiểu bằng `str(...)` tại `skill_trace.py:318,327`, chỉ kiểm tra skill keys bằng `issubset` tại `331-335`, không kiểm tra kiểu `parent_workflow_run`/`agent_id`, và không cấm nhiều event `started`. Fixture schema-invalid vẫn được validator trả `valid: true`, exit `0`. Xem `STE-002`. |
| Riêng tư của aggregate | `Fail` | `skill_trace.py:466-475` nhóm cả trace invalid theo raw `skill`/`sha256`. Fixture invalid với marker `PRIVATE_MARKER_DO_NOT_EXPORT` xuất marker hai lần trong aggregate dù payload tự ghi `counts-only; no summaries or refs`. Xem `STE-003`. |
| Sáu kịch bản cố định và comparison | `Fail` | Test hiện có xanh nhưng không chạy concurrency thật, không chứng minh append không viết lại lịch sử, không thử absolute Windows path/junction, không kiểm schema JSON đã commit và không kiểm aggregate trước trace invalid. Do đó claim `6/6` tại `validation-report.md:5-17` lớn hơn bằng chứng. Xem `STE-004`. |
| Append/concurrency assumptions | `Minor concern` | Lock `O_EXCL` bảo vệ một writer nhưng `.append.lock` không có metadata, timeout hay stale-lock recovery (`skill_trace.py:176-198`); crash có thể khóa trace vĩnh viễn. Xem `STE-005`. |
| Raw trace ignore và derived-index exclusion | `Pass` | `git check-ignore -v` xác nhận raw `manifest.json`/`events.jsonl` bị nested `.gitignore` chặn; chỉ `README.md` và `.gitignore` được track. `index-config.json:25-26` loại cả `temp/**` và `.agent-execution-runs/**`; generated index không chứa raw trace entry. |
| Aggregate không chứa summary/ref trong trace hợp lệ | `Pass có giới hạn` | Aggregate từ hai raw trace thật không chứa request/event summary hoặc refs; unit test hiện có cũng đạt. Kết quả không bao phủ trace invalid, là nguyên nhân `STE-003`. |
| Skill hash và Git evidence | `Pass có giới hạn` | Hai raw manifest ghi full baseline HEAD, dirty state và SHA-256; hash hiện tại của `repo-skill-creator` và `workflow-orchestration` khớp manifest. Baseline/candidate branch/implementation commit kiểm chứng được. `implementation-log.md:7` vẫn ghi evidence commit là pending dù commit review là `cd811a4`; cần đồng bộ trước ratification. |
| Giới hạn không có platform hook | `Pass` | Giới hạn được nêu rõ trong `execution-tracing/README.md:3`, decision record, implementation log và central contract; không có claim capture tự động tuyệt đối trong nguồn được commit. |
| Central contract và độ phình skill | `Pass` | Hợp đồng chung nằm trong `AGENTS.md`; chỉ ba skill chịu ảnh hưởng được thêm chỉ dẫn hẹp, không nhân bản schema/CLI trong mọi skill. Cả ba validator skill đạt. |
| `.gitignore` và quyền sở hữu | `Pass` | Diff baseline..candidate không chạm root `.gitignore`; dirty change `temp/*` tồn tại ngoài hai candidate commit và được ghi là pre-existing. Candidate chỉ thêm nested `.agent-execution-runs/.gitignore`. |
| Migration và rollback | `Pass` | `migration-and-rollback.md` không backfill lịch sử, giữ raw evidence tới expiry, rollback bằng revert commit mới và không đụng root `.gitignore`. |
| Tài liệu portable | `Minor concern` | `temp/generalizable-agent-harness-patterns.md:484` nói validator phải báo invocation thiếu, nhưng code chỉ liệt kê trace directory hiện có (`skill_trace.py:438-448`) và không thể suy ra invocation bị bỏ qua. Tệp cũng bị ignore nên thay đổi portable không tái dựng được từ candidate commit. Xem `STE-006`. |
| Hồ sơ orchestration tự tuân thủ hợp đồng mới | `Minor concern` | `orchestration-log.md` liệt kê execution ID trong cột output nhưng thiếu cột `Skill trace` và thiếu `trace_path` theo `agent-dispatch-protocol.md`; workflow trace đang mở dưới 24 giờ là hợp lệ trong lúc lượt chạy còn tiếp tục. Xem `STE-007`. |

## Phép kiểm tra đã chạy

```text
python -X utf8 -m unittest discover -s .agents/execution-tracing/tests -v
=> 7/7 pass

python -X utf8 .agents/skills/repo-skill-creator/scripts/quick_validate.py <affected-skill>
=> 3/3 pass

python -X utf8 -m unittest discover -s .agents/indexing/tests -v
=> 8/8 pass

python -X utf8 .agents/execution-tracing/skill_trace.py validate --all
=> 2 traces valid; 1 closed, 1 open dưới 24 giờ; exit 0

python -X utf8 .agents/execution-tracing/skill_trace.py aggregate --output temp/governance-review-skill-trace-aggregate.json --force
=> counts-only cho hai trace thật; file tạm đã xóa

python -X utf8 .agents/indexing/validate_index.py --index .agents/generated/context-index.json
=> schema valid nhưng stale orchestration-log; exit 1

python -X utf8 .agents/indexing/sync_index.py --check
=> exit 1

git diff --check a65e86caff89feb4e7c065fa5a22443a83d4d23e..cd811a4d8ff8fb6d0374d16985d6f13f60758f63
=> pass
```

Index failure hiện tại đến từ `orchestration-log.md` đã được Điều phối viên cập nhật sau evidence commit để mở work unit review; thêm chính hai tệp review cũng sẽ làm index stale. Đây không phải finding implementation riêng, nhưng index phải được tái sinh và cả `validate_index.py` lẫn `sync_index.py --check` phải đạt sau khi review/disposition ổn định và trước ratification.

Quét candidate/hồ sơ/raw trace theo các mẫu private key, OpenAI/GitHub/AWS token và credential phổ biến không thấy dữ liệu nhạy cảm thật; chuỗi duy nhất khớp là token giả trong negative unit test. Fixture review và aggregate tạm đã được xóa.

## Điều kiện để re-review

1. Disposition đầy đủ cho mọi finding; sửa `STE-001` đến `STE-004` trước khi xin `Pass`.
2. Bổ sung test Windows junction/symlink, schema/lifecycle tamper, invalid-trace aggregate, concurrency/append và toàn bộ mệnh đề của sáu kịch bản đã khóa.
3. Đồng bộ hồ sơ Git/skill trace, đóng trace workflow khi lượt kết thúc, sửa claim portable và tái sinh index sau khi hồ sơ ổn định.
4. Re-review phải chạy trên commit mới, giữ nguyên baseline và chỉ chấp nhận khi không còn `Blocker`/`Major`.
