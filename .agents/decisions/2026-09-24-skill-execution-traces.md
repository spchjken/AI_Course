# Ghi vết thực thi kỹ năng cục bộ

- Ngày: 2026-09-24
- Trạng thái: Ratified — Chủ sở hữu đã chấp thuận tích hợp và publish ngày 2026-09-24
- Bên quyết định: Chủ sở hữu kho
- Phạm vi ảnh hưởng: hợp đồng tác nhân, skill cục bộ, giao thức điều phối, công cụ/hồ sơ vận hành và derived index
- Thay thế hồ sơ: Bổ sung phần còn chưa quyết định trong `2026-09-24-separate-harness-discovery-from-validation.md`

## Bối cảnh và xung đột

Repo lưu workflow runs nhưng không lưu lifecycle của standalone skill invocation. Vì vậy discovery có thể đọc quy trình dài nhưng không đo được skill nào đã chạy, phiên bản nào, có retry/correction hay kết quả gì.

Repo code cũng không nhận được platform hook khi host chọn hoặc nạp skill. Một giải pháp trong repo có thể bắt buộc và hỗ trợ ghi trace, nhưng không được tuyên bố capture tự động tuyệt đối.

## Các phương án đã cân nhắc

1. Không đổi và tiếp tục suy từ Git/workflow logs.
2. Yêu cầu từng skill tự định nghĩa log riêng.
3. Gửi telemetry ra dịch vụ ngoài.
4. Dùng recorder/schema chung trong repo, raw trace local/ignored và aggregate chỉ xuất có chủ đích.

Chọn phương án 4 vì có thể kiểm tra, không cần secret/dịch vụ ngoài và tránh nhân bản schema trong từng skill.

## Bằng chứng thuận và nghịch

Không có trace root hay recorder hiện hành; workflow logs chỉ chứng minh điều phối workflow. Mặt khác, hợp đồng dựa trên agent vẫn có thể bị bỏ qua nếu runtime không tuân thủ `AGENTS.md`. Validator và audit phát hiện được khoảng trống sau sự kiện nhưng không biến nó thành platform hook.

## Quyết định đề xuất

- Dùng `.agent-execution-runs/<execution-id>/` cho raw local traces và `.agents/execution-tracing/` cho recorder/schema/tests. Vị trí runtime ở root tránh yêu cầu quyền nâng cao cho mỗi invocation trong sandbox hiện tại.
- Mỗi trace gắn tên skill, hash `SKILL.md`, Git HEAD, thời điểm, request summary đã giới hạn, refs tương đối và event lifecycle append-only.
- Không có trường raw prompt, chain-of-thought, secret, personal data hay full response.
- Bắt buộc invocation contract tại `AGENTS.md`; workflow dispatch truyền trace id/path khi giao skill.
- Cho phép xuất aggregate counts/outcomes có chủ đích; raw runtime tree không được commit hoặc đưa vào derived index.
- Giữ cổng `Ratify` trước khi tích hợp vào `main`.

Ứng viên cuối là `6ce41a4`. Các phép tự kiểm tra đạt, nhưng kiểm định độc lập của chính SHA này là `Not verified` vì Chủ sở hữu đã yêu cầu dừng vòng review tiếp theo. Chủ sở hữu đã ratify với giới hạn bằng chứng này được ghi rõ; nó không được diễn giải thành `Pass` ngầm.

## Hệ quả và phạm vi chuyển đổi

Skill mới và cũ không cần sao chép logging prose; chúng dùng hợp đồng chung. Lượt đang chạy khi thay đổi có hiệu lực không bị hồi tố. Các invocation sau ratification phải mở trace trước hành động chuyên môn đầu tiên và đóng trace trước bàn giao cuối.

## Điều kiện xem xét lại

- Host cung cấp lifecycle hooks đáng tin cậy.
- Tỷ lệ trace thiếu/không đóng vẫn cao qua hai audit.
- Chi phí hai lệnh start/finish lớn hơn giá trị bằng chứng.
- Chính sách riêng tư hoặc retention của dự án thay đổi.
