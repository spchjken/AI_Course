# G08 — Quản lý ngữ cảnh dự án

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G08. Quản lý và truy xuất ngữ cảnh là chọn, tổ chức, kiểm tra và làm mới thông tin đã được dự án tích lũy để tác nhân AI ra quyết định đúng; không phải bắt đầu xây toàn bộ cơ sở tri thức ở mục tiêu này hoặc nạp càng nhiều token càng tốt.

## Đặc tả học phần

- **Vấn đề người học:** sau nhiều phiên, AI quên quyết định, dùng tệp cũ hoặc bị ngập bởi ngữ cảnh không liên quan; học viên phản ứng bằng cách dán toàn bộ lịch sử hoặc toàn bộ kho dự án.
- **Kết quả quan sát được:** học viên tạo và kiểm thử gói ngữ cảnh có mục đích trên nền xương sống tri thức đã có, truy được về nguồn chuẩn có thẩm quyền, dùng tìm kiếm và nhật ký quyết định để khởi động phiên mới và chọn có căn cứ giữa tệp/chỉ mục, cơ sở tri thức được tuyển chọn, RAG hoặc chế độ xem dạng đồ thị.
- **Điều kiện tiên quyết:** bộ khung kiểm soát G04, vòng lặp G05 và bằng chứng bài thực hành G06; dự án đã có nhiều tệp và quyết định đủ để ngữ cảnh trở thành vấn đề thật.
- **Đầu vào:** kho dự án, bản định hướng, đặc tả và sơ đồ, nhật ký quyết định, hồ sơ kiểm chứng và một tác vụ mới.
- **Đầu ra cho G09:** quy ước ngữ cảnh và bằng chứng khởi động lại hoặc bàn giao để mã hóa thành quy tắc, kỹ năng hoặc quy trình phù hợp.
- **Thời lượng thiết kế ban đầu:** 90–120 phút; phần mở rộng về cơ sở tri thức/RAG chỉ dùng khi tình huống đủ phức tạp. Cần dạy thử.

## Phạm vi nội dung

### Phải có

1. Phân biệt cửa sổ ngữ cảnh, tri thức dự án, nguồn chuẩn có thẩm quyền và ngữ cảnh làm việc.
2. Bắt đầu từ tác vụ rồi tìm tệp hoặc sản phẩm trung gian liên quan bằng tìm kiếm, bản đồ và lịch sử.
3. Tạo gói ngữ cảnh tối thiểu: mục tiêu, trạng thái hiện tại, ràng buộc, nguồn liên quan, quyết định, câu hỏi chưa giải quyết và lệnh kiểm chứng.
4. Ghi nguồn gốc: mỗi bản tóm tắt hoặc quyết định trỏ về nguồn có thể kiểm tra.
5. Nén ngữ cảnh bằng bản tóm tắt có ranh giới và cập nhật hoặc loại bỏ thông tin lỗi thời.
6. Kiểm thử bàn giao bằng phiên tác nhân AI mới.
7. Ra quyết định khi nào tệp hoặc chỉ mục nhẹ đủ, khi nào mới cần cơ sở tri thức được tuyển chọn, RAG hoặc chế độ xem dạng đồ thị.

### Chưa thuộc học phần này

- Xây hệ thống RAG vận hành thật, quy trình tạo biểu diễn nhúng hoặc cơ sở dữ liệu đồ thị.
- Dạy kiến trúc LLM sâu hoặc tối ưu lượng token theo công thức cứng.
- Viết quy tắc/kỹ năng tự động hóa ngữ cảnh; đó là G09.
- Coi toàn bộ bản chép lời trò chuyện là nguồn chuẩn có thẩm quyền mặc định.

## Mạch học đề xuất

1. **Lỗi ngữ cảnh:** cho tác nhân AI trả lời bằng quyết định/tệp cũ và tìm nguyên nhân.
2. **Tìm kiếm từ tác vụ:** học viên nêu tác vụ, dự đoán nguồn cần thiết rồi dùng điểm vào, kho dự án, sơ đồ và lịch sử để kiểm tra.
3. **Đóng gói:** tạo gói ngữ cảnh ngắn, đánh dấu chuẩn nguồn, bản tóm tắt và điểm chưa chắc chắn.
4. **Kiểm định bản tóm tắt:** AI tóm tắt; học viên đối chiếu nguồn, loại chi tiết thừa và sửa điểm sai hoặc lỗi thời.
5. **Kiểm thử khởi động lại:** mở phiên mới, chỉ cung cấp gói ngữ cảnh và yêu cầu tác nhân AI trình bày lại mục tiêu, ràng buộc và kế hoạch.
6. **Quyết định chiến lược:** so sánh tệp hoặc chỉ mục nhẹ, cơ sở tri thức được tuyển chọn, RAG và đồ thị dựa trên quy mô, độ mới kiểu truy vấn, khả năng bảo trì và bằng chứng thất bại truy xuất.
7. **Quy ước lưu hồ sơ:** chốt khi nào cập nhật gói ngữ cảnh hoặc nhật ký quyết định và ai chịu trách nhiệm.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Chọn ngữ cảnh dựa trên tác vụ và giải thích được phần đưa vào hoặc loại ra;
- Mọi quyết định quan trọng truy được tới chuẩn nguồn;
- Phát hiện và sửa ít nhất một bản tóm tắt lỗi thời, thiếu hoặc mâu thuẫn;
- Phiên mới đề xuất kế hoạch nhất quán mà không cần toàn bộ lịch sử cuộc trò chuyện;
- Không chọn RAG hoặc đồ thị chỉ vì “nâng cao”, mà nêu được nhu cầu và chi phí bảo trì;
- Có quy ước làm mới ngữ cảnh khi dự án thay đổi.

## Vai trò của AI

- Hỗ trợ tìm kiếm, tóm tắt, tạo gói ngữ cảnh và phát hiện mâu thuẫn.
- Đề xuất nguồn liên quan và nêu điểm chưa chắc chắn và nguồn gốc.
- Mô phỏng bàn giao hoặc khởi động lại để kiểm thử gói ngữ cảnh.
- Không tự nâng bản tóm tắt thành nguồn chuẩn có thẩm quyền hoặc tự quyết định bỏ nguồn chuẩn.

## Quyền quyết định của học viên

Học viên chốt ranh giới tác vụ, nguồn chuẩn, ngữ cảnh được cấp, bản tóm tắt được chấp nhận, quyết định nào phải ghi lâu dài và chiến lược truy xuất phù hợp.

## Điểm chạm với mã nguồn

- Dùng cây tệp hoặc tìm kiếm để tìm điểm bắt đầu, ký hiệu, cấu hình và nơi thực hiện hành vi.
- Đọc lịch sử thay đổi để biết trạng thái hiện tại và quyết định đã thay đổi.
- Yêu cầu AI giải thích đoạn mã nguồn liên quan rồi đối chiếu với nguồn thực.
- Không cần tự viết thuật toán RAG hoặc học tìm kiếm mã nguồn như chương riêng.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** gói ngữ cảnh cho một tác vụ thật.
- **Sản phẩm trung gian phụ:** quy ước nhật ký quyết định, bản đồ nguồn và hồ sơ quyết định chiến lược.
- **Bằng chứng:** kiểm thử khởi động lại thành công, liên kết nguồn gốc đúng và một lỗi ngữ cảnh được phát hiện/sửa.
- **Cách kiểm tra:** đưa gói ngữ cảnh cho phiên mới, hỏi mục tiêu, ràng buộc, các tệp liên quan và câu hỏi chưa giải quyết và so sánh với nguồn chuẩn.

## Quy tắc an toàn áp dụng

- Gói ngữ cảnh không chứa thông tin bí mật, dữ liệu nhận dạng cá nhân hoặc dữ liệu ngoài phạm vi tác vụ.
- Không gửi toàn kho dự án hoặc dữ liệu tới dịch vụ ngoài mà chưa biết quyền hạn và chính sách lưu giữ.
- Đánh dấu ngày hoặc phiên bản cho bản tóm tắt dễ lỗi thời và bỏ quyền truy cập không cần thiết.
- Với cơ sở tri thức/RAG, nêu nguồn dữ liệu, độ mới, quyền truy cập và cách xóa hoặc cập nhật.

## Tài nguyên chuẩn phải dùng

- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Sơ đồ hệ thống](../../shared/templates/system-map.md)
- [Trò chuyện với AI](../../shared/practices/ai-conversation.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)

## Đường xử lý lỗi bắt buộc

Phải có gói ngữ cảnh quá dài nhưng thiếu ràng buộc quan trọng, hoặc bản tóm tắt mâu thuẫn với nguồn mới. Học viên dùng nguồn gốc hoặc tìm kiếm để phát hiện, sửa và chạy kiểm thử khởi động lại.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$learner-artifact-design` cho gói ngữ cảnh và `$assessment-design` cho bằng chứng lựa chọn và khởi động lại.
2. Chuẩn bị một kho dự án hoặc tình huống có tệp gần giống, quyết định cũ và ngữ cảnh gây nhiễu.
3. Tạo hoạt động bắt học viên loại ngữ cảnh, không chỉ thu thập thêm.
4. Dạy RAG hoặc đồ thị như nhánh quyết định có ngưỡng, không như bước mặc định.
5. Xác minh tính năng tìm kiếm/ngữ cảnh của công cụ hiện hành bằng `$curriculum-reference-research`.
6. Tạo hướng dẫn cho giảng viên xử lý ngữ cảnh thông tin bịa đặt, bản tóm tắt lỗi thời và ranh giới quyền riêng tư.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên tạo và kiểm thử gói ngữ cảnh trên phiên mới.
- Có nguồn gốc, độ mới, quyền riêng tư và loại bỏ ngữ cảnh thừa.
- Có quyết định có căn cứ về chiến lược truy xuất.
- Sản phẩm trung gian nối sang G09 và bài học có kiểm định chất lượng.
