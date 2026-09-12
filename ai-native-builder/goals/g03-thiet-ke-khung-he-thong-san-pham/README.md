# G03 — Thiết kế khung hệ thống sản phẩm

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho học phần G03. Đây là bước phân tích hệ thống bằng ngôn ngữ thường giữa đặc tả và bộ khung kiểm soát, không phải bài kiến trúc phần mềm hàn lâm.

## Đặc tả học phần

- **Vấn đề người học:** có đặc tả nhưng chưa biết sản phẩm gồm những phần nào, thông tin đi đâu và nên giao cho tác nhân AI lát cắt nào trước.
- **Kết quả quan sát được:** học viên tạo và giải thích được sơ đồ hệ thống gồm thành phần, trách nhiệm, luồng dữ liệu/trạng thái, quan hệ phụ thuộc, ranh giới tin cậy, rủi ro, phần chưa làm và lát cắt xây dựng nhỏ nhất.
- **Điều kiện tiên quyết:** bản đặc tả sản phẩm G02 có luồng thao tác người dùng và tiêu chí nghiệm thu tối thiểu.
- **Đầu vào:** bản định hướng, đặc tả và nhật ký quyết định.
- **Đầu ra cho G04:** sơ đồ hệ thống cùng lát cắt xây dựng đầu tiên để tổ chức không gian làm việc, chỉ dẫn và vòng lặp thực thi.
- **Thời lượng thiết kế ban đầu:** lõi 60–75 phút; bản đầy đủ có thể thêm kiểm định rủi ro và ánh xạ vào cây tệp. Cần dạy thử.

## Phạm vi nội dung

### Phải có

1. Nhìn hệ thống như các trách nhiệm hợp tác để thực hiện luồng thao tác người dùng.
2. Xác định tối thiểu phần giao diện/tương tác, logic, dữ liệu/trạng thái và dịch vụ bên ngoài nếu có.
3. Mô tả đầu vào, đầu ra và trách nhiệm của từng thành phần bằng ngôn ngữ thường.
4. Theo dấu một hành động của người dùng qua các thành phần và trạng thái thay đổi.
5. Xác định quan hệ phụ thuộc, nguồn chuẩn có thẩm quyền, ranh giới tin cậy và chỗ chứa dữ liệu nhạy cảm.
6. Ghi rủi ro, điều chưa biết và phần chủ động chưa xây.
7. Chọn lát cắt dọc nhỏ nhất có thể xây dựng và kiểm chứng end-to-end.

### Chưa thuộc học phần này

- Dạy design mẫu hình, cloud kiến trúc hoặc microservices như kiến thức bắt buộc.
- Chốt khung công nghệ hoặc cơ sở dữ liệu chỉ vì AI đề xuất.
- Tạo cấu trúc kho dự án, quy tắc hoặc quy trình thực thi; đó là G04.
- Viết phần triển khai chi tiết cho mọi thành phần.

## Mạch học đề xuất

1. **Đi từ luồng thao tác người dùng:** chọn một luồng trong đặc tả và liệt kê những trách nhiệm cần tồn tại để luồng hoàn thành.
2. **Nhóm trách nhiệm thành thành phần:** đặt tên theo chức năng, không theo buzzword công nghệ.
3. **Vẽ luồng:** theo dấu dữ liệu/trạng thái từ đầu vào tới đầu ra và chỉ ra nguồn chuẩn có thẩm quyền.
4. **AI tạo phương án cạnh tranh:** so sánh một bản đồ tối giản với một bản đồ phức tạp hơn; học viên chọn dựa trên ràng buộc.
5. **Kiểm định rủi ro và độ tin cậy:** đánh dấu quan hệ phụ thuộc bên ngoài, thông tin bí mật, dữ liệu nhạy cảm, điểm có thể lỗi và điều chưa biết.
6. **Chọn lát cắt dọc:** khoanh phần nhỏ nhất vẫn đi qua đủ lớp để chứng minh một tiêu chí nghiệm thu.
7. **Giải thích lại:** học viên giải thích bản đồ mà không dựa vào thuật ngữ AI sinh ra.

## Mục tiêu và tiêu chí đạt

Sơ đồ hệ thống đạt khi:

- Mỗi thành phần có trách nhiệm rõ và không trùng mơ hồ;
- Một hành động của người dùng có thể được lần theo xuyên suốt hệ thống;
- Dữ liệu/trạng thái quan trọng có nơi sở hữu rõ;
- External quan hệ phụ thuộc, ranh giới tin cậy, rủi ro và unknown được thể hiện;
- Lát cắt dọc liên kết trực tiếp với một tiêu chí nghiệm thu;
- Học viên giải thích được ít nhất một sự đánh đổi kiến trúc bằng ngôn ngữ thường.

## Vai trò của AI

- Hỏi để phát hiện trách nhiệm hoặc luồng còn thiếu.
- Đề xuất nhiều cách chia thành phần và nêu sự đánh đổi của từng cách.
- Đóng vai lỗi Người kiểm định, theo dấu dữ liệu và tìm quan hệ phụ thuộc ẩn.
- Chuyển bản đồ thành mô tả có cấu trúc sau khi học viên đã chốt ranh giới.

## Quyền quyết định của học viên

Học viên chốt thành phần ranh giới, nguồn chuẩn có thẩm quyền, quan hệ phụ thuộc được chấp nhận, rủi ro cần xử lý, phần không làm và lát cắt dọc. Không chấp nhận sơ đồ mà học viên không thể giải thích.

## Điểm chạm với mã nguồn

- Không yêu cầu tự viết phần triển khai.
- Có thể quan sát một cây tệp mẫu hoặc nguyên mẫu hiện có và gắn tệp/thư mục vào trách nhiệm trên bản đồ.
- Học viên cần nhận diện điểm bắt đầu, nơi giữ trạng thái và điểm nối dịch vụ bên ngoài ở mức khái niệm; không biến hoạt động thành bài cú pháp.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** sơ đồ hệ thống theo mẫu dùng chung.
- **Sản phẩm trung gian phụ:** ghi chú về lát cắt dọc và mục trong nhật ký quyết định cho một sự đánh đổi quan trọng.
- **Bằng chứng:** bản đồ theo dấu được một luồng, chỉ rõ ranh giới và rủi ro và giải thích vì sao lát cắt đã chọn là nhỏ nhất nhưng còn có giá trị.
- **Cách kiểm tra:** Người kiểm định đưa ra một lỗi hoặc thay đổi requirement; học viên chỉ được thành phần bị ảnh hưởng và giải thích lý do.

## Quy tắc an toàn áp dụng

- Không đưa thông tin bí mật hoặc dữ liệu thật vào sơ đồ; chỉ mô tả loại dữ liệu và ranh giới.
- Phân biệt dữ liệu có thể ở phía máy khách, dữ liệu phải giữ phía máy chủ và dịch vụ bên ngoài chưa được tin cậy.
- Không cho AI tự mặc định quyền truy cập, chi phí hoặc độ tin cậy của quan hệ phụ thuộc.

## Tài nguyên chuẩn phải dùng

- [Đặc tả sản phẩm](../../shared/templates/product-spec.md)
- [Sơ đồ hệ thống](../../shared/templates/system-map.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)

## Đường xử lý lỗi bắt buộc

Phải có hoạt động sửa một sơ đồ hệ thống “trông chuyên nghiệp” nhưng không lần được luồng thao tác người dùng, quá nhiều thành phần hoặc che giấu nơi giữ trạng thái/thông tin bí mật. Học viên cắt giảm và ghi sự đánh đổi.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring` và `$learner-artifact-design` để hoàn thiện mẫu sơ đồ hệ thống.
2. Tạo ít nhất một sơ đồ bằng text/Mermaid hoặc bảng trách nhiệm; không yêu cầu công cụ vẽ chuyên dụng.
3. Dùng cùng tình huống từ G02 để thể hiện quan hệ phụ thuộc thực, không tạo tình huống kỹ thuật tách rời.
4. Cung cấp vocabulary tối thiểu: thành phần, trách nhiệm, trạng thái, quan hệ phụ thuộc, ranh giới, lát cắt dọc.
5. Tạo giảng viên yêu cầu cho AI giúp học viên giản lược bản đồ, không khoe kiến trúc phức tạp.
6. Nếu đề cập kiến trúc/công cụ hiện hành, xác minh bằng `$curriculum-reference-research`.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên tạo, phản biện và giải thích sơ đồ hệ thống của chính dự án.
- Có điểm chạm mã nguồn vừa đủ để nối bản đồ với kho dự án tương lai.
- Có lỗi hoạt động, an toàn kiểm định và bằng chứng rõ.
- Lát cắt dọc trở thành đầu vào trực tiếp cho G04; bài học có kiểm định chất lượng riêng.
