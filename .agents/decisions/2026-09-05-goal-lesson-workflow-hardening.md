# Làm rõ quyền sở hữu và đường chuyển cấp trong quy trình hoàn thiện bài học

- Ngày: 2026-09-05
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `complete-goal-lessons`, `$lesson-authoring` và các lượt tác nhân thực hiện D0–D6
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Quy trình hoàn thiện bài học đã bổ sung phiếu phản hồi dạy thử và trạng thái `Release-ready`, nhưng một số phần chưa được đồng bộ. Đường chuyển xung đột kiến trúc, quyền sở hữu `references.md` và `review.md`, ánh xạ kỹ năng cho từng đơn vị công việc và cách xử lý `Not verified` còn mơ hồ.

## Các phương án đã cân nhắc

1. Giữ workflow làm tài liệu bao quát và để điều phối viên tự suy ra quyền sở hữu cùng đường chuyển cấp.
2. Tách mọi loại tệp thành một skill riêng trước khi tiếp tục.
3. Giữ bộ skill hiện có nhưng quy định tường minh quyền sở hữu, ánh xạ từng đơn vị công việc và đường bàn giao giữa các workflow.

## Bằng chứng thuận và nghịch

- Các tác nhân nhẹ cần ranh giới tệp và kỹ năng cụ thể; suy luận ngầm làm tăng số vòng sửa.
- `$lesson-authoring` đủ rộng để làm hợp đồng bao quát nhưng không thay thế `$assessment-design`, nghiên cứu nguồn hoặc kiểm định độc lập.
- Thêm skill riêng cho phiếu phản hồi ở thời điểm này sẽ tăng cơ chế quản trị trước khi có bằng chứng sử dụng lặp lại.
- Cho phép chuẩn bị mục tiêu độc lập giúp tránh tắc hàng đợi, nhưng bàn giao đầu ra chưa kiểm chứng sẽ truyền rủi ro xuống quan hệ phụ thuộc.

## Quyết định

- Phân biệt xung đột cục bộ với thay đổi kiến trúc. Thay đổi mục tiêu, điều kiện tiên quyết, quan hệ phụ thuộc, lời hứa chương trình hoặc nguồn chuẩn phải được bàn giao sang `change-curriculum-architecture`.
- Không bàn giao đầu ra chưa được kiểm chứng như một điều kiện tiên quyết đã đạt. Công việc độc lập ở mục tiêu khác chỉ được tiếp tục khi không sử dụng hoặc giả định phần chưa kiểm chứng.
- Giai đoạn B sở hữu `references.md`; giai đoạn D chỉ sử dụng và kiểm tra liên kết tới các khẳng định đã nghiên cứu.
- Người kiểm định độc lập sở hữu `review.md`; người soạn không tạo trước phán quyết hoặc tự nâng trạng thái.
- `$lesson-authoring` là hợp đồng bao quát cho phần soạn bài, nhưng từng đơn vị công việc phải gọi đúng kỹ năng chuyên trách. `$assessment-design` sở hữu phần đánh giá năng lực; việc thiết kế phiếu phản hồi trước dạy thử không gọi `$pilot-feedback-analysis`.
- Giai đoạn D gồm D0–D6 sau khi bỏ đơn vị tích hợp tài liệu tham khảo trùng quyền sở hữu.
- Mức tự tin do học viên tự báo cáo chỉ là bằng chứng bổ trợ, không tự đủ để nâng điểm hoặc cấp `Validated`.

## Hệ quả và phạm vi chuyển đổi

- `complete-goal-lessons.md` phải thể hiện đường bàn giao và tái nhập quy trình, đủ năm phán quyết nghiên cứu, vai trò `Orchestrator`, sáu tệp đầu ra ngoài `README.md` và hai đích trước dạy thử.
- `lesson-authoring/SKILL.md` phải tuân theo bộ tài liệu cùng quyền sở hữu do workflow quy định và tách tự kiểm tra của người soạn khỏi nghiệm thu độc lập.
- Các lời nhắc D0–D6 cũ phải được tạo lại từ ánh xạ kỹ năng mới; không hồi tố trạng thái các bài học chưa được triển khai.

## Điều kiện xem xét lại

- Bằng chứng triển khai cho thấy D0 hoặc D6 cần một skill chuyên trách thay vì `$lesson-authoring`.
- Phiếu phản hồi được thiết kế lặp lại đủ nhiều để chứng minh nhu cầu về một skill riêng.
- Cấu trúc bộ tài liệu bài học hoặc mô hình kiểm định độc lập thay đổi.
