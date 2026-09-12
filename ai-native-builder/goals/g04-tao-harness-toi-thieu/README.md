# G04 — Tạo bộ khung kiểm soát tối thiểu

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G04. “bộ khung kiểm soát” ở đây là môi trường và cơ chế giúp AI làm việc nhất quán, có quan sát và có hoàn tác; không đồng nghĩa với một bộ cấu hình đồ sộ.

## Đặc tả học phần

- **Vấn đề người học:** có đặc tả và sơ đồ hệ thống nhưng vẫn giao việc trong chat rời rạc, khiến tác nhân AI thiếu bối cảnh, sửa quá rộng và không để lại dấu vết có thể kiểm tra.
- **Kết quả quan sát được:** học viên dựng được không gian làm việc/kho dự án tối thiểu với cấu trúc dễ hiểu, xương sống tri thức dự án (điểm vào, nguồn chuẩn, provenance và nhật ký quyết định), chỉ dẫn cơ bản, điểm kiểm tra và vòng lặp `plan → build → verify` cho lát cắt dọc đầu tiên.
- **Điều kiện tiên quyết:** bản đặc tả sản phẩm G02 và sơ đồ hệ thống/lát cắt dọc G03.
- **Đầu vào:** đặc tả, sơ đồ hệ thống, tiêu chí nghiệm thu của lát cắt và chính sách dùng chung.
- **Đầu ra cho G05:** một môi trường an toàn trong đó tác nhân AI có thể nhận tác vụ nhỏ, đề xuất kế hoạch và tạo thay đổi quan sát được.
- **Thời lượng thiết kế ban đầu:** lõi 75–90 phút; thiết lập có thể tách trước buổi học. Phải dạy thử trên thiết bị của đúng đối tượng.

## Phạm vi nội dung

### Phải có

1. Bộ khung kiểm soát giải quyết vấn đề gì: ngữ cảnh, phạm vi, khả năng lặp lại, khả năng quan sát và phục hồi.
2. Tạo không gian làm việc/kho dự án hoặc phương án chụp trạng thái tương đương nếu chưa dùng Git.
3. Cấu trúc dự án tối thiểu bám theo sơ đồ hệ thống và lát cắt dọc.
4. Một chỉ dẫn điểm bắt đầu nêu mục tiêu, giới hạn, cách làm việc và cách kiểm chứng.
5. Nhật ký quyết định và vị trí lưu sản phẩm trung gian/bằng chứng.
6. Xương sống tri thức tối thiểu: một điểm vào để tác nhân tìm đúng đặc tả, sơ đồ, quyết định và bằng chứng; mỗi bản tóm tắt hoặc chỉ dẫn dẫn về nguồn có thể kiểm tra.
7. Vòng lặp `plan → learner review → small build → inspect change → verify → record`.
8. Trạng thái gốc chạy được hoặc trạng thái ban đầu có thể khôi phục.

### Chưa thuộc học phần này

- Viết hệ thống quy tắc, kỹ năng hoặc quy trình nâng cao; đó là G09.
- Tối ưu lời nhắc cho tác vụ dài nhiều bước; đó là G05.
- Xây bộ kiểm thử đầy đủ; G06 phụ trách phương pháp kiểm chứng.
- Chọn khung công nghệ phức tạp hoặc tự động hóa CI/CD.

## Mạch học đề xuất

1. **Quan sát thất bại:** so sánh một lời nhắc rời rạc với tác vụ có không gian làm việc, ngữ cảnh và điều kiện dừng.
2. **Khởi tạo trạng thái gốc:** tạo kho dự án hoặc ảnh chụp trạng thái, cây tệp tối thiểu và xác nhận có thể mở/chạy trạng thái ban đầu.
3. **Đặt chỉ dẫn:** học viên chốt mục tiêu, phạm vi, nguồn chuẩn, điều tác nhân AI phải hỏi và bước kiểm chứng.
4. **Nối sản phẩm trung gian:** đưa đặc tả, sơ đồ hệ thống và nhật ký quyết định vào vị trí tác nhân AI có thể tìm thấy.
5. **Tạo kế hoạch cho tác nhân AI đầu tiên:** tác nhân AI đề xuất tác vụ nhỏ cho lát cắt dọc; học viên sửa phạm vi trước khi cho làm.
6. **Chạy thử:** thực hiện một thay đổi rất nhỏ, xem phần thay đổi hoặc tệp thay đổi, kiểm tra và ghi kết quả.
7. **Diễn tập phục hồi:** hoàn tác hoặc phục hồi snapshot để chứng minh bộ khung kiểm soát không chỉ tạo đầu ra mà còn kiểm soát rủi ro.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi một phiên tác nhân AI mới có thể:

- Tìm đúng mục tiêu, đặc tả và sơ đồ hệ thống;
- Tìm được điểm vào, nguồn chuẩn và quyết định liên quan mà không cần toàn bộ lịch sử trò chuyện;
- Nêu lại phạm vi và điều không được tự ý làm;
- Đề xuất một kế hoạch nhỏ gắn với tiêu chí nghiệm thu;
- Tạo thay đổi ở vị trí dự kiến;
- Để học viên quan sát, kiểm tra và phục hồi được thay đổi;
- Không phụ thuộc vào lịch sử trò chuyện ẩn để hiểu dự án.

## Vai trò của AI

- Đề xuất cấu trúc tối thiểu và giải thích mục đích từng phần.
- Đọc các nguồn chuẩn có thẩm quyền, tạo kế hoạch và nêu tệp dự kiến thay đổi trước khi xây dựng.
- Thực hiện thay đổi nhỏ sau khi học viên phê duyệt.
- Hỗ trợ diễn giải phần thay đổi, lỗi thiết lập và lựa chọn phục hồi.

## Quyền quyết định của học viên

Học viên chốt công cụ hoặc không gian làm việc, cấu trúc đủ dùng, chỉ dẫn, phạm vi tác nhân AI được phép sửa, kế hoạch đầu tiên, điều kiện dừng và việc chấp nhận hoặc hoàn tác thay đổi.

## Điểm chạm với mã nguồn

- Mở và định vị cây tệp, điểm bắt đầu và tệp cấu hình cơ bản.
- Chạy xem trước hoặc lệnh kiểm tra đã được chuẩn bị; quan sát đầu ra và lỗi.
- Xem danh sách tệp hoặc phần thay đổi do tác nhân AI thay đổi và mô tả tác động bằng ngôn ngữ thường.
- Thực hiện một chỉnh sửa hoặc hoàn tác có hướng dẫn; không yêu cầu nhớ cú pháp.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** không gian làm việc hoặc kho dự án với bộ khung kiểm soát tối thiểu.
- **Sản phẩm trung gian phụ:** chỉ dẫn điểm bắt đầu, nhật ký quyết định, kế hoạch cho tác nhân AI đầu tiên và ghi chú về trạng thái gốc và phục hồi.
- **Bằng chứng:** phiên tác nhân AI mới đọc đúng ngữ cảnh; thay đổi nhỏ có kế hoạch, phần thay đổi, kết quả kiểm chứng và đường hoàn tác.
- **Cách kiểm tra:** xóa ngữ cảnh hội thoại khỏi giả định, bắt đầu phiên mới và xem bộ khung kiểm soát có đủ để tiếp tục đúng phạm vi hay không.

## Quy tắc an toàn áp dụng

- Dùng dữ liệu giả; không đưa khóa truy cập, mật khẩu hoặc tệp môi trường chứa thông tin bí mật vào kho dự án.
- Xem trước phạm vi và hậu quả trước khi tác nhân AI sửa tệp hoặc chạy hành động có tác động phụ.
- Tạo nhánh, bản ghi thay đổi hoặc ảnh chụp trạng thái trước thay đổi đáng kể; hướng dẫn dừng/hoàn tác tương xứng.
- Không dùng hệ thống môi trường vận hành thật hoặc tài khoản thật trong bài.

## Tài nguyên chuẩn phải dùng

- [Sơ đồ hệ thống](../../shared/templates/system-map.md)
- [Kế hoạch cho tác nhân AI](../../shared/templates/agent-plan.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)
- [Quyền riêng tư, thông tin bí mật và quyền hạn](../../shared/policies/privacy-secrets-and-permissions.md)

## Đường xử lý lỗi bắt buộc

Phải có tình huống tác nhân AI định sửa quá nhiều tệp, bỏ qua đặc tả hoặc tạo thay đổi không chạy. Học viên dùng chỉ dẫn, kiểm định kế hoạch, phần thay đổi và hoàn tác để giới hạn và phục hồi.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`; dùng `$learner-artifact-design` cho kế hoạch cho tác nhân AI hoặc nhật ký quyết định nếu cần.
2. Chuẩn bị đường thiết lập dễ nhất và phương án dự phòng không phụ thuộc Git cho học viên chưa cài đủ công cụ.
3. Tách rõ nguyên lý bộ khung kiểm soát bền vững với thao tác cụ thể của Codex, VS Code hoặc Antigravity.
4. Mọi hướng dẫn giao diện hoặc dòng lệnh dễ lỗi thời phải được `$curriculum-reference-research` kiểm tra và ghi ngày.
5. Tạo danh sách kiểm tra thiết lập, hoạt động chạy thử, diễn tập phục hồi và giảng viên ghi chú xử lý sự cố.
6. Không biến bài học thành phần giới thiệu IDE hay danh sách cấu hình.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Người mới tạo được bộ khung kiểm soát và hoàn thành một vòng lặp nhỏ có hoàn tác.
- Sản phẩm trung gian từ G02/G03 được dùng thật, không chỉ được nhắc tên.
- Có bằng chứng phiên mới tiếp tục được công việc đúng phạm vi.
- Bài học có đường chương trình thực hành ngắn tối thiểu, đường đầy đủ và kiểm định chất lượng.
