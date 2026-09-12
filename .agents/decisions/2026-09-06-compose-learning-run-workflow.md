# Thiết kế quy trình ghép lộ trình học

- Ngày: 2026-09-06
- Trạng thái: Đề xuất — chờ duyệt
- Bên đề xuất: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/workflows/compose-learning-run.md`, `.agents/workflows/README.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Tệp ghép lộ trình mới chỉ là tệp giữ chỗ. Nó chưa phân biệt việc phác thảo một lộ trình từ các mục tiêu đã chốt với việc đóng gói một lộ trình đủ điều kiện dạy thử. Nếu buộc mọi công việc phải chờ toàn bộ bài học hoàn thiện, việc phát hiện khoảng trống diễn ra quá muộn. Nếu cho phép lộ trình phác thảo được coi là sẵn sàng dạy, trạng thái chất lượng sẽ bị nâng vượt bằng chứng.

## Các phương án đã cân nhắc

1. Chỉ ghép lộ trình sau khi mọi bài học hoàn thiện và được kiểm định.
2. Cho phép ghép bất kỳ lúc nào và không phân biệt kết quả phác thảo với kết quả sẵn sàng dạy.
3. Dùng hai chế độ: phác thảo sớm để phát hiện và bàn giao khoảng trống; đóng gói để dạy chỉ khi các bài học bắt buộc đã đạt mức sẵn sàng.

## Bằng chứng thuận và nghịch

- Các mục tiêu và quan hệ phụ thuộc đã được chốt có thể cho biết một lời hứa có khả thi về trình tự và thời lượng trước khi bài học hoàn thiện.
- Mức trưởng thành bài học, kiểm định độc lập và bằng chứng dạy thử là những loại bằng chứng khác nhau; không được suy ra một loại từ loại khác.
- Việc gộp mục tiêu theo tương đồng chủ đề dễ bỏ qua vòng thực hành, sản phẩm trung gian và thời lượng phục hồi.
- Một tệp lộ trình chỉ nên điều phối và liên kết; sao chép nội dung chuẩn sẽ gây lệch nguồn và làm tăng chi phí bảo trì.

## Quyết định

- Thiết kế `compose-learning-run` với hai chế độ `Early composition` và `Delivery packaging`.
- Chế độ phác thảo sớm tạo hợp đồng, lịch dự kiến, ma trận bao phủ và danh sách khoảng trống, nhưng luôn giữ trạng thái `Needs revision`.
- Chế độ đóng gói để dạy chỉ tiếp tục sau khi mọi bài học bắt buộc tối thiểu `Pilot-ready`; sau kiểm định độc lập, lộ trình có thể đạt `Pilot-ready` hoặc `Release-ready`, không thể đạt `Validated`.
- Lộ trình phải được dựng ngược từ lời hứa, qua đồ thị điều kiện tiên quyết và sản phẩm trung gian, trước khi sắp buổi và tính thời lượng.
- Bất kỳ mâu thuẫn nào đòi đổi mục tiêu, quan hệ phụ thuộc hoặc cam kết đều được bàn giao sang `change-curriculum-architecture`; khoảng trống bài học bàn giao sang `complete-goal-lessons`; dạy thử bàn giao sang `pilot-and-validate`.
- Dùng mô hình phân công động chung. Người kiểm định độc lập là lượt tác nhân mới, tách với người thiết kế và người soạn.

## Hệ quả và phạm vi chuyển đổi

- Các lộ trình hiện có không tự được nâng trạng thái. Chúng cần đi qua quy trình mới khi được chỉnh sửa hoặc chuẩn bị dạy thử.
- Thư mục `runs/<run-slug>/` có bộ tệp điều phối với chủ sở hữu rõ ràng: hợp đồng, lịch, ma trận bao phủ, mức sẵn sàng và kết quả kiểm định; tệp theo buổi chỉ tạo khi thật sự cần.
- Kiểm định phải lần theo đường từ lời hứa tới mục tiêu, sản phẩm, điểm kiểm tra, phục hồi và buổi tiếp theo; không chỉ kiểm tra tiêu đề hay tổng thời lượng.
- Khi thực thi có tác nhân con, bằng chứng vòng đời và tính độc lập phải được lưu tại `.agents/workflow-runs/<run-id>/orchestration-log.md`.

## Điều kiện xem xét lại

- Dạy thử cho thấy hai chế độ tạo thêm chi phí điều phối mà không phát hiện khoảng trống sớm hơn.
- Một loại lộ trình mới cần bộ tệp hoặc cổng chất lượng khác đáng kể.
- Công cụ kiểm tra tự động xuất hiện và làm thay đổi ranh giới giữa kiểm tra xác định với kiểm định ngữ nghĩa.
- Bằng chứng vận hành cho thấy cấu trúc tác nhân đề xuất không phù hợp với môi trường thực thi.
