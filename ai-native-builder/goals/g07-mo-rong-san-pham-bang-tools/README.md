# G07 — Mở rộng sản phẩm bằng công cụ

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G07. công cụ, API hoặc MCP chỉ được đưa vào khi giải quyết một nhu cầu sản phẩm cụ thể và có ranh giới, quyền hạn, chi phí cùng cách kiểm chứng rõ.

## Đặc tả học phần

- **Vấn đề người học:** dễ kết nối công cụ vì mới lạ, dán thông tin bí mật vào lời nhắc hoặc mã nguồn hoặc trao quyền rộng mà chưa hiểu dữ liệu và tác động phụ.
- **Kết quả quan sát được:** học viên lập kế hoạch và triển khai một tích hợp trong môi trường thử nghiệm tối thiểu với quyền hạn phù hợp, thông tin bí mật được bảo vệ, hành động nhạy cảm có phê duyệt, chi phí và giới hạn tần suất được nhận diện và hành vi được kiểm chứng.
- **Điều kiện tiên quyết:** đặc tả, sơ đồ hệ thống, bộ khung kiểm soát, vòng lặp điều khiển tác nhân và hồ sơ kiểm chứng từ G02–G06.
- **Đầu vào:** một nhu cầu người dùng chưa thể đáp ứng bằng chức năng nội bộ và tiêu chí nghiệm thu liên quan.
- **Đầu ra cho G09/G10:** ranh giới tích hợp, ma trận quyền hạn, phần triển khai và bằng chứng đủ để đưa vào bộ khung kiểm soát nâng cao và kiểm định phát hành.
- **Thời lượng thiết kế ban đầu:** 90–180 phút tùy thiết lập; nên có mô phỏng hoặc phương án dự phòng để giữ kết quả khi dịch vụ ngoài lỗi. Phải dạy thử.

## Phạm vi nội dung

### Phải có

1. Quyết định có thực sự cần công cụ bên ngoài, API hoặc MCP hay không.
2. Khái niệm vừa đủ về yêu cầu và phản hồi, xác thực, lệnh gọi công cụ và tác động phụ bên ngoài.
3. Vẽ luồng dữ liệu và ranh giới tin cậy của phần tích hợp trên sơ đồ hệ thống.
4. Quản lý thông tin bí mật qua biến môi trường hoặc phía máy chủ ranh giới phù hợp; không để khóa ở phía máy khách, kho dự án hoặc cuộc trò chuyện.
5. Quyền hạn tối thiểu, phân loại đọc, ghi, công bố, xóa và chi tiền; đồng thời yêu cầu phê duyệt trước hành động nhạy cảm.
6. Chi phí, hạn mức, giới hạn tần suất, thời gian chờ và lỗi; có phương án dự phòng/mô phỏng.
7. Kiểm chứng hành vi thành công và lỗi; nhật ký không làm lộ dữ liệu.

### Chưa thuộc học phần này

- Giới thiệu hàng loạt API hoặc MCP hoặc so sánh mọi nền tảng.
- OAuth hoặc kiến trúc bảo mật chuyên sâu nếu dự án không cần.
- Triển khai và giám sát ở môi trường vận hành thật hoàn chỉnh; đó là G10.
- Xây kỹ năng/quy trình tái sử dụng; đó là G09.

## Mạch học đề xuất

1. **Cổng xác định nhu cầu:** bắt đầu từ luồng thao tác người dùng/tiêu chí và chứng minh việc tích hợp là cần thiết.
2. **Đặc tả:** mô tả đầu vào, đầu ra, lỗi, bên chịu trách nhiệm về dữ liệu và hành động có tác động phụ.
3. **Kiểm tra rủi ro và quyền hạn:** đánh dấu thông tin bí mật, dữ liệu gửi ra ngoài, phạm vi quyền, phê duyệt và chi phí.
4. **Mô phỏng trước:** kiểm tra luồng bằng dữ liệu giả hoặc stub trước khi dùng thông tin xác thực thật.
5. **Triển khai bằng tác nhân AI:** giao một tác vụ có ranh giới rõ; học viên duyệt tệp, quyền và quan hệ phụ thuộc tác nhân AI định thêm.
6. **Kiểm chứng:** chạy các tình huống thành công, đầu vào không hợp lệ và dịch vụ gặp lỗi; quan sát dấu hiệu trong nhật ký, chi phí và hạn mức.
7. **Hồ sơ:** cập nhật sơ đồ hệ thống, kế hoạch tích hợp, ma trận quyền hạn và giới hạn.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Giải thích được phần tích hợp phục vụ tiêu chí nào;
- Chỉ được dữ liệu rời hệ thống, nơi giữ thông tin bí mật và ai có quyền hành động;
- Phân biệt hành động chỉ đọc với hành động thay đổi trạng thái;
- Thiết kế phê duyệt cho hành động có tác động đáng kể;
- Chứng minh thành công và ít nhất một tình huống lỗi hoặc sử dụng phương án dự phòng;
- Nêu chi phí, hạn mức và giới hạn chưa kiểm chứng.

## Vai trò của AI

- Tìm và giải thích tài liệu chính thức, đề xuất kế hoạch tích hợp và trường hợp lỗi.
- Hỗ trợ nền mã nguồn hoặc cấu hình trong ranh giới đã duyệt.
- Hỗ trợ phân tích quyền hạn, nhật ký và lỗi.
- Chủ động nêu giả định nhưng không tự cấp thông tin xác thực hoặc tự phê duyệt hành động bên ngoài.

## Quyền quyết định của học viên

Học viên chọn công cụ dựa trên nhu cầu, dữ liệu được phép gửi, quyền hạn phạm vi, mức chi phí chấp nhận, hành động cần phê duyệt, phương án dự phòng và quyết định có tiếp tục tích hợp hay không.

## Điểm chạm với mã nguồn

- Nhận diện phần giao diện và phía máy chủ ranh giới, tệp cấu hình và biến môi trường.
- Đọc đoạn gọi dịch vụ ở mức đầu vào, đầu ra và lỗi, không yêu cầu tự nhớ SDK.
- Xem quan hệ phụ thuộc hoặc phần thay đổi tác nhân AI thêm, chạy lệnh gọi trong môi trường thử nghiệm và đọc nhật ký đã làm sạch.
- Sửa cấu hình hoặc cách xử lý nhỏ với AI hỗ trợ rồi kiểm thử lại.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** kế hoạch tích hợp + ma trận quyền hạn + tích hợp trong môi trường thử nghiệm.
- **Sản phẩm trung gian phụ:** bản cập nhật luồng dữ liệu, ghi chú về chi phí và hạn mức, hồ sơ kiểm chứng đã loại dữ liệu nhạy cảm và phương án dự phòng.
- **Bằng chứng:** thông tin bí mật không nằm trong kho dự án hoặc phía máy khách; quyền hạn tối thiểu; hành động nhạy cảm có phê duyệt; kiểm thử thành công và lỗi có kết quả.
- **Cách kiểm tra:** Người kiểm định vô hiệu hóa thông tin xác thực hoặc dịch vụ hoặc từ chối phê duyệt và quan sát hệ thống gặp lỗi an toàn.

## Quy tắc an toàn áp dụng

- Dùng kiểm thử tài khoản thử nghiệm, gói miễn phí hoặc dữ liệu giả; không yêu cầu thông tin xác thực cá nhân trong tài liệu nộp.
- Không ghi mã truy cập vào nhật ký, nội dung nhạy cảm hoặc toàn bộ dữ liệu gửi đi nếu không cần.
- Thao tác ghi bên ngoài, công bố, xóa hoặc chi tiền phải được xem trước và có phê duyệt rõ.
- Có điều kiện dừng, trần hạn mức hoặc chi phí và cách thu hồi thông tin xác thực.

## Tài nguyên chuẩn phải dùng

- [Sơ đồ hệ thống](../../shared/templates/system-map.md)
- [Kế hoạch cho tác nhân AI](../../shared/templates/agent-plan.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)

## Đường xử lý lỗi bắt buộc

Phải có tình huống thông tin bí mật bị đặt sai ranh giới, quyền hạn rộng quá mức hoặc dịch vụ bên ngoài hết thời gian chờ hoặc vượt giới hạn tần suất. Học viên phát hiện bằng sơ đồ hoặc nhật ký, thu hẹp quyền hoặc chuyển phương án dự phòng rồi kiểm tra lại.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$learner-artifact-design` cho kế hoạch tích hợp và `$assessment-design` cho khả năng phán đoán về quyền hạn và bằng chứng.
2. Chọn một phần tích hợp phục vụ tình huống học tập; luôn cung cấp mô phỏng hoặc phương án dự phòng không cần trả phí.
3. Tách nguyên lý chung khỏi hướng dẫn Codex/MCP/API cụ thể.
4. Bắt buộc dùng `$curriculum-reference-research` cho tài liệu chính thức, giá, quyền hạn và phiên bản; ghi liên kết và ngày kiểm tra gần hướng dẫn.
5. Chuẩn bị tệp khởi đầu không chứa thông tin bí mật, nhật ký đã loại dữ liệu nhạy cảm, các bước đặt lại hoặc thu hồi và ghi chú thiết lập cho giảng viên.
6. Không đưa thông tin xác thực vào kho dự án hoặc tạo hành động bên ngoài thật trong tài liệu mẫu.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Việc tích hợp bắt đầu từ nhu cầu và có ranh giới về dữ liệu, quyền hạn và chi phí.
- Học viên ra ít nhất một quyết định hạn chế quyền hoặc tác động phụ.
- Có mô phỏng, lỗi, phương án dự phòng, kiểm chứng và thu hồi và đường hoàn tác.
- Nội dung riêng cho công cụ có nguồn hiện hành và bài học có kiểm định chất lượng.
