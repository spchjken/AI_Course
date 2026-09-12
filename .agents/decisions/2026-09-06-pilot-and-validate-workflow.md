# Thiết kế quy trình dạy thử và kiểm chứng

- Ngày: 2026-09-06
- Trạng thái: Đề xuất — chờ duyệt
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/workflows/pilot-and-validate.md`, `.agents/workflows/README.md`, `curriculum-content-architecture.md`, `ai-native-builder/pilots/`, `.agents/rules/curriculum-contract.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Hệ thống đã có điều kiện chất lượng trước dạy thử và phiếu phản hồi cho từng bài học, nhưng chưa có cơ chế xác định phiên bản nào được dạy, bằng chứng nào được phép dùng, ai quyết định áp dụng thay đổi, hay khi nào một lần dạy thử đủ để nâng trạng thái. Nếu lưu câu trả lời học viên trong tệp bài học chuẩn, dữ liệu cá nhân và bằng chứng theo từng phiên sẽ lẫn với nội dung giáo trình.

## Các phương án đã cân nhắc

1. Lưu phản hồi và phân tích trực tiếp trong thư mục bài học hoặc lộ trình.
2. Dùng một tệp kết luận duy nhất cho mỗi lần dạy thử.
3. Lưu hồ sơ dạy thử ẩn danh, tách khóa phiên bản, kế hoạch thu thập, bằng chứng, phân tích, quyết định và kiểm định; chỉ bàn giao thay đổi về tầng sở hữu sau quyết định của con người.

## Bằng chứng thuận và nghịch

- Hành vi quan sát, sản phẩm, kết quả đánh giá và thời lượng thực tế đáng tin hơn mức hài lòng hoặc nhận định đơn lẻ.
- Một phiên 1-1 vẫn có thể tạo bằng chứng hữu ích, nhưng không đủ để suy rộng ngoài người học, hình thức, phiên bản và môi trường đã quan sát.
- Người phân tích có thể đề xuất giải thích nhưng không nên tự chọn thay đổi vì bằng chứng dạy thử thường còn nhiều giả thuyết cạnh tranh.
- Dữ liệu học viên có thể chứa thông tin cá nhân, bí mật hoặc lịch sử tương tác không cần thiết cho kiểm định; kho dự án chỉ nên giữ phần đã giảm thiểu và ẩn danh.

## Quyết định

- Đưa `pilot-and-validate` lên trạng thái `Proposed` với chuỗi: chuẩn bị → khóa phiên bản → dạy thử do con người thực hiện → kiểm tra dữ liệu → phân tích → cổng quyết định của con người → kiểm định độc lập → bàn giao.
- Tạo `ai-native-builder/pilots/` làm nơi lưu hồ sơ dạy thử chính tắc. Mỗi hồ sơ có một đối tượng chính và tên không chứa danh tính.
- Tách kết quả phân tích khẳng định (`Supported`, `Partially supported`, `Contradicted`, `Inconclusive`) khỏi kết quả cổng chất lượng (`Pass`, `Fail`, `Not verified`).
- Không tự sửa giáo trình trong quy trình này. Mọi thay đổi được chấp nhận được chuyển tới quy trình sở hữu và cần một hồ sơ dạy thử mới nếu thay đổi làm mất hiệu lực bằng chứng cũ.
- `Validated` luôn là kết luận có phạm vi, gắn với đối tượng học viên, hình thức dạy, phiên bản nội dung và môi trường đã kiểm chứng.

## Hệ quả và phạm vi chuyển đổi

- Các bài học và lộ trình hiện có không tự được cấp `Validated`; chúng cần hồ sơ dạy thử, phân tích và kiểm định độc lập theo quy trình mới.
- `pilot-feedback-form.md` vẫn là công cụ chuẩn bị thu dữ liệu trong bài học; câu trả lời thực tế không được ghi vào tệp mẫu đó.
- Hồ sơ dạy thử không thay `.agents/workflow-runs/`, nơi chỉ lưu bằng chứng điều phối tác nhân.
- Nguồn chuẩn cấp kiến trúc và đặc tả giáo trình được cập nhật để nhận diện `pilots/` và ranh giới dữ liệu của nó.

## Điều kiện xem xét lại

- Dạy thử thực tế cho thấy bộ hồ sơ có nhiều tệp hơn mức cần thiết để tái dựng quyết định.
- Yêu cầu pháp lý hoặc nền tảng lưu dữ liệu thay đổi, làm cách ẩn danh hoặc nơi lưu hiện tại không còn phù hợp.
- Một mô hình dạy theo nhóm cần phân tích mẫu hoặc cơ chế đồng thuận khác với lộ trình 1-1.
- Bằng chứng vận hành cho thấy cổng quyết định hoặc cổng kiểm định cần được tách hoặc gộp lại.
