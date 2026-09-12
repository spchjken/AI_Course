# G01 — Định hướng vấn đề

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho học phần G01. Tác nhân AI triển khai dùng bản định hướng này để viết bài giảng, hoạt động và tài liệu kiểm định; không tự đổi kết quả, quan hệ phụ thuộc hoặc phạm vi.

## Đặc tả học phần

- **Vấn đề người học:** có thể trò chuyện với AI nhưng thường bắt đầu bằng một ý tưởng giải pháp mơ hồ, để AI chọn hộ vấn đề, người dùng và phạm vi.
- **Kết quả quan sát được:** học viên tự chọn và diễn đạt được một vấn đề đáng giải quyết, người dùng cụ thể, giá trị mong muốn, giới hạn và dấu hiệu thành công ban đầu; đồng thời giải thích được vì sao chưa chọn ít nhất một hướng khác.
- **Điều kiện tiên quyết:** biết mở và trao đổi nhiều lượt với một giao diện trò chuyện AI trên web; không yêu cầu biết mã nguồn.
- **Đầu vào:** trải nghiệm, nhu cầu hoặc lĩnh vực học viên quan tâm; có thể dùng một tình huống giả lập an toàn nếu chưa có dự án cá nhân.
- **Đầu ra cho G02:** một bản định hướng sản phẩm đủ rõ để chuyển thành hành vi người dùng và tiêu chí nghiệm thu.
- **Thời lượng thiết kế ban đầu:** lõi 60–75 phút; có thể mở rộng thêm phỏng vấn vấn đề và phản biện. Phải kiểm chứng lại bằng dạy thử.

## Phạm vi nội dung

### Phải có

1. Phân biệt “ý tưởng giải pháp” với “vấn đề của một người dùng trong một bối cảnh”.
2. Xác định người dùng chính, tình huống xảy ra vấn đề và thay đổi mong muốn.
3. Làm rõ giá trị: điều gì tốt hơn nếu vấn đề được giải quyết.
4. Chốt phạm vi đầu tiên, ràng buộc, điều không làm và dấu hiệu thành công ban đầu.
5. Biến giả định thành câu hỏi cần kiểm tra thay vì trình bày chúng như sự thật.
6. Dùng AI để phỏng vấn ngược, đưa cách hiểu cạnh tranh và phản biện tính hữu ích/khả thi.
7. So sánh ít nhất hai hướng rồi ghi quyết định của học viên.

### Chưa thuộc học phần này

- Viết danh sách tính năng hoặc tiêu chí nghiệm thu chi tiết.
- Chọn kiến trúc, khung công nghệ, API hoặc mô hình AI.
- Yêu cầu AI sinh ứng dụng để chứng minh ý tưởng.
- Nghiên cứu thị trường đầy đủ hoặc cam kết rằng nhu cầu đã được xác thực.

## Mạch học đề xuất

1. **Khởi động:** cho học viên mang vào một ý tưởng thô; chỉ ra phần nào đang là giải pháp, giả định và dữ kiện.
2. **AI phỏng vấn ngược:** AI đặt câu hỏi về người dùng, bối cảnh, tần suất, hậu quả và giới hạn; học viên trả lời hoặc đánh dấu chưa biết.
3. **Tạo các cách hiểu cạnh tranh:** yêu cầu AI trình bày phiên bản mạnh nhất của ít nhất hai cách đóng khung vấn đề và nêu bằng chứng có thể chứng thực hoặc chứng ngụy chúng.
4. **Chốt phạm vi:** học viên tự chọn người dùng chính, thay đổi mong muốn, mục tiêu loại trừ và tiêu chí thành công sơ bộ.
5. **Kiểm tra độ rõ:** một người khác hoặc một phiên AI mới phải tóm tắt đúng vấn đề mà không tự thêm tính năng.
6. **Ghi quyết định:** lưu bản định hướng, hướng bị loại, lý do và phần còn chưa biết.

## Mục tiêu và tiêu chí đạt

Học viên đạt mục tiêu khi có thể trình bày bằng ngôn ngữ thường:

- Ai đang gặp vấn đề, trong hoàn cảnh nào;
- Điều gì hiện chưa ổn và tác động của nó;
- Kết quả mong muốn, không đồng nhất kết quả với một tính năng cụ thể;
- Phạm vi đầu tiên và ít nhất một mục tiêu loại trừ;
- Giả định quan trọng cần kiểm tra;
- Hướng đã chọn, hướng đã loại và lý do do học viên tự quyết định.

## Vai trò của AI

- Đóng vai người phỏng vấn, người phản biện và người tóm tắt.
- Đề xuất cách diễn đạt hoặc cách đóng khung cạnh tranh, không tự quyết định vấn đề thay học viên.
- Chỉ ra chỗ mơ hồ, nhảy thẳng sang giải pháp hoặc thiếu bằng chứng.
- Kiểm tra lại bản định hướng bằng cách diễn giải nó như một người chưa biết dự án.

## Quyền quyết định của học viên

Học viên phải tự chốt người dùng, vấn đề, phạm vi, mục tiêu loại trừ, dấu hiệu thành công và việc chấp nhận/từ chối đề xuất của AI. Một bản định hướng do AI tạo nhưng học viên không giải thích được không đạt yêu cầu.

## Điểm chạm với mã nguồn

Không yêu cầu viết hay đọc mã nguồn. Nếu học viên đã có nguyên mẫu, chỉ dùng nó như dữ kiện để hỏi “sản phẩm đang giả định điều gì”, không sửa phần triển khai trong G01.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** `product-brief` theo mẫu dùng chung.
- **Sản phẩm trung gian phụ:** một mục ghi trong nhật ký quyết định ghi lựa chọn, phương án bị loại và phần chưa chắc chắn.
- **Bằng chứng:** bản định hướng có tình huống cụ thể, mục tiêu loại trừ, giả định có thể kiểm tra và ít nhất một quyết định không giao cho AI.
- **Cách kiểm tra:** người kiểm định có thể phân biệt rõ vấn đề, kết quả mong muốn và giải pháp đang để ngỏ.

## Quy tắc an toàn áp dụng

- Không đưa dữ liệu cá nhân, bí mật kinh doanh hoặc nội dung nhạy cảm thật vào cuộc trò chuyện; dùng dữ liệu giả hoặc đã ẩn danh.
- Không để AI khẳng định nhu cầu thị trường hoặc hành vi người dùng khi chưa có bằng chứng.
- Không thực hiện hành động bên ngoài như gửi khảo sát hoặc liên hệ người thật nếu chưa được phê duyệt.

## Tài nguyên chuẩn phải dùng

- [Bản định hướng sản phẩm](../../shared/templates/product-brief.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Trò chuyện với AI](../../shared/practices/ai-conversation.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)

## Đường xử lý lỗi bắt buộc

Tác nhân AI triển khai phải có hoạt động xử lý ít nhất ba lỗi: AI nhảy sang tính năng, phạm vi quá rộng và chân dung người dùng do AI bịa. Học viên phải phát hiện lỗi, sửa bản định hướng và ghi lý do.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`; dùng `$learner-artifact-design` để hoàn thiện bản định hướng sản phẩm nếu mẫu chung còn sơ sài.
2. Viết một ví dụ yếu và một ví dụ đạt, nhưng không biến ví dụ thành đáp án mẫu để sao chép.
3. Tạo lời nhắc gợi mở theo nhiều lượt, không cung cấp “siêu lời nhắc” sinh trọn bản định hướng.
4. Tạo hoạt động cho học viên, dấu hiệu để giảng viên can thiệp và danh sách kiểm định bám đúng bằng chứng trên.
5. Giữ thuật ngữ kỹ thuật ở mức tối thiểu và không giới thiệu IDE ở đây.
6. Khi phải thêm khẳng định thực tế hoặc phương pháp có tính tranh luận, dùng `$curriculum-reference-research`.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Có đường học tối thiểu cho người chỉ quen web chat và phần mở rộng cho khóa đầy đủ.
- Có hoạt động học viên tự ra quyết định, phản biện AI và sửa một lỗi có chủ đích.
- Sản phẩm trung gian nối trực tiếp sang G02.
- Có `review.md` chạy đủ các cổng chất lượng; trước dạy thử không chấm tối đa cho `Beginner clarity` hoặc `Time feasibility`.
