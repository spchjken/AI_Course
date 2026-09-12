# Đặt cổng khảo sát nguồn bên ngoài trước khi soạn bài học

- Ngày: 2026-09-12
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình
- Phạm vi ảnh hưởng: `complete-goal-lessons`, `$curriculum-reference-research`, `references.md` của từng mục tiêu và metadata khám phá skill
- Thay thế hồ sơ: Không có; tiếp tục quyết định `2026-09-12-reopen-goal-lesson-external-research.md`

## Bối cảnh và xung đột

Workflow cũ nghiên cứu hai lượt quanh giai đoạn thiết kế nhưng chỉ bắt buộc cho một số claim về công cụ, an toàn hoặc phương pháp gây tranh luận. Nó chưa buộc mỗi mục tiêu so sánh khung nội dung với tiền lệ giáo trình và nghiên cứu liên quan trước khi viết, đồng thời chưa chỉ dẫn cách dùng công cụ tìm kiếm hay điều kiện dừng.

## Các phương án đã cân nhắc

1. Chỉ tìm khi người dùng nêu nguồn hoặc một claim đã bị tranh chấp.
2. Khảo sát rộng trước khi có khung nội dung cụ thể.
3. Chạy một khảo sát nền bắt buộc sau hợp đồng thiết kế và dàn ý truy vết, trước khi viết nội dung; chỉ kiểm tra bổ sung có mục tiêu nếu phát sinh claim trọng yếu mới.

## Bằng chứng thuận và nghịch

- Khảo sát quá sớm thiếu câu hỏi so sánh cụ thể và dễ biến thành sưu tầm tài liệu.
- Khảo sát sau khi đã viết đầy đủ dễ tạo thiên kiến bảo vệ nội dung và tăng chi phí viết lại.
- Một lượt sau khung thiết kế nhưng trước văn bản cho phép phản biện phạm vi, thứ tự, thực hành và bằng chứng khi chi phí thay đổi còn thấp.
- Nguồn ngoài không có cùng đối tượng, lời hứa hoặc ràng buộc không thể là chuẩn mặc định; tiền lệ phải được đánh giá bằng logic và khả năng áp dụng.
- Claim mới có thể xuất hiện lúc viết; cấm mọi nghiên cứu bổ sung sẽ buộc giữ nội dung chưa kiểm chứng hoặc lặp lại toàn bộ khảo sát.

## Quyết định

- Mỗi `gNN` chạy đúng một khảo sát nền sau `learning-design-contract.md` và `content-trace.md`, trước D1–D6.
- Khảo sát dùng khả năng tìm kiếm và duyệt web mặc định của môi trường, với ngân sách hơi rộng hơn mức tối thiểu được ghi trong skill; không khóa workflow vào một nhà cung cấp.
- Mở nguồn gốc và kiểm tra trực tiếp; snippet hoặc tóm tắt do AI tạo không phải bằng chứng.
- Tạo `references.md` cho mọi mục tiêu, gồm bảng đối chiếu tiền lệ, sổ khẳng định và sổ bằng chứng.
- Đánh giá thiết kế bằng mục tiêu, đối tượng, ràng buộc và chất lượng bằng chứng. Không đổi nội dung chỉ để giống khóa học bên ngoài.
- Sau khảo sát nền, chỉ chạy kiểm tra bổ sung có mục tiêu cho claim trọng yếu mới; không lặp lại khảo sát toàn cảnh.

## Hệ quả và phạm vi chuyển đổi

- Chuyển thiết kế học tập và `content-trace.md` lên trước giai đoạn nghiên cứu trong `complete-goal-lessons`.
- `references.md` chuyển từ đầu ra có điều kiện thành đầu ra bắt buộc của mỗi mục tiêu.
- Hợp đồng hai bảng cũ của `references.md` được giữ nguyên và mở rộng bằng bảng đối chiếu tiền lệ; `refresh-volatile-content` phải chấp nhận cấu trúc mở rộng này.
- Mở rộng trigger và hướng dẫn công cụ của `$curriculum-reference-research`; đồng bộ metadata và danh mục skill.
- `complete-goal-lessons` vẫn giữ `Proposed` cho tới khi cơ chế mới được kiểm định và chạy thử có kiểm soát.

## Điều kiện xem xét lại

- Khảo sát nền tạo chi phí lớn nhưng không thay đổi hoặc củng cố được quyết định thiết kế qua nhiều mục tiêu liên tiếp.
- Giới hạn nguồn truy cập khiến ngân sách mặc định không khả thi.
- Chạy thử cho thấy cần tách nghiên cứu khoa học và khảo sát tiền lệ giáo trình thành hai skill hoặc hai loại hồ sơ.
- Cấu trúc `references.md` không đủ để Người kiểm định truy lại nguồn và phân biệt dữ kiện với suy luận.
