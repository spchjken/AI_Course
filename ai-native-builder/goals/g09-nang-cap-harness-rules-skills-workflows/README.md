# G09 — Nâng cấp bộ khung kiểm soát: quy tắc, kỹ năng, quy trình

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G09. Học viên chỉ mã hóa một hành vi thành quy tắc, kỹ năng hoặc quy trình sau khi có bằng chứng lặp lại từ dự án; không tạo “hệ thống tác nhân AI” phức tạp để trang trí.

## Đặc tả học phần

- **Vấn đề người học:** bộ khung kiểm soát tối thiểu giúp bắt đầu nhưng lỗi và hướng dẫn lặp lại chưa được chuyển thành cơ chế tái sử dụng; ngược lại, người học có thể tạo quá nhiều quy tắc mơ hồ hoặc chồng chéo.
- **Kết quả quan sát được:** từ bằng chứng của dự án, học viên chọn đúng cơ chế quy tắc, kỹ năng hoặc quy trình; triển khai một nâng cấp tối thiểu (có thể là quy ước metadata, chỉ mục hoặc truy xuất nếu thật sự cần), kiểm thử trước/sau và giải thích điều kiện kích hoạt, phạm vi, quyền sở hữu cùng chi phí bảo trì.
- **Điều kiện tiên quyết:** bộ khung kiểm soát G04, vòng lặp điều khiển tác nhân AI G05, kiểm chứng G06 và ngữ cảnh bài thực hành G08; có ít nhất một lỗi/mẫu hình thực được ghi lại.
- **Đầu vào:** nhật ký quyết định, ngữ cảnh lỗi, lặp lại yêu cầu cho AI, hồ sơ kiểm chứng và hiện tại bộ khung kiểm soát.
- **Đầu ra cho G10:** bộ khung kiểm soát nâng cao đã kiểm thử, giúp công việc phát hành lặp lại nhất quán hơn.
- **Thời lượng thiết kế ban đầu:** 90–180 phút tùy cơ chế; chỉ triển khai một nâng cấp chính trong đường tối thiểu. Cần dạy thử.

## Phạm vi nội dung

### Phải có

1. Phân biệt:
   - **Quy tắc:** ràng buộc/nguyên tắc luôn hoặc thường phải tuân thủ trong phạm vi xác định;
   - **Kỹ năng:** hướng dẫn chuyên biệt được kích hoạt cho một loại tác vụ;
   - **Quy trình:** chuỗi bước điều phối lặp lại, có đầu vào, điểm kiểm tra và đầu ra.
2. Trích ứng viên từ bằng chứng, không từ sở thích nhất thời.
3. Chọn cơ chế nhỏ nhất phù hợp với tần suất, biến thiên, rủi ro và nhu cầu tái sử dụng.
4. Xác định điều kiện kích hoạt, phạm vi, mục tiêu loại trừ, thẩm quyền, đầu vào, đầu ra và hành vi khi lỗi.
5. Tránh trùng lặp hoặc mâu thuẫn với nguồn chuẩn có thẩm quyền và cơ chế hiện có.
6. Kiểm thử bằng tác vụ đại diện cùng kiểm thử âm hoặc trường hợp biên; so sánh trước/sau.
7. Ghi bên chịu trách nhiệm, phiên bản, điều kiện cập nhật và cách sửa hoặc xóa khi cơ chế không còn giá trị.
8. Chỉ tự động hóa việc tìm kiếm, đóng gói hoặc lập chỉ mục sau khi có mẫu hình lặp lại và bằng chứng trước/sau; không coi công cụ nâng cao là đầu ra mặc định.

### Chưa thuộc học phần này

- Tạo nhiều kỹ năng hoặc quy tắc chỉ để đủ danh mục.
- Xây tác nhân AI nền tảng hoặc tự động hóa môi trường vận hành thật phức tạp.
- Đưa nội dung bài học vào quy tắc/kỹ năng thay cho nguồn chuẩn.
- Coi một lần thành công là bằng chứng cơ chế tổng quát.

## Mạch học đề xuất

1. **Khai thác bằng chứng:** rà nhật ký quyết định và lỗi để tìm một lỗi lặp lại hoặc yêu cầu cho AI thường xuyên phải viết lại.
2. **Chọn cơ chế:** so sánh không thay đổi/mẫu/quy tắc, kỹ năng hoặc quy trình và chọn phương án nhỏ nhất.
3. **Đặc tả:** viết điều kiện kích hoạt, phạm vi, mục tiêu loại trừ, bước, đầu ra, an toàn và bàn giao.
4. **Triển khai:** cho tác nhân AI hỗ trợ nền cơ chế; học viên kiểm định nội dung, đường dẫn và phần chồng lấn.
5. **Kiểm thử dương:** chạy một tác vụ đại diện và thu bằng chứng.
6. **Kiểm thử âm:** thử tác vụ không nên kích hoạt hoặc đầu vào thiếu để kiểm tra ranh giới và hành vi khi lỗi.
7. **So sánh và bảo trì:** so sánh trước và sau về tính nhất quán, công sức và lỗi; ghi bên chịu trách nhiệm và điều kiện kích hoạt kiểm tra lại.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Chỉ được bằng chứng dẫn tới nhu cầu nâng cấp;
- Giải thích đúng vì sao chọn quy tắc, kỹ năng hoặc quy trình;
- Cơ chế có điều kiện kích hoạt, phạm vi, đầu ra và hành vi khi lỗi rõ và không chồng chéo nguồn chuẩn;
- Có kiểm thử dương và kiểm thử âm cùng kết quả quan sát được;
- Học viên sửa hoặc từ chối ít nhất một đề xuất thiết kế quá mức cần thiết của AI;
- Có điều kiện bảo trì hoặc loại bỏ.

## Vai trò của AI

- Phân cụm bằng chứng, đề xuất phương án và các cơ chế cạnh tranh.
- Hỗ trợ dựng tệp và cấu trúc theo đặc tả đã duyệt.
- Tự kiểm tra tính nhất quán và hỗ trợ chạy kiểm thử tình huống.
- Không tự biến sở thích thành quy tắc hoặc tự tuyên bố kỹ năng tổng quát sau một tình huống.

## Quyền quyết định của học viên

Học viên chốt mẫu hình vấn đề, cơ chế, điều kiện kích hoạt, phạm vi, thẩm quyền, nội dung bắt buộc, bằng chứng `Pass`/`Fail` và quyết định giữ, sửa hoặc xóa nâng cấp.

## Điểm chạm với mã nguồn

- Đọc hoặc sửa Markdown, YAML hoặc cấu hình hoặc kịch bản nhỏ khi cơ chế thật sự cần.
- Quan sát tác nhân AI cơ chế phát hiện và điều kiện kích hoạt, tệp được đọc và phần thay đổi do quy trình tạo.
- Chạy kiểm thử tình huống và chẩn đoán lỗi phạm vi hoặc điều kiện kích hoạt.
- Không yêu cầu xây khung công nghệ tác nhân AI riêng.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** một quy tắc, kỹ năng hoặc quy trình có đặc tả rõ.
- **Sản phẩm trung gian phụ:** bằng chứng về nhu cầu, hồ sơ kiểm thử trước và sau, kiểm thử âm và ghi chú bảo trì.
- **Bằng chứng:** cơ chế cải thiện hành vi đã nêu mà không kích hoạt ngoài phạm vi hoặc mâu thuẫn nguồn chuẩn.
- **Cách kiểm tra:** một một tác nhân AI hoặc phiên mới dùng cơ chế trong tình huống đúng và bỏ qua hoặc báo lỗi rõ trong tình huống sai.

## Quy tắc an toàn áp dụng

- Quy tắc/kỹ năng không được tự cấp quyền hạn cao hơn chính sách hoặc yêu cầu người dùng.
- Quy trình có hành động bên ngoài, chi tiền, công bố hoặc xóa phải giữ phê duyệt ranh giới.
- Không đưa thông tin bí mật, dữ liệu cá nhân hoặc yêu cầu cho AI chứa dữ liệu thật vào tài nguyên hoặc kiểm thử.
- Giữ thay đổi có thể hoàn tác và không cài quan hệ phụ thuộc hoặc công cụ chưa được duyệt.

## Tài nguyên chuẩn phải dùng

- [Kế hoạch cho tác nhân AI](../../shared/templates/agent-plan.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)

## Đường xử lý lỗi bắt buộc

Phải có ứng viên quá rộng, trùng quy tắc khác hoặc điều kiện kích hoạt nhầm. Học viên thu hẹp đặc tả, sửa hoặc quyết định không tạo cơ chế rồi kiểm thử lại.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`; khi bài yêu cầu tạo/cập nhật Codex kỹ năng cục bộ, dùng `$repo-skill-creator` và đọc đầy đủ chỉ dẫn của nó.
2. Tạo bảng quyết định `no change → template → rule → skill → workflow` dựa trên bằng chứng, mức biến thiên và rủi ro.
3. Chuẩn bị một nhật ký lỗi đủ thực để học viên không phải bịa nhu cầu.
4. Bắt buộc kiểm thử dương và kiểm thử âm; không dùng “tệp đã tồn tại” làm bằng chứng.
5. Tách nguyên lý bộ khung kiểm soát khỏi định dạng hoặc công cụ cụ thể; chỉ đề xuất metadata, chỉ mục, RAG hoặc graph sau khi bảng bằng chứng cho thấy tìm kiếm hiện tại không đủ; xác minh định dạng/công cụ hiện hành bằng `$curriculum-reference-research`.
6. Dùng `$assessment-design` để đánh giá khả năng phán đoán chọn cơ chế, không đánh giá số tệp tạo ra.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Một mẫu hình thực được chuyển thành đúng một nâng cấp tối thiểu hoặc quyết định có căn cứ rằng chưa cần nâng cấp.
- Có ranh giới, kiểm tra xung đột, kiểm thử trước/sau và kế hoạch bảo trì.
- Học viên chứng minh quyền sở hữu thay vì chỉ chạy công cụ sinh tệp.
- Sản phẩm trung gian hỗ trợ G10 và bài học có kiểm định chất lượng.
