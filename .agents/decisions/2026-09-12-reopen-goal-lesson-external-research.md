# Mở lại quy trình hoàn thiện bài học để thiết kế nghiên cứu nguồn bên ngoài

- Ngày: 2026-09-12
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình
- Phạm vi ảnh hưởng: `complete-goal-lessons`, `$curriculum-reference-research`, danh mục workflow và các lượt hoàn thiện bài học mới
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

`complete-goal-lessons` đã gọi `$curriculum-reference-research` có điều kiện cho khẳng định về công cụ, API, mô hình, giao diện, giá, quyền hạn, an toàn hoặc phương pháp gây tranh luận. Kỹ năng hiện quy định cách lập khẳng định, chọn loại nguồn, tìm bằng chứng thuận/nghịch và ghi phán quyết, nhưng chưa chỉ rõ công cụ tìm kiếm, cách dựng và mở rộng truy vấn, điều kiện dừng, cách xử lý khi công cụ không khả dụng hoặc mức nghiên cứu so sánh tối thiểu cho một bài học.

Vì vậy trạng thái `Active` tạo ấn tượng rằng workflow đã đủ xác định để tự động nghiên cứu nguồn ngoại lai trước khi soạn, trong khi một tác nhân vẫn có thể hoàn thành phần lớn nội dung từ nguồn nội bộ và tri thức trong trọng số mô hình mà không thực hiện một lượt tìm kiếm có thể truy vết.

## Các phương án đã cân nhắc

1. Giữ `Active` và yêu cầu Chủ sở hữu giáo trình nhắc tìm nguồn hoặc cung cấp danh sách nguồn trong từng lượt.
2. Bắt buộc khảo sát rộng khóa học tương tự và tài liệu khoa học cho mọi mục tiêu, bất kể quyết định cần đưa ra.
3. Tạm đưa workflow về `Proposed`, sau đó thiết kế cơ chế nghiên cứu có điều kiện nhưng tự động, gồm phép thử kích hoạt, công cụ, chiến lược tìm kiếm, đầu ra và cổng chất lượng.

## Bằng chứng thuận và nghịch

- Cơ chế hiện tại đã có nền tảng tốt: sổ khẳng định, thứ tự ưu tiên nguồn, bằng chứng thuận/nghịch, năm mức phán quyết và `references.md` cục bộ.
- Skill chưa biến yêu cầu “tìm nguồn” thành thao tác có thể lặp lại giữa các tác nhân hoặc môi trường công cụ khác nhau.
- Không phải bài học nào cũng cần khảo sát rộng; tìm kiếm không có câu hỏi quyết định dễ tạo danh mục nguồn dài nhưng không ảnh hưởng thiết kế.
- Nghiên cứu khóa học tương tự có thể phát hiện khoảng trống, chuẩn đầu ra và cách tổ chức thực hành, nhưng uy tín hoặc độ phổ biến của một khóa học không tự chứng minh hiệu quả sư phạm.
- Nghiên cứu khoa học có giá trị khi dân số, nhiệm vụ và điều kiện đủ gần đối tượng người mới của chương trình; kết quả không chuyển giao trực tiếp phải được ghi là giới hạn, không dùng làm bảo chứng trang trí.
- Công cụ tìm kiếm và quyền truy cập có thể khác theo phiên. Workflow cần đường dự phòng và phán quyết trung thực khi không thể mở hoặc kiểm tra nguồn gốc.

## Quyết định

- Chuyển `complete-goal-lessons` từ `Active` về `Proposed` cho tới khi cơ chế nghiên cứu nguồn bên ngoài được xác định và chạy thử có kiểm soát.
- Không hạ trạng thái chất lượng của nội dung hiện có chỉ vì thay đổi trạng thái workflow.
- Giữ Giai đoạn B và `$curriculum-reference-research` làm nền thiết kế, nhưng chưa coi chúng là hợp đồng tự động hóa hoàn chỉnh.
- Trước khi sửa tiếp workflow hoặc skill, cần chốt ba nhóm quyết định:
  1. Khi nào nghiên cứu bên ngoài là bắt buộc, tùy chọn hoặc không cần thiết.
  2. Công cụ nào được dùng, thứ tự thao tác tìm kiếm, cách mở và kiểm tra nguồn, ngân sách cùng điều kiện dừng.
  3. Dữ liệu nào được đưa về `references.md` hoặc hồ sơ nghiên cứu, cách đánh giá chất lượng, khả năng áp dụng và bằng chứng phản bác.
- Khi workflow còn `Proposed`, chỉ chạy thử có kiểm soát nếu Chủ sở hữu giáo trình cho phép; không tự động xử lý hàng loạt các mục tiêu.

## Hệ quả và phạm vi chuyển đổi

- `README.md`, `.agents/workflows/README.md` và `complete-goal-lessons.md` phải cùng ghi `Proposed`.
- Yêu cầu hoàn thiện một `gNN` mới phải nêu đây là lượt thử có kiểm soát nếu muốn thực thi trước khi cơ chế nghiên cứu được duyệt.
- Chưa sửa `$curriculum-reference-research` hoặc cấu trúc `references.md` trong quyết định này; các thay đổi đó phụ thuộc vào kết quả thảo luận ba nhóm quyết định.
- Các quyết định quản trị trước đây về quyền sở hữu tệp, kiểm định độc lập và bàn giao vẫn có hiệu lực.

## Điều kiện xem xét lại

- Có ma trận phép thử kích hoạt nghiên cứu cho khẳng định biến động, khẳng định sư phạm, tiền lệ giáo trình và quyết định thiết kế.
- Có hợp đồng công cụ và đường dự phòng khi không có tìm kiếm web, không mở được nguồn hoặc nguồn yêu cầu quyền truy cập.
- Có quy trình truy vấn, chọn nguồn, tìm bằng chứng phản bác, dừng tìm và ghi độ bất định đủ để một tác nhân khác lặp lại.
- Có đặc tả đầu ra phân biệt dữ kiện nguồn, suy luận áp dụng cho giáo trình và quyết định của Chủ sở hữu giáo trình.
- Có cổng chất lượng ngăn dùng snippet, nội dung tổng hợp không nguồn, tài liệu quảng bá hoặc nghiên cứu không phù hợp đối tượng làm bằng chứng quyết định.
- Cơ chế được chạy thử có kiểm soát trên ít nhất một khẳng định ổn định về phương pháp và một khẳng định biến động theo công cụ trước khi đề xuất trở lại `Active`.
