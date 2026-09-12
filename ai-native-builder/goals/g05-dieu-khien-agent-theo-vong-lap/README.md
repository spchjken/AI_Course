# G05 — Điều khiển tác nhân AI theo vòng lặp

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G05. Trọng tâm là năng lực điều khiển công việc nhiều bước trong bộ khung kiểm soát, không phải học thuộc công thức yêu cầu cho AI.

## Đặc tả học phần

- **Vấn đề người học:** thường giao mục tiêu lớn bằng một yêu cầu cho AI, chấp nhận kế hoạch hoặc đầu ra đầu tiên rồi lặp lại mơ hồ khi kết quả sai.
- **Kết quả quan sát được:** học viên điều khiển tác nhân AI hoàn thành một thay đổi có giới hạn qua các vòng `set intent → provide context → review plan → execute small change → observe → respond → verify → record`.
- **Điều kiện tiên quyết:** bộ khung kiểm soát G04 hoạt động; có đặc tả, sơ đồ hệ thống, kế hoạch cho tác nhân AI và trạng thái gốc phục hồi được.
- **Đầu vào:** một tiêu chí nghiệm thu/lát cắt dọc và ngữ cảnh dự án đã tổ chức.
- **Đầu ra cho G06:** thay đổi sản phẩm cùng kế hoạch, dấu vết quyết định và bằng chứng sơ bộ để kiểm chứng độc lập.
- **Thời lượng thiết kế ban đầu:** lõi 75–90 phút; bản đầy đủ nên có thêm vòng sửa lỗi. Cần dạy thử.

## Phạm vi nội dung

### Phải có

1. Viết tác vụ đặc tả gồm mục tiêu, ngữ cảnh liên quan, ràng buộc, sản phẩm bàn giao, cách kiểm chứng và điều kiện dừng.
2. Chia thay đổi lớn thành lát nhỏ có quan hệ phụ thuộc và điểm kiểm tra.
3. Chọn ngữ cảnh đủ dùng thay vì đổ toàn bộ dự án vào lời nhắc.
4. Yêu cầu lập kế hoạch trước và kiểm định kế hoạch dựa trên đặc tả và sơ đồ hệ thống.
5. Cho tác nhân AI thực hiện từng phần, quan sát tệp, phần thay đổi và đầu ra trước bước tiếp theo.
6. Phản hồi bằng điểm không khớp và bằng chứng cụ thể thay cho “làm lại cho tốt”.
7. Biết dừng, thu hẹp, đổi chiến lược hoặc hoàn tác khi vòng lặp không hội tụ.

### Chưa thuộc học phần này

- Thiết kế quy tắc/kỹ năng tái sử dụng cho nhiều tác vụ; đó là G09.
- Xây phương pháp kiểm thử đầy đủ hoặc tuyên bố sản phẩm đúng; đó là G06.
- Tích hợp API/công cụ bên ngoài; đó là G07.
- Tối ưu ngữ cảnh dài hạn toàn dự án; đó là G08.

## Mạch học đề xuất

1. **So sánh tác vụ yếu và mạnh:** dự đoán rủi ro của yêu cầu cho AI mục tiêu lớn và tác vụ đặc tả có ranh giới.
2. **Truy vết từ đặc tả:** chọn một tiêu chí nghiệm thu và xác định thay đổi nhỏ nhất phục vụ nó.
3. **Lựa chọn ngữ cảnh:** học viên chọn tệp hoặc sản phẩm trung gian cần đưa cho tác nhân AI và giải thích phần cố ý loại bỏ.
4. **Kiểm định kế hoạch:** tác nhân AI lập kế hoạch; học viên kiểm tra quan hệ phụ thuộc, phạm vi, tệp dự kiến và bước kiểm chứng rồi mới duyệt.
5. **Xây dựng theo điểm kiểm tra:** thực hiện một phần, quan sát phần thay đổi, bản xem trước hoặc lỗi, ghi điểm không khớp.
6. **Phản hồi dựa trên bằng chứng:** học viên yêu cầu chỉnh bằng dẫn chứng cụ thể và so sánh kết quả mới.
7. **Dừng và ghi hồ sơ:** chấp nhận, thử lại, thu hẹp hoặc hoàn tác; cập nhật nhật ký quyết định.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi có thể:

- Biến kết quả thành tác vụ đủ nhỏ và có điều kiện dừng;
- Giải thích vì sao ngữ cảnh đã chọn là liên quan;
- Phát hiện ít nhất một vấn đề trong kế hoạch hoặc đầu ra của tác nhân AI;
- Đưa phản hồi dựa trên đặc tả, phần thay đổi, lỗi hoặc hành vi quan sát được;
- Quyết định có căn cứ giữa chấp nhận, thử lại, thu hẹp lại phạm vi và hoàn tác;
- Để lại dấu vết đủ cho người khác tiếp tục.

## Vai trò của AI

- Phân tích tác vụ, hỏi về thiếu ngữ cảnh và đề xuất kế hoạch.
- Thực thi từng thay đổi trong phạm vi đã duyệt.
- Tóm tắt tệp/phần thay đổi, nêu giả định và tự kiểm tra nhưng không tự cấp quyền nghiệm thu.
- Đề xuất cách sửa khi có bằng chứng mới.

## Quyền quyết định của học viên

Học viên sở hữu mục tiêu tác vụ, ngữ cảnh được cấp, phạm vi, kế hoạch được duyệt, thời điểm cho tác nhân AI hành động, bằng chứng được chấp nhận và quyết định dừng hoặc hoàn tác.

## Điểm chạm với mã nguồn

- Xác định tệp liên quan từ sơ đồ hệ thống hoặc tìm kiếm dự án.
- Đọc phần thay đổi theo câu hỏi: tệp nào đổi, hành vi nào đổi, ngoài phạm vi không.
- Quan sát bảng điều khiển, lỗi hoặc bản xem trước và yêu cầu AI giải thích phần mã nguồn liên quan.
- Chỉnh một giá trị hoặc đoạn nhỏ có hướng dẫn khi điều đó giúp kiểm tra hiểu biết; không thi cú pháp.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** kế hoạch cho tác nhân AI đã được học viên chỉnh và một tác vụ hoàn thành theo điểm kiểm tra.
- **Sản phẩm trung gian phụ:** tác vụ đặc tả, dấu vết quyết định, bản tóm tắt thay đổi và kết quả kiểm tra sơ bộ.
- **Bằng chứng:** có ít nhất một lần học viên phản biện/chỉnh kế hoạch hoặc đầu ra bằng bằng chứng.
- **Cách kiểm tra:** Người kiểm định hỏi tại sao từng bước/tệp cần thiết và điều gì khiến học viên accept hay hoàn tác.

## Quy tắc an toàn áp dụng

- Chỉ cấp công cụ, tệp và quyền cần cho tác vụ hiện tại.
- Xem trước hành động có tác động phụ; không cho tác nhân AI triển khai, công bố, gửi dữ liệu hoặc tạo chi phí trong bài học.
- Giữ điểm kiểm tra phục hồi trước thay đổi lớn và không dán thông tin bí mật vào ngữ cảnh.
- Dừng khi đầu ra vượt phạm vi hoặc bằng chứng không đủ, thay vì tiếp tục nhắc AI vô hạn.

## Tài nguyên chuẩn phải dùng

- [Kế hoạch cho tác nhân AI](../../shared/templates/agent-plan.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Trò chuyện với AI](../../shared/practices/ai-conversation.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)

## Đường xử lý lỗi bắt buộc

Phải có kế hoạch cho tác nhân AI nghe hợp lý nhưng vi phạm phạm vi hoặc quan hệ phụ thuộc, hoặc một đầu ra “chạy được” nhưng không đáp ứng tiêu chí. Học viên phải tìm mismatch, sửa tác vụ hoặc ngữ cảnh và quyết định thử lại hay hoàn tác.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$learner-artifact-design` cho tác vụ đặc tả/kế hoạch cho tác nhân AI và `$assessment-design` cho khả năng điều khiển vòng lặp.
2. Thiết kế một thử thách có ít nhất hai điểm kiểm tra; không dùng trình diễn một-click.
3. Chuẩn bị bản chép lời rút gọn về vòng lặp tốt và xấu để phân tích, không yêu cầu học viên lưu toàn bộ cuộc trò chuyện.
4. Tạo cho giảng viên danh sách dấu hiệu kích hoạt can thiệp cho các lỗi: tác vụ quá lớn, ngữ cảnh thừa hoặc thiếu, kế hoạch không được kiểm định và thử lại không có bằng chứng.
5. Giữ yêu cầu cho AI theo cấu trúc linh hoạt, không dạy từ ngữ thần chú hoặc phụ thuộc mô hình.
6. Xác minh thao tác tác nhân AI hoặc công cụ thay đổi theo phiên bản trước khi viết hướng dẫn.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên thực sự điều khiển ít nhất một vòng sửa, không chỉ xem giảng viên trình diễn.
- Có quyết định thuộc về học viên, điểm chạm mã nguồn, bằng chứng và đường dừng/hoàn tác.
- Đầu ra bàn giao đủ để G06 kiểm chứng nhưng chưa được tuyên bố đúng hoàn toàn.
- Bài học có kiểm định chất lượng và biến thể thời lượng phù hợp lộ trình.
