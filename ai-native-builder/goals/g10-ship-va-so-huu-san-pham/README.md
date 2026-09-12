# G10 — Phát hành và sở hữu sản phẩm

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G10. Phát hành là một quyết định chịu trách nhiệm dựa trên bằng chứng, an toàn và khả năng vận hành và hoàn tác; không chỉ là bấm nút triển khai.

## Đặc tả học phần

- **Vấn đề người học:** nguyên mẫu có thể chạy cục bộ nhưng chưa chắc an toàn, dễ dùng, tái lập hoặc sẵn sàng cho người khác; AI thường thúc đẩy triển khai mà không làm rõ quyền sở hữu.
- **Kết quả quan sát được:** học viên thực hiện kiểm định phát hành, sửa lỗi chặn, triển khai một phiên bản phù hợp, viết `README.md` trung thực và chứng minh biết vận hành, quan sát, hoàn tác hoặc gỡ sản phẩm.
- **Điều kiện tiên quyết:** đặc tả và sơ đồ hệ thống, bằng chứng kiểm chứng, ranh giới tích hợp nếu có và bộ khung kiểm soát đã đủ ổn định từ G01–G09.
- **Đầu vào:** bản ứng viên phát hành, tiêu chí nghiệm thu, hồ sơ kiểm chứng, ghi chú về rủi ro, quyền hạn và chi phí và nhật ký quyết định.
- **Đầu ra cho G11:** ứng viên dự án tổng kết đã triển khai hoặc sản phẩm trung gian phát hành cùng README, giới hạn đã biết và bằng chứng quyền sở hữu.
- **Thời lượng thiết kế ban đầu:** 90–180 phút ngoài thời gian nền tảng dựng và triển khai; phải có phương án dự phòng trình diễn nếu dịch vụ ngoài lỗi. Cần dạy thử.

## Phạm vi nội dung

### Phải có

1. Định nghĩa đối tượng tiếp cận và ranh giới phát hành: nội bộ, bản xem trước riêng tư hay công khai.
2. Cổng phát hành dựa trên tiêu chí nghiệm thu, rủi ro nghiêm trọng và bằng chứng còn thiếu.
3. Kiểm tra quá trình dựng và chạy, biến môi trường, thông tin bí mật và ranh giới máy khách–máy chủ và dữ liệu mẫu.
4. Quyền riêng tư, quyền hạn, bản quyền, giấy phép và điều khoản của dịch vụ bên ngoài ở mức phù hợp dự án.
5. Triển khai có bản xem trước, nhận thức về chi phí, cấu hình tên miền, quyền truy cập và kiểm tra nhanh.
6. Quan sát nhật ký và lỗi tối thiểu, kỳ vọng hỗ trợ, bảo trì và đường hoàn tác hoặc gỡ công bố.
7. README gồm mục đích, cách dùng, tổng quan kiến trúc, thiết lập, kiểm chứng, giới hạn và bên chịu trách nhiệm.
8. Quyết định phát hành hoặc không phát hành có căn cứ; cho phép không phát hành khi lỗi chặn chưa xử lý.

### Chưa thuộc học phần này

- DevOps/SRE chuyên sâu, mở rộng ở môi trường vận hành thật hoặc chứng nhận bảo mật.
- Đánh bóng hồ sơ năng lực hoặc câu chuyện trình bày; đó là G11.
- Hứa thời gian hoạt động, quyền riêng tư hoặc bảo mật vượt quá bằng chứng.
- Buộc mọi dự án phải công khai nếu trình diễn riêng tư phù hợp hơn.

## Mạch học đề xuất

1. **Xác định phạm vi phát hành:** ai sẽ truy cập, dữ liệu gì dùng, mức công khai và hậu quả nếu lỗi.
2. **Kiểm định phát hành:** chạy danh sách kiểm tra nghiệm thu, thông tin bí mật, quyền riêng tư, quyền hạn, quan hệ phụ thuộc, chi phí và giới hạn đã biết.
3. **Sửa hoặc hoãn:** phân loại lỗi chặn, bắt buộc sửa, nên sửa hoặc có thể chờ; học viên chốt phạm vi phát hành.
4. **Chạy thử:** xây dựng và triển khai vào môi trường xem trước hoặc thử nghiệm; quan sát cấu hình, nhật ký và lỗi môi trường.
5. **Phát hành:** phê duyệt hành động bên ngoài, triển khai phạm vi đã chọn và chạy kiểm tra nhanh.
6. **Diễn tập phục hồi:** hoàn tác hoặc gỡ công bố hoặc chứng minh các bước có thể thực hiện.
7. **Hồ sơ quyền sở hữu:** hoàn thiện README, ranh giới hỗ trợ, giới hạn và quyết định phát hành.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Phân biệt nguyên mẫu chạy được với phát hành đủ điều kiện;
- Đưa ra quyết định phát hành hoặc không phát hành dựa trên bằng chứng và rủi ro;
- Không để thông tin bí mật hoặc dữ liệu thật trong máy khách, kho dự án hoặc nhật ký;
- Triển khai và kiểm tra nhanh đúng môi trường hoặc dùng phương án dự phòng đã công bố;
- Giải thích cách quan sát lỗi, giới hạn chi phí và hoàn tác hoặc gỡ công bố;
- `README.md` cho phép người khác hiểu mục đích, sử dụng và giới hạn mà không phóng đại.

## Vai trò của AI

- Tạo danh sách kiểm tra phát hành, rà cấu hình và phần thay đổi, hỗ trợ dựng và triển khai và soạn bản nháp `README.md`.
- Đề xuất rủi ro, kiểm tra nhanh và các bước phục hồi.
- Giải thích lỗi môi trường hoặc nhật ký và phương án khắc phục.
- Không tự phê duyệt công bố, chi tiền hoặc tuyên bố sản phẩm an toàn/sẵn sàng.

## Quyền quyết định của học viên

Học viên chốt đối tượng tiếp cận, dữ liệu, phạm vi phát hành, lỗi chặn nào phải sửa, nền tảng và chi phí, thời điểm công bố, phán quyết sau kiểm tra nhanh và trách nhiệm bảo trì hoặc gỡ bỏ.

## Điểm chạm với mã nguồn

- Đọc dựng và triển khai config, ánh xạ biến môi trường và phần mã nguồn tiếp cận thông tin bí mật hoặc dịch vụ bên ngoài.
- Quan sát nhật ký dựng sản phẩm và lỗi khi chạy, truy vết về tệp liên quan và duyệt phần thay đổi sửa lỗi.
- Chạy kiểm tra nhanh, kiểm tra mạng hoặc bảng điều khiển ở mức cần thiết.
- Thực hiện hoàn tác có hướng dẫn và giải thích tác động.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** bộ tài liệu phát hành gồm bản triển khai hoặc xem trước riêng tư phù hợp và `README.md` của dự án.
- **Sản phẩm trung gian phụ:** danh sách kiểm tra phát hành, nhật ký đã loại dữ liệu nhạy cảm và hồ sơ kiểm tra nhanh, giới hạn đã biết và hồ sơ hoàn tác hoặc gỡ công bố.
- **Bằng chứng:** mọi lỗi chặn được xử lý hoặc quyết định không phát hành; triển khai đáp ứng phạm vi đã công bố; đường phục hồi được kiểm tra.
- **Cách kiểm tra:** Người kiểm định truy cập theo README, chạy kiểm tra nhanh và hỏi học viên xử lý một tình huống lỗi, chi phí hoặc quyền riêng tư.

## Quy tắc an toàn áp dụng

- Công bố, triển khai hoặc chi tiền là hành động bên ngoài cần xem trước và phê duyệt rõ.
- Dùng thông tin bí mật trong biến môi trường đúng ranh giới; rà kho dự án/sản phẩm trung gian trước phát hành.
- Không công khai dữ liệu cá nhân, tài nguyên có bản quyền không rõ quyền hoặc điểm cuối không được bảo vệ.
- Đặt ranh giới về chi phí, hạn mức và quyền truy cập; có hoàn tác hoặc gỡ công bố, đầu mối liên hệ và quyền sở hữu rõ.

## Tài nguyên chuẩn phải dùng

- [`README.md` của dự án](../../shared/templates/project-readme.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)

## Đường xử lý lỗi bắt buộc

Phải có ít nhất một lỗi phát hành thực hoặc mô phỏng: thông tin bí mật hoặc cấu hình sai, xây dựng chỉ chạy cục bộ, quan hệ phụ thuộc bên ngoài lỗi hoặc kiểm tra nhanh không đạt. Học viên phải quyết định sửa, hoãn hoặc không phát hành rồi chứng minh phục hồi.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$assessment-design` và `$curriculum-reference-research` cho nền tảng triển khai, giá, quyền riêng tư và quyền hạn và hướng dẫn hiện hành.
2. Chuẩn bị đường triển khai gói miễn phí mặc định, lựa chọn xem trước hoặc riêng tư và phương án dự phòng trình diễn không phụ thuộc dịch vụ.
3. Tạo danh sách kiểm tra phát hành theo rủi ro, không tạo danh sách kiểm tra hình thức quá dài.
4. Có quy trình xử lý cho giảng viên cho lỗi khi dựng sản phẩm, thiếu biến môi trường, hạn mức và hoàn tác.
5. Dùng mẫu `README.md` của dự án chuẩn; không sao chép chính sách dài vào bài học.
6. Đánh giá quyền sở hữu và bằng chứng, không đánh giá việc triển khai trông hào nhoáng.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên thực hiện quyết định phát hành, kiểm tra nhanh và phục hồi, không chỉ xem triển khai trình diễn.
- Có ranh giới về thông tin bí mật, quyền riêng tư, chi phí và quyền hạn và `README.md` trung thực.
- Phát hành sản phẩm trung gian đủ đầu vào cho G11 hoặc ghi rõ lý do không phát hành hợp lệ.
- Thông tin riêng cho công cụ có nguồn/ngày kiểm tra và bài học có kiểm định chất lượng.
