# G06 — Kiểm chứng đầu ra và quyết định

> **Vai trò của tệp:** bản định hướng thiết kế chuẩn cho G06. Đây là năng lực dùng bằng chứng để đánh giá sản phẩm và đầu ra AI, không phải bài học thuộc kiểm thử khung công nghệ.

## Đặc tả học phần

- **Vấn đề người học:** dễ coi đầu ra “trông đúng”, chạy một lần hoặc được AI tự xác nhận là bằng chứng đủ để nghiệm thu.
- **Kết quả quan sát được:** học viên thiết kế và thực hiện kiểm tra từ tiêu chí nghiệm thu, phát hiện ít nhất một lỗi/mismatch, rồi đưa ra quyết định accept, revise hoặc hoàn tác có dẫn chứng.
- **Điều kiện tiên quyết:** đặc tả G02, bộ khung kiểm soát G04 và thay đổi có dấu vết quyết định từ G05.
- **Đầu vào:** tiêu chí nghiệm thu, phần triển khai/nguyên mẫu, phần thay đổi, các giả định đã biết và trạng thái gốc.
- **Đầu ra:** hồ sơ kiểm chứng có thể dùng cho trình diễn nội bộ; tạo nền cho G07/G08 và các quyết định phát hành sau này.
- **Thời lượng thiết kế ban đầu:** lõi 75–90 phút; bản đầy đủ thêm kiểm thử dựa trên rủi ro và phục hồi. Phải dạy thử.

## Phạm vi nội dung

### Phải có

1. Phân biệt khẳng định, bằng chứng và phán quyết; lời tự xác nhận của AI không phải bằng chứng độc lập.
2. Chuyển tiêu chí nghiệm thu thành kiểm thử tình huống có đầu vào, hành động, kết quả dự kiến và thực tế.
3. Kiểm tra luồng thành công cùng ít nhất một lỗi, trạng thái trống hoặc trường hợp biên phù hợp.
4. Dùng nhiều loại bằng chứng vừa sức: quan sát hành vi, bảng điều khiển hoặc nhật ký, phần thay đổi, kiểm thử hoặc ảnh chụp màn hình có ngữ cảnh.
5. Xác định căn cứ xác định kết quả đúng: dựa vào đâu để biết kết quả đúng.
6. Chẩn đoán mismatch trước khi sửa; phân biệt lỗi đặc tả, phần triển khai, dữ liệu và môi trường.
7. Quyết định chấp nhận, sửa hoặc hoàn tác và ghi giới hạn của phán quyết.

### Chưa thuộc học phần này

- Bao phủ mọi loại kiểm thử hoặc dạy khung công nghệ testing chuyên sâu.
- Kiểm toán bảo mật chuyên nghiệp hoặc bảo đảm sản phẩm không có bug.
- Triển khai công khai; đó là G10.
- Dùng điểm số AI hay lời giải thích AI làm bằng chứng duy nhất.

## Mạch học đề xuất

1. **Kiểm định một khẳng định:** lấy câu “tính năng đã xong” và liệt kê bằng chứng còn thiếu.
2. **Suy ra kiểm thử:** biến tiêu chí trong G02 thành bảng đầu vào, hành động, kết quả dự kiến và thực tế.
3. **Luồng thành công:** thu bằng chứng có nguồn và thời điểm rõ.
4. **Đưa lỗi vào:** dùng dữ liệu trống/sai, mất quan hệ phụ thuộc hoặc một lỗi được chuẩn bị để xem hệ thống phản ứng.
5. **Chẩn đoán:** tác nhân AI đề xuất nguyên nhân; học viên đối chiếu nhật ký, phần thay đổi và đặc tả và chọn giả thuyết đáng thử.
6. **Phục hồi:** sửa nhỏ hoặc hoàn tác, chạy lại cùng kiểm thử để so sánh.
7. **Verdict:** ghi `Pass`/`Fail`/`Not verified`, giới hạn và quyết định tiếp theo; chuẩn bị trình diễn nội bộ nếu theo chương trình thực hành ngắn.

## Mục tiêu và tiêu chí đạt

Học viên đạt khi:

- Mỗi phán quyết quan trọng truy được về tiêu chí và bằng chứng;
- Có kết quả dự kiến và thực tế thay vì nhận xét “có vẻ ổn”;
- Phát hiện được ít nhất một đầu ra sai, thiếu, không chạy hoặc vượt phạm vi;
- Giải thích được nguyên nhân đang là dữ kiện hay giả thuyết;
- Thực hiện thử lại hoặc hoàn tác an toàn và kiểm tra lại;
- Không khẳng định vượt quá phạm vi đã kiểm thử.

## Vai trò của AI

- Đề xuất kiểm thử tình huống, trường hợp biên và giả thuyết nguyên nhân.
- Hỗ trợ chạy lệnh, đọc nhật ký và phần thay đổi và tóm tắt bằng chứng.
- Tranh luận phán quyết hoặc tìm cách chứng ngụy kết luận hiện tại.
- Không tự quyết định đầu ra của chính nó đã đạt.

## Quyền quyết định của học viên

Học viên chốt tiêu chí ưu tiên, bằng chứng đáng tin, căn cứ xác định kết quả đúng, giả thuyết cần thử, phán quyết và việc chấp nhận, sửa hoặc hoàn tác. Học viên phải nêu giới hạn của kết luận.

## Điểm chạm với mã nguồn

- Chạy xem trước hoặc lệnh kiểm thử đã được hướng dẫn.
- Đọc lỗi, bảng điều khiển, nhật ký và phần thay đổi liên quan tới hành vi thất bại.
- Theo dấu tiêu chí tới phần phần triển khai có khả năng chịu trách nhiệm.
- Cho tác nhân AI tạo hoặc sửa kiểm thử nhỏ, sau đó học viên kiểm tra kiểm thử có thật sự chứng minh tiêu chí không.

## Sản phẩm trung gian và bằng chứng hoàn thành

- **Sản phẩm trung gian chính:** hồ sơ bằng chứng kiểm chứng.
- **Sản phẩm trung gian phụ:** ma trận kiểm thử, chẩn đoán lỗi và mục trong nhật ký quyết định cho phán quyết.
- **Bằng chứng:** có bằng chứng trước và sau hoặc kết quả dự kiến và thực tế, ít nhất một lỗi tình huống và kết quả kiểm thử lại sau sửa/hoàn tác.
- **Cách kiểm tra:** Người kiểm định có thể tái hiện tối thiểu một kiểm thử và hiểu phán quyết mà không dựa vào lời khẳng định của AI.

## Quy tắc an toàn áp dụng

- Kiểm thử trên máy cục bộ hoặc môi trường thử nghiệm với dữ liệu giả; không gây tác động phụ lên môi trường vận hành thật hoặc tài khoản thật.
- Che thông tin bí mật và dữ liệu nhạy cảm khỏi nhật ký, ảnh chụp màn hình và sản phẩm trung gian.
- Chuẩn bị điểm kiểm tra và hoàn tác trước khi đưa lỗi vào hoặc sửa mã nguồn.
- Ghi rõ kiểm thử chưa chạy hoặc bằng chứng không thu được là `Not verified`.

## Tài nguyên chuẩn phải dùng

- [Đặc tả sản phẩm](../../shared/templates/product-spec.md)
- [Nhật ký quyết định](../../shared/templates/decision-log.md)
- [Chuẩn kiểm chứng](../../shared/policies/verification-standard.md)
- [Bằng chứng và tự phản tư](../../shared/practices/evidence-and-reflection.md)
- [Tiếp xúc với mã nguồn](../../shared/practices/code-contact.md)
- [Thử nghiệm an toàn](../../shared/practices/safe-experimentation.md)

## Đường xử lý lỗi bắt buộc

Phải có ít nhất một “dương tính giả”: giao diện đẹp hoặc kiểm thử đạt nhưng không chứng minh đúng tiêu chí; và một lỗi có thể phục hồi. Học viên phải sửa cách kiểm chứng, không chỉ sửa sản phẩm.

## Hướng dẫn cho tác nhân AI triển khai

1. Dùng `$lesson-authoring`, `$assessment-design` và mẫu kiểm chứng chuẩn trong `shared/policies/` khi được hoàn thiện.
2. Chuẩn bị nguyên mẫu có lỗi có chủ đích nhưng an toàn và có đường đặt lại.
3. Tạo bảng kiểm thử tối thiểu, hướng dẫn xử lý sự cố cho giảng viên và hoạt động hoạt động phản biện phán quyết của AI.
4. Bản chương trình thực hành ngắn chỉ cần một luồng thành công, một lỗi và trình diễn nội bộ; không hứa mức sẵn sàng phát hành.
5. Bản đầy đủ mở rộng theo rủi ro, không theo số lượng kiểm thử tùy ý.
6. Xác minh mọi lệnh hoặc chỉ dẫn riêng cho công cụ bằng `$curriculum-reference-research`.

## Điều kiện hoàn thành cho phần bài giảng sau này

- Học viên tự tạo/chọn kiểm thử, thu bằng chứng và đưa ra phán quyết.
- Có thử thách dương tính giả, lỗi phục hồi và điểm chạm mã nguồn vừa sức.
- Chương trình thực hành ngắn có thể kết thúc bằng trình diễn nội bộ với giới hạn được nói rõ.
- Bài học có kiểm định các cổng chất lượng; không gọi `Validated` nếu chưa có dạy thử phù hợp.
