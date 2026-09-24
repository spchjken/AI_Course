# Kiểm định quản trị độc lập

- **Reviewer:** `/root/harness_discovery_split_governance_review`
- **Tính độc lập:** Lượt `fresh-review`; không tham gia tạo hoặc sửa các tệp triển khai được kiểm định.
- **Phạm vi:** Thay đổi chưa commit cho việc tách discovery khỏi validation của harness, gồm skill, workflow, decision record, ghi chú thiết kế, tài liệu portable, điều hướng và chỉ mục dẫn xuất.
- **Verdict:** `Fail` — còn một finding `Major` chưa được xử lý.

## Bằng chứng đã đọc trực tiếp

- `AGENTS.md`, `README.md`, `.agents/rules/README.md`.
- `.agents/workflows/README.md`, `.agents/workflows/agent-dispatch-protocol.md` và `.agents/skills/workflow-orchestration/SKILL.md`.
- `.agents/skills/repo-skill-creator/SKILL.md` cùng quy ước `agents/openai.yaml` liên quan.
- `.agents/skills/harness-improvement-discovery/SKILL.md` và `agents/openai.yaml` của skill.
- `.agents/workflows/validate-agent-harness-improvement.md` và hai ghi chú thiết kế liên quan.
- `.agents/decisions/2026-09-24-separate-harness-discovery-from-validation.md`.
- `temp/generalizable-agent-harness-patterns.md`.
- `.agents/generated/context-index.json`, cấu hình/công cụ kiểm tra index, `git status`, `git diff` và các tham chiếu tên cũ/tên mới trong kho.

## Kết quả theo tiêu chí

| Tiêu chí | Kết quả | Bằng chứng chính |
|---|---|---|
| Discovery là skill read-only, ngắn gọn, tự do cao | `Pass` | `SKILL.md` dòng 8–23 giữ phương pháp mở; dòng 57–63 cấm sửa harness, tự mở workflow hoặc sao chép dữ liệu nhạy cảm. Tệp chỉ dài 63 dòng và không dựng state machine/run registry. |
| Candidate tương thích đầu vào workflow và quy tắc một vấn đề gốc | `Pass` | Schema skill dòng 35–55 cung cấp mệnh đề, expected/observed, evidence, scope, impact, forbidden data và decision owner; workflow dòng 74–85 nhận đúng các trường này; workflow dòng 24–28 khóa một vấn đề gốc mỗi lượt. |
| Workflow không còn nhận trách nhiệm discovery rộng; tên/đường dẫn hiện hành nhất quán | `Pass` | Workflow dòng 14–22 loại audit mở, dòng 74–85 khóa đầu vào; `README.md` và `.agents/workflows/README.md` trỏ tới `validate-agent-harness-improvement.md`. Tên cũ chỉ còn trong hồ sơ lịch sử hoặc chú thích ánh xạ. |
| Không viết lại sai bằng chứng lịch sử | `Pass` | Các workflow-run và decision cũ vẫn giữ chuỗi `optimize-agent-harness-system`; decision mới dòng 38–44 yêu cầu bảo toàn lịch sử. So sánh Git cho thấy ghi chú thiết kế lịch sử chỉ đổi tiêu đề/liên kết hiện hành và thêm chú thích tên, còn phần nội dung lịch sử giữ nguyên. |
| Tài liệu portable có bootstrap pattern và giới hạn bằng chứng skill/workflow | `Pass` | `temp/generalizable-agent-harness-patterns.md` dòng 19–28 tách discovery/validation; dòng 159–177 nêu evidence envelope và giới hạn khi thiếu skill trace; dòng 571–585 đưa trình tự bootstrap; dòng 595–596 kiểm tra trực tiếp hai giới hạn này. |
| Governance decision và UI metadata hợp lệ | `Pass` | Decision ghi bối cảnh, phương án, bằng chứng thuận/nghịch, quyết định, chuyển đổi, phạm vi kiểm định lại và điều kiện xem xét lại. `openai.yaml` dùng chuỗi được quote, mô tả ngắn 39 ký tự và `default_prompt` nhắc đúng `$harness-improvement-discovery`. `quick_validate.py` đạt khi chạy Python ở UTF-8 mode. |
| Không chạm thay đổi `.gitignore` thuộc người dùng | `Pass` | Hồ sơ lượt chạy loại `.gitignore` khỏi phạm vi; reviewer không sửa tệp này. Diff hiện có `temp/*` được coi là dirty state ngoài phạm vi, chỉ đọc để đánh giá tính tái tạo của index. |
| Liên kết hiện hành và chỉ mục dẫn xuất nhất quán | `Fail` | Link validator không báo link thiếu, nhưng chỉ mục chứa nguồn `temp/` bị ignore/không được Git theo dõi và bản index hiện stale. Xem `HDS-001` và `HDS-002` trong `review-findings.md`. |

## Kiểm tra đã chạy

```text
python -X utf8 .agents/skills/repo-skill-creator/scripts/quick_validate.py .agents/skills/harness-improvement-discovery
Result: Skill is valid!

python .agents/indexing/validate_index.py --index .agents/generated/context-index.json
Result: valid_schema=true; missing_links=[]; stale_sources includes orchestration-log.md; pass=false

python -X utf8 .agents/indexing/sync_index.py --check
Result: exit 2

git check-ignore -v temp/generalizable-agent-harness-patterns.md temp/agent-dispatch-protocol.md
Result: both matched .gitignore:12 temp/*

git ls-files --error-unmatch <each temp path>
Result: exit 1 for both paths; neither is tracked
```

Lần chạy `quick_validate.py` không có `-X utf8` thất bại do Python trên Windows dùng `cp1252`; đây là giới hạn của script/môi trường hiện có, không phải lỗi frontmatter của skill. Chạy lại ở UTF-8 mode đã xác nhận skill hợp lệ.

## Điều kiện để re-review

1. Xử lý `HDS-001` mà không sửa thay đổi `.gitignore` ngoài phạm vi: committed index không được phụ thuộc vào nguồn ignored/untracked và không được đưa bản sao `temp/agent-dispatch-protocol.md` vào tìm kiếm mặc định.
2. Sau khi toàn bộ hồ sơ review đã tồn tại, tái sinh index bằng nguồn có thể tái tạo và làm cho `validate_index.py` cùng `sync_index.py --check` đều đạt.
3. Re-review chỉ cần tập trung vào cấu hình/phạm vi nguồn của index, diff `.agents/generated/context-index.json`, trạng thái Git của các nguồn được index và hai phép kiểm tra trên.

## Re-review 2026-09-24 — HDS-001 và HDS-002

- **Phạm vi:** Chỉ hai finding đã được `Accept`; không tái mở các tiêu chí đã đạt ở lượt đầu.
- **Bằng chứng sửa:** `finding-disposition.md`, `.agents/indexing/index-config.json`, `.agents/generated/context-index.json`, Git status/diff và kết quả kiểm tra xác định ngay trước khi nối phần re-review này.
- **Kết quả HDS-001:** `Resolved`. Cấu hình thêm đúng một exclude `temp/**`; index có `0` entry với đường dẫn `temp/*`. Hai tệp local vẫn bị `.gitignore:12` loại và không được force-add. Diff `.gitignore` giữ nguyên hai dòng đã có tại baseline review đầu; sửa finding không chạm tệp này.
- **Kết quả HDS-002:** `Resolved`. Trước khi reviewer nối đầu ra này, `validate_index.py` trả `pass: true`, `missing_sources: []`, `stale_sources: []`, `authority_mismatches: []`, `missing_links: []`; `sync_index.py --check` trả exit `0`.
- **Giới hạn thời điểm:** Việc nối lịch sử review làm thay đổi chính hai nguồn operational-evidence này sau snapshot vừa kiểm tra. Điều đó không phủ định phép re-review theo yêu cầu “current before reviewer output”; Điều phối viên phải tái sinh index lần cuối sau khi hồ sơ review và orchestration log ổn định.
- **Verdict mới nhất:** `Pass` — cả `HDS-001` và `HDS-002` đã được giải quyết; không còn `Blocker` hoặc `Major` trong phạm vi kiểm định này.
