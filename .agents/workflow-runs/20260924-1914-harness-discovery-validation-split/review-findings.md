# Findings của kiểm định quản trị

## HDS-001 — `Major` — Chỉ mục commit phụ thuộc vào tệp `temp/` bị ignore và không được theo dõi

- **Mệnh đề:** `.agents/generated/context-index.json` không còn là snapshot kho có thể tái tạo cho worker khác, vì nó đưa hai tệp cục bộ dưới `temp/` vào `default_search=true`, trong đó có một bản sao của giao thức phân công hiện hành.
- **Hệ quả:** Sau clone/checkout, hai nguồn này không tồn tại nhưng index đã commit vẫn tham chiếu tới chúng; tìm kiếm mặc định cũng có thể trả `temp/agent-dispatch-protocol.md` thay vì nguồn chuẩn `.agents/workflows/agent-dispatch-protocol.md`. Điều này làm sai tính portable, truy vết và định tuyến thẩm quyền của derived index.
- **Bằng chứng tệp/phần:** `.agents/generated/context-index.json` dòng 2228–2238 thêm `temp/agent-dispatch-protocol.md` với `default_search: true`; dòng 2240–2262 thêm `temp/generalizable-agent-harness-patterns.md` với `default_search: true`. `.gitignore` dòng 12 là `temp/*`. `git check-ignore -v` xác nhận cả hai tệp bị ignore; `git ls-files --error-unmatch` trả exit 1 cho cả hai.
- **Bằng chứng phản bác đã kiểm tra:** Cả hai entry được gắn `authority: supporting`, không phải `canonical`, và link validator không báo link thiếu trong working tree hiện tại. Điều đó không giải quyết việc nguồn không được Git phân phối và bản sao giao thức vẫn tham gia tìm kiếm mặc định.
- **Yêu cầu disposition:** `Accept`, `Dispute`, `Need evidence`, `Out of scope` hoặc `Requires human decision` theo giao thức. Nếu `Accept`, sửa ở tầng sở hữu index/config hoặc phạm vi nguồn; không sửa `.gitignore` của người dùng chỉ để hợp thức hóa entry.
- **Phép kiểm tra đóng finding:** `git ls-files` và chính sách nguồn index phải thống nhất; index sau tái sinh không chứa nguồn ignored/untracked, không có bản sao giao thức cạnh tranh trong tìm kiếm mặc định, và cả `validate_index.py` lẫn `sync_index.py --check` đạt.

## HDS-002 — `Minor` — Snapshot index đã stale trước khi reviewer tạo đầu ra

- **Mệnh đề:** Ngay tại baseline review, `.agents/generated/context-index.json` không khớp nội dung hiện tại của hồ sơ lượt chạy.
- **Hệ quả:** Fingerprint/entry hash không phản ánh đúng working tree; thêm hai tệp review bắt buộc còn làm tăng phần cần tái sinh trước khi nghiệm thu.
- **Bằng chứng:** `python .agents/indexing/validate_index.py --index .agents/generated/context-index.json` trả `stale_sources: [.agents/workflow-runs/20260924-1914-harness-discovery-validation-split/orchestration-log.md]` và `pass: false`; `python -X utf8 .agents/indexing/sync_index.py --check` trả exit 2.
- **Yêu cầu disposition:** Có thể xử lý cùng lượt sửa `HDS-001`, nhưng phải tái sinh sau khi `governance-review.md` và `review-findings.md` đã ổn định.
- **Phép kiểm tra đóng finding:** `validate_index.py` trả `pass: true`, không còn missing/stale source; `sync_index.py --check` trả exit 0.

## Trạng thái re-review 2026-09-24

### HDS-001 — `Resolved`

- `finding-disposition.md` ghi `Accept` và sửa hẹp đúng tầng sở hữu index.
- `.agents/indexing/index-config.json` thêm `temp/**` vào `exclude`.
- `.agents/generated/context-index.json` có `0` entry `temp/*`; không còn bản sao giao thức hoặc portable note local trong tìm kiếm mặc định.
- `.gitignore` không bị sửa trong lượt khắc phục; diff hiện tại vẫn là thay đổi `temp/*` đã quan sát ở baseline review đầu.

### HDS-002 — `Resolved`

- Kiểm tra ngay trước khi nối trạng thái này: `validate_index.py` trả `pass: true` với mọi danh sách lỗi rỗng và exit `0`.
- `sync_index.py --check` trả exit `0`.
- Index đã current và có thể tái tạo trong baseline trước đầu ra re-review. Sau khi reviewer nối hai tệp operational-evidence này, cần tái sinh snapshot cuối như bước đóng cơ học; không cần mở lại finding nếu chỉ các hash/entry của hồ sơ review và orchestration log thay đổi.
