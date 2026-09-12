# G11 — Xây và trình bày dự án tổng kết

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G11. Dự án tổng kết tổng hợp và chứng minh năng lực đã hình thành ở G01–G10; không phải một dự án mới do AI làm hộ ở cuối khóa.

## Đặc tả học phần

- **Vấn đề người học:** có nhiều sản phẩm trung gian và một sản phẩm nhưng chưa tích hợp chúng thành bằng chứng năng lực; dễ dành thời gian đánh bóng trình diễn hoặc kể câu chuyện vượt quá phần mình thực sự quyết định.
- **Kết quả quan sát được:** học viên hoàn thiện, trình bày và bảo vệ một dự án tổng kết có kho dự án, trình diễn hoặc phát hành phù hợp, README, sơ đồ hệ thống, bằng chứng kiểm chứng và dấu vết quyết định; giải thích được lựa chọn, giới hạn và một lần phục hồi từ lỗi.
- **Điều kiện tiên quyết:** sản phẩm trung gian từ G01–G10 và dự án tổng kết phạm vi đã được kiểm định trong các buổi thực hành tích hợp.
- **Đầu vào:** bản định hướng, đặc tả, bản đồ, bộ khung kiểm soát, tác nhân AI và nhật ký quyết định, hồ sơ kiểm chứng và phát hành và sản phẩm hiện tại.
- **Đầu ra chương trình:** bộ tài liệu dự án tổng kết dùng cho hồ sơ năng lực hoặc CV cùng bằng chứng phân biệt rõ đóng góp của AI và quyền sở hữu của học viên.
- **Thời lượng thiết kế ban đầu:** nhiều buổi hoặc buổi thực hành tích hợp theo lộ trình 20 buổi; G11 tập trung tích hợp, bằng chứng và trình bày, không mở tính năng lớn mới. Phải dạy thử toàn luồng.

## Phạm vi nội dung

### Phải có

1. Khóa kết quả và phạm vi dựa trên thời gian và bằng chứng còn thiếu.
2. Kiểm định chuỗi `problem → specification → system map → implementation → verification → release`.
3. Ưu tiên lỗi chặn và khoảng trống bằng chứng trước trau chuốt hoặc tính năng mới.
4. Hoàn thiện kho dự án, trình diễn hoặc triển khai phù hợp, README và mục lục sản phẩm trung gian.
5. Giải thích kiến trúc và sự đánh đổi bằng ngôn ngữ của học viên.
6. Chọn quyết định, lỗi và phục hồi tiêu biểu để chứng minh quy trình AI-native.
7. Xây câu chuyện trình diễn theo chuỗi `user problem → acceptance evidence`.
8. Chuyển năng lực thành mô tả hồ sơ năng lực hoặc CV trung thực, không gán toàn bộ đầu ra AI cho bản thân.

### Chưa thuộc học phần này

- Dạy thêm năng lực nền mới hoặc đổi kiến trúc lớn sát hạn.
- Chấm sản phẩm chủ yếu theo độ bóng giao diện hay số tính năng.
- Viết hộ câu chuyện cá nhân, phần giải thích hệ thống hoặc câu trả lời phản biện.
- Ép công khai triển khai khi quyền riêng tư, chi phí hoặc độ tin cậy không cho phép.

## Mạch học đề xuất

1. **Kiểm kê bằng chứng:** gom sản phẩm trung gian G01–G10 và đánh dấu thiếu, lỗi thời, mâu thuẫn hoặc không còn phản ánh sản phẩm.
2. **Phạm vi đã khóa:** chốt lỗi bắt buộc sửa, lỗi bằng chứng, phần trau chuốt và mục tiêu loại trừ được nêu rõ.
3. **Tích hợp:** sửa lỗi chặn theo bộ khung kiểm soát và vòng lặp điều khiển tác nhân AI, chạy lại kiểm chứng và cập nhật bản đồ/README.
4. **Câu chuyện về quyền sở hữu:** chọn ba quyết định lớn, một đề xuất AI bị sửa hoặc từ chối và một lỗi và quá trình phục hồi.
5. **Thiết kế phần trình diễn:** đi theo chuỗi `problem → user flow → evidence → limitations → next step`; chuẩn bị phương án dự phòng nếu trình diễn trực tiếp lỗi.
6. **Diễn tập bảo vệ:** Người kiểm định hỏi về phạm vi, kiến trúc, đường đi trong mã nguồn, kiểm chứng, an toàn và đóng góp của AI.
7. **Chuyển hóa thành hồ sơ năng lực:** viết mô tả ngắn về vấn đề, hành động, bằng chứng và kết quả; bạn học hoặc giảng viên kiểm tra chống phóng đại.
8. **Phán quyết cuối:** đánh giá theo bảng tiêu chí đánh giá, ghi giới hạn và kế hoạch sau khóa.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Dự án tổng kết giải quyết vấn đề và phạm vi đã chốt, không chỉ là trình diễn công nghệ;
- Sản phẩm trung gian nhất quán với sản phẩm hiện tại và truy vết được;
- Học viên tự giải thích sơ đồ hệ thống, đường đi chính trong mã nguồn và sự đánh đổi;
- Có bằng chứng kiểm chứng và phát hành cùng giới hạn của kết luận;
- Chỉ ra cụ thể AI đã làm gì và mình đã quyết định và kiểm tra gì;
- Trình diễn có phương án dự phòng và câu chuyện hồ sơ năng lực không chứa khẳng định không được hỗ trợ.

## Vai trò của AI

- Hỗ trợ kiểm định sản phẩm trung gian, tìm điểm thiếu nhất quán, lên kế hoạch sửa và diễn tập các câu hỏi khó.
- Soạn bản nháp `README.md`, dàn ý trình diễn hoặc gạch đầu dòng cho hồ sơ năng lực để học viên phản biện và viết lại.
- Hỗ trợ phần triển khai và kiểm chứng trong bộ khung kiểm soát đã có.
- Không tự tạo câu chuyện quyền sở hữu hoặc tự chấm dự án tổng kết đạt.

## Quyền quyết định của học viên

Học viên sở hữu phạm vi đã khóa, ưu tiên sửa lỗi, kiến trúc và sự đánh đổi được bảo vệ, bằng chứng được trình bày, cách mô tả đóng góp của AI, mức độ công khai khi phát hành và mọi khẳng định hồ sơ năng lực hoặc CV.

## Điểm chạm với mã nguồn

- Chỉ được điểm bắt đầu và các tệp hoặc thành phần quan trọng trên sơ đồ hệ thống.
- Giải thích một luồng từ hành động của người dùng qua mã nguồn, dữ liệu và quan hệ phụ thuộc bên ngoài ở mức phù hợp.
- Dùng lịch sử thay đổi để trình bày một quyết định hoặc phục hồi thật.
- Chẩn đoán một lỗi trình diễn có hướng dẫn và chọn phương án dự phòng; không thi viết mã nguồn từ trí nhớ.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** bộ tài liệu dự án tổng kết gồm kho dự án, trình diễn hoặc triển khai phù hợp và README.
- **Sản phẩm trung gian bằng chứng:** bản định hướng và đặc tả sản phẩm, sơ đồ hệ thống, nhật ký về các quyết định và tác nhân AI đã chọn, hồ sơ kiểm chứng và phát hành, kịch bản hoặc video trình diễn hoặc phương án dự phòng và bản tóm tắt hồ sơ năng lực.
- **Bằng chứng quyền sở hữu:** ít nhất ba quyết định thuộc về học viên, một đề xuất của AI bị sửa hoặc từ chối và một lỗi và quá trình phục hồi có bằng chứng.
- **Cách kiểm tra:** phần bảo vệ trực tiếp ngắn trong đó Người kiểm định truy vết khẳng định tới sản phẩm trung gian hoặc sản phẩm và yêu cầu học viên giải thích một sự đánh đổi.

## Khung đánh giá phải phản ánh

Giữ tỷ trọng cấp chương trình, sau đó cụ thể hóa thành tiêu chí quan sát được bằng `$assessment-design`:

- Định hướng và đặc tả và sơ đồ hệ thống: 25%;
- Điều khiển tác nhân AI và quản lý ngữ cảnh: 25%;
- Kiểm chứng, bộ khung kiểm soát và công cụ an toàn: 30%;
- Sản phẩm, triển khai và trình bày: 20%.

Không dùng tổng điểm để bù một lỗi nghiêm trọng về an toàn, kiểm chứng hoặc quyền sở hữu.

## Quy tắc an toàn áp dụng

- Rà dữ liệu nhận dạng cá nhân, thông tin bí mật, quyền sử dụng tài nguyên và mã nguồn, giấy phép và dữ liệu trước khi chia sẻ kho dự án, phần trình diễn hoặc video.
- Không công khai liên kết hoặc tài khoản nếu học viên chưa phê duyệt phạm vi.
- Nêu rõ quan hệ phụ thuộc, chi phí, độ tin cậy và giới hạn đã biết.
- Có bản trình diễn dự phòng, hoàn tác hoặc gỡ công bố và phương án ẩn sản phẩm trung gian nhạy cảm.

## Tài nguyên chuẩn phải dùng

- [Bản định hướng sản phẩm](../../shared/templates/product-brief.md)
- [Đặc tả sản phẩm](../../shared/templates/product-spec.md)
- [Sơ đồ hệ thống](../../shared/templates/system-map.md)
- [`README.md` của dự án](../../shared/templates/project-readme.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)

## Đường xử lý lỗi bắt buộc

Phải diễn tập ít nhất hai tình huống: trình diễn trực tiếp lỗi và Người kiểm định phát hiện khẳng định không có bằng chứng/mâu thuẫn sản phẩm trung gian. Học viên dùng phương án dự phòng, thu hẹp khẳng định hoặc cập nhật bằng chứng thay vì che giấu.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$assessment-design`, `$learner-artifact-design` và `$curriculum-quality-review`.
2. Tạo bản kiểm kê sản phẩm trung gian, danh sách kiểm tra khóa phạm vi, bộ câu hỏi bảo vệ, trình diễn mẫu và hồ sơ năng lực kiểm tra tính trung thực.
3. Thiết kế buổi thực hành tích hợp để kiểm định và tích hợp, không giảng lại toàn bộ G01–G10.
4. Yêu cầu học viên thực hiện giải thích lại và bảo vệ trực tiếp; không chấp nhận kịch bản AI mà học viên chỉ đọc.
5. Cung cấp nhiều hình thức trình diễn tương đương cho accessibility/độ tin cậy nhưng giữ cùng bằng chứng khẳng định.
6. Mọi thông tin nền tảng công khai, triển khai hoặc hồ sơ năng lực thay đổi theo thời gian phải được nghiên cứu và ghi nguồn.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Dự án tổng kết bộ tài liệu hoàn chỉnh, nhất quán và có mục lục bằng chứng.
- Đánh giá năng lực đo quyền sở hữu của học viên, kiểm chứng và khả năng giải thích, không chỉ độ đẹp sản phẩm.
- Có trình diễn trực tiếp hoặc bằng phương án dự phòng, phần bảo vệ, kiểm tra an toàn, công bố và hiệu chỉnh mức độ khẳng định.
- Chỉ dùng trạng thái `Validated` nếu có dạy thử đúng đối tượng theo các cổng chất lượng.
