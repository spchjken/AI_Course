# Đặc tả quy trình thay đổi kiến trúc giáo trình

- Ngày: 2026-09-05
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/workflows/change-curriculum-architecture.md`, `.agents/workflows/README.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Tệp cũ mới là tệp giữ chỗ, chưa trả lời đủ khi nào cần dùng, sẽ làm gì và kiểm chứng ra sao. Nếu để tác nhân AI tự lấp khoảng trống, lỗi cục bộ có thể bị nâng thành thay đổi kiến trúc, nguồn chuẩn có thể bị sửa trước quyết định của con người và bằng chứng cũ có thể tiếp tục được dùng dù đã mất hiệu lực.

## Các phương án đã cân nhắc

1. Giữ tệp ở trạng thái giữ chỗ tới khi có thay đổi thực tế.
2. Gộp xử lý kiến trúc vào `complete-goal-lessons`.
3. Tạo quy trình quản trị riêng với phép thử kích hoạt, hai chế độ thực thi, cổng quyết định của con người, kiểm định độc lập và bàn giao về quy trình sở hữu.

## Bằng chứng thuận và nghịch

- Kiến trúc nội dung, bản đồ chương trình, bản định hướng mục tiêu, bài học và chương trình dạy có quyền sở hữu khác nhau; thay đổi xuyên tầng cần thứ tự áp dụng tường minh.
- Tác nhân AI nhẹ cần đầu vào, đầu ra, điều kiện dừng và tệp được phép sửa để không tự mở rộng phạm vi.
- Tách quy trình làm tăng chi phí điều phối, nhưng giữ quản trị kiến trúc khỏi luồng viết bài vốn đã dài.
- Không phải mọi chênh lệch giữa nguồn chuẩn đều là quyết định mới; cần chế độ đồng bộ hạn chế bên cạnh thay đổi ngữ nghĩa.
- Kiểm tra cấu trúc không thay thế kiểm định ngữ nghĩa độc lập hay quyết định ưu tiên của con người.

## Quyết định

- Hoàn thiện `change-curriculum-architecture` thành quy trình độc lập ở trạng thái `Proposed` để chạy thử có kiểm soát.
- Chỉ kích hoạt khi thay đổi động tới cam kết chương trình, kết quả mục tiêu, ranh giới, điều kiện tiên quyết, quan hệ phụ thuộc hoặc sản phẩm trung gian.
- Phân biệt đồng bộ quyết định đã có thẩm quyền với thay đổi kiến trúc có ý nghĩa mới.
- Thay đổi ngữ nghĩa phải qua cổng quyết định của chủ sở hữu trước khi sửa nguồn chuẩn.
- Điều phối viên chịu trách nhiệm tập hợp đầu vào theo từng giai đoạn; bên phát hiện cung cấp yêu cầu và bằng chứng hiện có, Người phân tích xác định phạm vi ảnh hưởng, Người nghiên cứu bổ sung bằng chứng thực tế và Chủ sở hữu giáo trình cung cấp quyết định.
- Sau khi áp dụng phải kiểm định độc lập, làm mất hiệu lực bằng chứng cũ có chọn lọc và bàn giao công việc tiếp theo.
- Không dùng quy trình này để viết bài học, phân tích dạy thử hoặc cấp `Validated`.

## Hệ quả và phạm vi chuyển đổi

- Danh mục quy trình đổi trạng thái của tệp từ `Placeholder` sang `Proposed`.
- Lần chạy đầu phải được người dùng cho phép và được xem là chạy thử có kiểm soát.
- Việc sửa bài học hoặc chương trình dạy được chuyển cho quy trình sở hữu, không thực hiện ngầm trong cùng đơn vị công việc.
- Bằng chứng và trạng thái chỉ mất hiệu lực khi có đường ảnh hưởng cụ thể; không hạ trạng thái toàn bộ giáo trình.
- Thay đổi bộ quy tắc quản trị phải qua cơ chế thay đổi quy tắc riêng và phê duyệt tường minh.

## Điều kiện xem xét lại

- Lần chạy thử cho thấy phép thử kích hoạt thường định tuyến sai.
- Cổng quyết định hoặc kiểm định tạo vòng lặp không có điều kiện dừng.
- Cấu trúc nguồn chuẩn đổi khiến thứ tự quyền lực hoặc bản đồ ảnh hưởng không còn đúng.
- Có công cụ tự động đủ ổn định để thay một phần kiểm tra thủ công.
- Bằng chứng vận hành đủ để chuyển quy trình từ `Proposed` sang `Active`, hoặc cho thấy cần tách thêm quy trình chuyển đổi quy mô lớn.
