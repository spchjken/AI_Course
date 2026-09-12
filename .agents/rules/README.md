# Luật dựng giáo trình

Các luật trong thư mục này áp dụng khi tạo, sửa, kiểm định hoặc sắp xếp nội dung của chương trình AI-native Builder.

## Nguyên tắc trọng yếu: giải quyết xung đột bằng suy luận và bằng chứng

Khi ý kiến của người dùng, nhận định của AI, tài liệu hiện có hoặc nguồn tham khảo mâu thuẫn theo cách có thể làm thay đổi kết quả công việc:

1. Không mặc định AI đúng và không đồng ý với người dùng chỉ để chiều theo ý kiến của họ.
2. Nêu chính xác các mệnh đề đang xung đột và hệ quả của từng mệnh đề đối với quyết định cần đưa ra.
3. Phân biệt dữ kiện kiểm chứng được, suy luận, giả định, lựa chọn ưu tiên và quyết định sản phẩm. Lựa chọn ưu tiên thuộc quyền người dùng; dữ kiện không trở thành đúng chỉ vì người dùng hoặc AI khẳng định nó.
4. Trình bày lập luận của người dùng theo phiên bản mạnh và hợp lý nhất trước khi phản biện. Không dựng một phiên bản yếu hơn để dễ bác bỏ.
5. Mặc định chủ động tìm bằng chứng có khả năng **chứng thực lẫn chứng ngụy** lập luận. Không yêu cầu người dùng tự tìm nguồn khi AI có thể kiểm tra bằng công cụ hiện có.
6. Khi người dùng cung cấp dẫn chứng, mở và kiểm tra trực tiếp nguồn đó: độ tin cậy, ngữ cảnh, thời điểm, phạm vi áp dụng và mức độ thực sự hỗ trợ cho kết luận.
7. Ưu tiên nguồn gốc, nguồn chính thức và thông tin hiện hành. Trích dẫn gần nhận định được hỗ trợ; không dùng số lượng nguồn để thay thế chất lượng lập luận.
8. Không sáng tạo lý thuyết, thuật ngữ hoặc cơ chế không có cơ sở để bảo vệ câu trả lời trước đó. Nếu câu trả lời trước sai hoặc thiếu, thừa nhận và sửa trực tiếp.
9. Đưa ra kết luận kèm chuỗi suy luận, bằng chứng thuận/nghịch, mức độ chắc chắn và phần còn chưa biết. Nếu bằng chứng chưa đủ, nói rõ sự bất định thay vì ép ra kết luận giả tạo.
10. Không thực hiện thay đổi phụ thuộc vào tiền đề đang tranh chấp cho đến khi xung đột được giải quyết. Trong thời gian đó, được phép đọc, tìm nguồn, kiểm tra và phân tích nếu các bước này không làm thay đổi trạng thái.

Một xung đột được xem là đã giải quyết khi xảy ra ít nhất một trong các trường hợp:

- Các bên thống nhất kết luận dựa trên bằng chứng và suy luận đã trình bày.
- Dữ kiện đã được xác minh đủ để loại bỏ một mệnh đề, và người dùng chấp nhận kết luận sửa đổi.
- Bằng chứng không thể quyết định lựa chọn ưu tiên hoặc đánh đổi; người dùng đưa ra quyết định sản phẩm sau khi đã thấy rõ hệ quả và sự bất định.
- Tiền đề gây xung đột được rút lại hoặc thay thế bằng một giả định được ghi rõ.

Sau khi giải quyết, cập nhật nguồn chuẩn có thẩm quyền chịu ảnh hưởng và ghi lý do vào hồ sơ quyết định trong `.agents/decisions/` rồi mới tiếp tục phần triển khai phụ thuộc vào quyết định đó. Hồ sơ quyết định lưu lịch sử và bằng chứng, không thay thế nguồn chuẩn hiện hành. Mẫu nhật ký quyết định trong `ai-native-builder/shared/` là sản phẩm dành cho học viên, không dùng cho quyết định quản trị giáo trình.

## Thứ tự đọc

1. `curriculum-contract.md` — xác định nội dung phải phù hợp với nguồn nào và nằm ở đâu.
2. `glossary.md` — dùng nghĩa chuẩn và từ vựng tiếng Việt thống nhất.
3. `authoring-standard.md` — xác định một bài học đạt chuẩn phải được thiết kế thế nào.
4. `quality-gates.md` — kiểm tra nội dung trước khi tuyên bố hoàn thành.
5. `safety-and-currency.md` — áp dụng khi nội dung liên quan dữ liệu, công cụ, API, quyền hạn, triển khai hoặc thông tin thay đổi theo thời gian.

## Quy trình bắt buộc

Khi tạo hoặc sửa nội dung giáo trình:

1. Xác định nguồn chuẩn có thẩm quyền và mục tiêu `gNN` liên quan.
2. Kiểm tra điều kiện tiên quyết và nội dung phụ thuộc.
3. Soạn nội dung theo `authoring-standard.md`.
4. Chạy toàn bộ cổng bắt buộc và chấm điểm chất lượng theo `quality-gates.md`.
5. Ghi kết quả kiểm định có dẫn chứng; không tuyên bố hoàn thành khi còn cổng bắt buộc thất bại.
6. Cập nhật tài liệu phụ thuộc nếu thay đổi làm lệch kế hoạch, kiến trúc nội dung, bản đồ chương trình hoặc lịch của lộ trình.

## Thứ tự ưu tiên về thẩm quyền và tài liệu

Thứ tự này xác định ai có quyền quyết định mục tiêu và tài liệu nào chi phối phần triển khai. Nó không được dùng để quyết định một khẳng định thực tế là đúng hay sai.

1. Yêu cầu mới nhất và rõ ràng của người dùng về mục tiêu, phạm vi, lựa chọn ưu tiên và quyết định sản phẩm.
2. `AI-native-builder-curriculum-plan.md` về mục đích, đối tượng, phạm vi, thời lượng và đầu ra.
3. `curriculum-content-architecture.md` về mục tiêu, quan hệ phụ thuộc và kiến trúc nội dung.
4. Các luật trong thư mục này.
5. Nội dung đã triển khai trong `ai-native-builder/`.

Khi hai nguồn mâu thuẫn, phải chỉ ra mâu thuẫn và đồng bộ các tài liệu liên quan. Không âm thầm chọn một nguồn rồi để kho dự án ở trạng thái không nhất quán.

## Thay đổi hệ thống quy tắc

Thay đổi trong `.agents/rules/` là thay đổi quản trị. Trước khi nghiệm thu:

1. Ghi vấn đề, lý do, phương án, hệ quả và bằng chứng vào một hồ sơ trong `.agents/decisions/`.
2. Xác định rõ tệp, quy trình, kỹ năng và nội dung giáo trình bị ảnh hưởng.
3. Chỉ kiểm định lại phạm vi chịu ảnh hưởng; không mặc định kiểm định lại toàn bộ giáo trình khi không có quan hệ phụ thuộc liên quan.
4. Ghi ngày có hiệu lực và yêu cầu chuyển đổi nếu quy tắc mới phải áp dụng cho nội dung cũ.
5. Không hồi tố âm thầm. Nội dung cũ chỉ bị thay đổi trạng thái hoặc buộc sửa khi hồ sơ quyết định chỉ rõ phạm vi và lý do.
6. Có một lượt kiểm định quản trị tách khỏi người viết trước khi coi quy tắc mới là chuẩn.
