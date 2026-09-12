# G02 — Viết đặc tả sản phẩm

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho học phần G02. Tác nhân AI triển khai phải biến bản định hướng thành trải nghiệm học tập, không mở rộng nó thành tài liệu kiến trúc hay yêu cầu xây dựng sản phẩm.

## Đặc tả học phần

- **Vấn đề người học:** bản định hướng đã nêu được ý định nhưng chưa đủ cụ thể để con người hoặc tác nhân AI biết phải tạo hành vi gì và kiểm tra thành công ra sao.
- **Kết quả quan sát được:** học viên chuyển bản định hướng sản phẩm thành một bản đặc tả sản phẩm mô tả tác nhân, luồng thao tác người dùng, trạng thái quan trọng, ràng buộc, mục tiêu loại trừ và tiêu chí nghiệm thu có thể kiểm tra.
- **Điều kiện tiên quyết:** bản định hướng sản phẩm G01 đã được chốt, gồm người dùng, vấn đề, phạm vi và giả định chính.
- **Đầu vào:** bản định hướng sản phẩm và nhật ký quyết định từ G01.
- **Đầu ra cho G03:** đặc tả đủ rõ để suy ra các thành phần, trách nhiệm và luồng dữ liệu/trạng thái.
- **Thời lượng thiết kế ban đầu:** lõi 60–75 phút; bản đầy đủ có thể thêm trường hợp biên và kiểm định chéo. Phải dạy thử để xác nhận.

## Phạm vi nội dung

### Phải có

1. Chuyển giá trị mong muốn thành các hành vi người dùng quan sát được.
2. Xác định tác nhân chính, điểm bắt đầu, luồng thành công và trạng thái kết thúc.
3. Nêu dữ liệu đầu vào/đầu ra bằng ngôn ngữ thường, chưa cần lược đồ kỹ thuật.
4. Viết tiêu chí nghiệm thu bằng ví dụ hoặc cấu trúc Given/When/Then dễ kiểm tra.
5. Thêm các trạng thái lỗi, trống hoặc đang tải cần thiết cho lát cắt đầu tiên.
6. Ghi ràng buộc, mục tiêu loại trừ và các câu hỏi chưa được quyết định.
7. Truy vết tính năng/tiêu chí về đúng vấn đề trong bản định hướng.

### Chưa thuộc học phần này

- Chia mô-đun kỹ thuật, chọn cơ sở dữ liệu, khung công nghệ hoặc nền tảng triển khai.
- Viết toàn bộ backlog cho sản phẩm hoàn chỉnh.
- Sinh mã nguồn hoặc đánh giá chất lượng phần triển khai.
- Tối ưu hiệu năng, bảo mật chuyên sâu hoặc thiết kế API chi tiết.

## Mạch học đề xuất

1. **Đọc bản định hướng bằng mắt của người thực thi:** đánh dấu mọi từ mơ hồ như “dễ dùng”, “thông minh”, “nhanh” hoặc “hoạt động tốt”.
2. **Mô tả một hành trình:** viết tác nhân → điều kiện kích hoạt → hành động → phản hồi hệ thống → kết quả.
3. **Tách lát cắt đầu tiên:** chọn luồng nhỏ nhất vẫn tạo ra giá trị, giữ phần còn lại trong mục tiêu loại trừ.
4. **Đối thoại phản biện với AI:** yêu cầu AI tìm mâu thuẫn, trường hợp thiếu và tiêu chí không thể kiểm tra.
5. **Viết tiêu chí nghiệm thu:** học viên duyệt, sửa hoặc từ chối từng đề xuất.
6. **Traceability check:** nối từng tiêu chí về nhu cầu người dùng và gắn câu hỏi chưa quyết định.

## Mục tiêu và tiêu chí đạt

Đặc tả đạt khi một người/tác nhân AI khác có thể trả lời nhất quán:

- Ai thực hiện hành vi nào và theo thứ tự nào;
- Hệ thống phản hồi gì ở mỗi bước quan trọng;
- Dữ liệu/trạng thái tối thiểu nào được tạo, thay đổi hoặc hiển thị;
- Điều kiện nào chứng minh lát cắt đã hoạt động;
- Điều gì chủ động chưa làm;
- Điểm nào vẫn là giả định hoặc câu hỏi mở.

## Vai trò của AI

- Chuyển ngôn ngữ mơ hồ thành các cách diễn đạt có thể quan sát và kiểm tra.
- Mô phỏng vai người dùng, người phát triển và Người kiểm định để tìm khoảng trống hoặc mâu thuẫn.
- Đề xuất trường hợp biên và tiêu chí nghiệm thu; học viên quyết định mức nào thuộc phạm vi.
- Kiểm tra khả năng truy vết giữa bản định hướng, luồng và tiêu chí.

## Quyền quyết định của học viên

Học viên sở hữu ưu tiên tính năng, lát cắt đầu tiên, hành vi bắt buộc, trường hợp biên thuộc phạm vi, mục tiêu loại trừ và tiêu chí được dùng để nghiệm thu. AI không được tự tăng phạm vi để làm đặc tả “đầy đủ hơn”.

## Điểm chạm với mã nguồn

Không yêu cầu viết mã nguồn. Nếu đã có nguyên mẫu, học viên có thể quan sát hành vi hiện có và đối chiếu với đặc tả; không kiểm định cú pháp hoặc kiến trúc trong G02.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** bản đặc tả sản phẩm theo mẫu dùng chung.
- **Sản phẩm trung gian phụ:** bảng truy vết ngắn `need → behavior → acceptance criterion` và mục trong nhật ký quyết định cho phạm vi.
- **Bằng chứng:** có ít nhất một luồng thành công, một lỗi/trạng thái trống phù hợp và tiêu chí có thể cho kết quả `Pass`/`Fail`.
- **Cách kiểm tra:** Người kiểm định đưa ra hai cách hiểu khác nhau; đặc tả phải giải quyết được hoặc đánh dấu rõ quyết định còn mở.

## Quy tắc an toàn áp dụng

- Dùng dữ liệu mẫu, không nhúng dữ liệu cá nhân, thông tin bí mật hoặc thông tin xác thực thật vào ví dụ.
- Đánh dấu rõ yêu cầu liên quan quyền riêng tư, quyền truy cập hoặc hành động bên ngoài để xử lý ở các mục tiêu sau.
- Không khẳng định một tiêu chí nghiệm thu bảo đảm an toàn nếu chưa có cách kiểm tra tương ứng.

## Tài nguyên chuẩn phải dùng

- [Bản định hướng sản phẩm](../../shared/templates/product-brief.md)
- [Đặc tả sản phẩm](../../shared/templates/product-spec.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Trò chuyện với AI](../../shared/practices/ai-conversation.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)

## Đường xử lý lỗi bắt buộc

Phải có tình huống AI tạo đặc tả dài nhưng không kiểm chứng được, tự thêm tính năng hoặc bỏ qua trạng thái lỗi. Học viên dùng bản định hướng và phạm vi để cắt bỏ, sửa tiêu chí và ghi quyết định.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`; phối hợp `$learner-artifact-design` cho đặc tả và `$assessment-design` cho tiêu chí đánh giá học viên.
2. Tạo hoạt động chuyển ba câu mơ hồ thành hành vi/tiêu chí quan sát được.
3. Cung cấp một đặc tả yếu, một đặc tả vừa đủ và câu hỏi kiểm định; không đưa đặc tả hoàn chỉnh để điền tên dự án.
4. Giải thích Given/When/Then như công cụ tư duy, không bắt học viên học ngôn ngữ kiểm thử.
5. Thiết kế bản chương trình thực hành ngắn chỉ giữ một luồng thao tác người dùng; phần mở rộng mới thêm trường hợp biên phức tạp.
6. Không thêm công nghệ hoặc các bước riêng cho công cụ khi chưa có nhu cầu từ mục tiêu.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên hoạt động tạo ra đặc tả chứ không chỉ nghe giải thích.
- Có ít nhất một quyết định phạm vi do học viên sở hữu và một lần phản biện đầu ra AI.
- Tiêu chí có thể được G06 dùng trực tiếp để kiểm chứng.
- Sản phẩm trung gian cung cấp đủ đầu vào cho sơ đồ hệ thống G03 và có kiểm định các cổng chất lượng.
