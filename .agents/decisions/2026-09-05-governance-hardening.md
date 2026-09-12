# Làm rõ quản trị, nghiệm thu và cơ chế điều phối tác nhân AI

- Ngày: 2026-09-05
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/rules/`, `.agents/skills/`, `.agents/workflows/`, `README.md`, `ai-native-builder/curriculum-map.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Hệ thống đã yêu cầu lưu quyết định nhưng chưa có nơi chuẩn; ranh giới giữa kiến trúc nội dung và bản đồ chương trình chưa rõ; người soạn có thể tự chấm; thuật ngữ và nguyên nhân `Not verified` chưa được chuẩn hóa; cơ chế kích hoạt và đồng bộ kỹ năng còn mơ hồ.

## Các phương án đã cân nhắc

1. Chỉ sửa từng tài liệu tại chỗ, không tạo lớp quản trị chung.
2. Dùng mẫu nhật ký quyết định của học viên cho cả quyết định quản trị.
3. Tạo hồ sơ quyết định quản trị riêng và đồng bộ các quy tắc, kỹ năng, quy trình chịu ảnh hưởng.

## Bằng chứng thuận và nghịch

- Quy tắc cũ nhắc đến “nhật ký quyết định phù hợp” nhưng không định nghĩa vị trí hoặc cấu trúc.
- `ai-native-builder/shared/templates/decision-log.md` thuộc tài liệu dùng chung cho người học; dùng chung sẽ trộn quyết định quản trị với sản phẩm của học viên.
- Các cổng chất lượng cũ chặn kết quả đạt khi thiếu bằng chứng nhưng chưa chặn người soạn làm thẩm quyền nghiệm thu duy nhất.
- Giữ ba kết quả `Pass`, `Fail`, `Not verified` tránh phá cơ chế tự động; làm rõ ý nghĩa của chúng đủ để biểu diễn các nguyên nhân khác nhau.
- Lớp quản trị mới làm tăng chi phí bảo trì, nên phạm vi kiểm định lại phải dựa trên ảnh hưởng thay vì mặc định toàn bộ giáo trình.

## Quyết định

- Lưu hồ sơ quyết định quản trị trong `.agents/decisions/`, tách khỏi nhật ký quyết định của học viên.
- Kiến trúc nội dung là nguồn chuẩn về mục tiêu và quan hệ phụ thuộc; bản đồ chương trình là hình chiếu vận hành được suy ra từ đó.
- Người soạn được tự kiểm tra nhưng việc nghiệm thu cần kiểm định độc lập.
- Giữ `Pass`, `Fail`, `Not verified`; mọi `Not verified` phải nêu nguyên nhân và phạm vi kiểm định lại.
- Thêm bảng thuật ngữ, quy tắc thay đổi quản trị, hai cơ chế kích hoạt kỹ năng và danh sách kiểm tra đồng bộ danh mục kỹ năng.

## Hệ quả và phạm vi chuyển đổi

- Các thay đổi mới từ ngày này phải tuân thủ quy tắc đã cập nhật.
- Nội dung cũ không tự động mất trạng thái. Chỉ kiểm định lại phần chịu ảnh hưởng khi được sửa, đưa vào dạy thử hoặc phát hành, hay khi có quan hệ phụ thuộc cụ thể.
- Quy trình hoàn thiện bài học phải chuyển thông tin về người kiểm định độc lập và nguyên nhân `Not verified` trong đầu ra kiểm định.

## Điều kiện xem xét lại

- Công cụ không hỗ trợ phân tách người soạn và người kiểm định như giả định.
- Cơ chế tự động cần thêm trạng thái ngoài bốn mức trưởng thành hoặc ba kết quả của cổng bắt buộc.
- Bản đồ chương trình phát triển thành dữ liệu máy đọc có cấu trúc riêng.
