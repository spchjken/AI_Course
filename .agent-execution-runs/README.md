# Skill execution runs

Thư mục này là vùng runtime local cho trace của repository-local skill. Mỗi invocation dùng một thư mục `<execution-id>/` gồm `manifest.json` và `events.jsonl` append-only.

Chỉ `.gitignore` và `README.md` được commit. Raw traces không phải nguồn chuẩn, không được đưa vào derived index và mặc định chỉ giữ 30 ngày. Không lưu raw prompt, chain-of-thought, secret, dữ liệu cá nhân, environment dump hoặc toàn bộ tool response.

Dùng `.agents/execution-tracing/skill_trace.py` để mở, ghi event, đóng, kiểm định và xuất aggregate. Aggregate chỉ chứa counts/outcomes; muốn lưu làm bằng chứng thì xuất có chủ đích vào workflow run hoặc vị trí đã được phê duyệt.

Khi dọn dữ liệu quá hạn, xem danh sách từ validator rồi chỉ xóa đúng execution directory đã kiểm tra. Không xóa đệ quy toàn thư mục này.
