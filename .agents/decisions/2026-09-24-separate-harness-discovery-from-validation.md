# Tách khám phá vấn đề khỏi kiểm chứng cải tiến harness

- Ngày: 2026-09-24
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu kho qua yêu cầu trực tiếp trong phiên làm việc
- Phạm vi ảnh hưởng: skill khám phá mới, workflow cải tiến harness, danh mục điều hướng, ghi chú thiết kế, tài liệu tổng quát hóa harness và cấu hình derived index loại trừ vùng `temp/` cục bộ
- Thay thế hồ sơ: Không thay thế quyết định pilot; thu hẹp phạm vi vận hành và đổi tên workflow được thiết kế trong `2026-09-15-agent-harness-workflow-proposed.md`
- Tên cũ: `optimize-agent-harness-system`
- Tên hiện hành: `validate-agent-harness-improvement`

## Bối cảnh và xung đột

Workflow cũ mang tên “optimize” nhưng chỉ hoạt động tốt sau khi đã có một vấn đề hoặc giả thuyết đủ cụ thể để lập baseline, thử candidate, kiểm định và ratify. Tên và đầu vào cũ làm người đọc có thể hiểu nhầm rằng workflow cũng tự rà soát các run, phát hiện vấn đề chưa biết và đề xuất không gian giải pháp.

Một workflow chi tiết hữu ích cho trial có kiểm soát nhưng tạo context không cần thiết và hạn chế khám phá mở vốn thường được giao cho mô hình suy luận mạnh. Đồng thời, yêu cầu audit của Chủ sở hữu có thể hợp lệ ngay cả khi chưa có metric vượt ngưỡng hoặc lỗi lặp lại.

## Các phương án đã cân nhắc

1. Giữ một workflow duy nhất và thêm giai đoạn khám phá mở ở đầu.
2. Tạo thêm một workflow audit rút gọn trước workflow hiện tại.
3. Dùng một skill read-only cho discovery, chuẩn hóa candidate handoff và thu hẹp/đổi tên workflow hiện tại.

Phương án 1 tiếp tục nạp context trial chi tiết vào công việc cần phán đoán mở. Phương án 2 thêm trạng thái, run record và điều phối nhiều vai trò dù discovery có thể do một tác nhân mạnh hoàn thành đầu-cuối. Phương án 3 giữ đúng ranh giới skill/workflow và được chọn.

## Bằng chứng thuận và nghịch

Workflow hiện tại đã có giá trị cho baseline, contract, test matrix, independent review, rollback và ratification sau khi có vấn đề cụ thể. Tuy nhiên trigger yêu cầu audit chung không tự cung cấp mệnh đề kiểm tra được mà các giai đoạn đó cần. Các workflow run hiện có cũng không bao phủ invocation của skill, nên discovery không được phép tuyên bố đã đánh giá toàn bộ harness.

Việc tách lớp tạo thêm một interface candidate cần duy trì. Rủi ro này được giới hạn bằng một schema duy nhất nằm trong skill và được workflow tuyên bố tiếp nhận trực tiếp.

## Quyết định

1. Tạo skill `$harness-improvement-discovery` ở mức tự do cao để rà soát bằng chứng vận hành mà không sửa harness.
2. Cho phép một lượt discovery trả không, một hoặc nhiều candidate; mỗi candidate là một vấn đề gốc độc lập.
3. Chuẩn hóa candidate để tương thích trực tiếp với đầu vào workflow, nhưng không tự động mở trial.
4. Đổi tên workflow thành `validate-agent-harness-improvement` và giới hạn đầu vào ở candidate `Ready` hoặc giả thuyết cụ thể do Chủ sở hữu chỉ định.
5. Giữ workflow ở trạng thái `Proposed`; quyết định này không tự nâng thành `Active` và không ratify bất kỳ trial tương lai nào.
6. Giữ nguyên hồ sơ workflow-run lịch sử. Các chuỗi tên cũ trong bằng chứng quá khứ mô tả đúng baseline tại thời điểm chạy và không được viết lại hồi tố.

## Hệ quả và chuyển đổi

- Cập nhật nguồn điều hướng hiện hành, liên kết thiết kế và tài liệu portable sang tên mới.
- Giữ `temp/` là vùng local/ignored và loại nó khỏi derived index được commit; tài liệu portable trong đó được mang sang repo khác như một export thủ công, không trở thành nguồn chuẩn của repo này.
- Các liên kết hoặc chuỗi trong decision/run lịch sử có thể giữ tên cũ; hồ sơ này cung cấp ánh xạ sang tên hiện hành.
- Skill chỉ có thể đánh giá những dấu vết tồn tại. Cho tới khi invocation của skill được lưu bền vững, mọi discovery report phải nêu rõ giới hạn phủ dữ liệu này.
- Candidate rõ ràng và cơ học có thể được bàn giao cho sửa hẹp; candidate còn bất định đi qua workflow validation.

## Phạm vi kiểm định lại

- Trigger, ranh giới không-sửa và schema đầu ra của skill.
- Tính tương thích giữa candidate `Ready` và mục 4.1/Giai đoạn A của workflow.
- Tên, đường dẫn và mô tả hiện hành trong `README.md`, `.agents/workflows/README.md` và tài liệu portable.
- Link validation, skill validation và derived context index sau đổi tên.

## Chưa được quyết định

Cơ chế ghi dấu mọi invocation của skill là một hạng mục nền tảng riêng. Quyết định này chỉ buộc skill báo giới hạn dữ liệu, không thiết kế hoặc triển khai telemetry đó.

## Kiểm định quản trị

Lượt kiểm định độc lập tại `.agents/workflow-runs/20260924-1914-harness-discovery-validation-split/` xác nhận ranh giới skill/workflow, schema candidate, lịch sử, metadata và tài liệu portable. Reviewer ban đầu phát hiện derived index nhận nguồn `temp/` local/ignored; finding được chấp nhận, sửa bằng exclude `temp/**` mà không chạm `.gitignore`, rồi re-review `Pass`. Không còn `Blocker` hoặc `Major` chưa xử lý.

## Điều kiện xem xét lại

- Discovery skill thường xuyên tạo candidate không thể đưa vào workflow mà phải viết lại thủ công.
- Hướng dẫn tự do cao tạo false positive hoặc chi phí review lớn hơn phần vấn đề tìm được.
- Runtime cung cấp telemetry skill đủ mạnh để thay đổi chiến lược lấy mẫu hoặc schema bằng chứng.
- Một loại candidate lặp lại đủ ổn định để chuyển sang đường sửa xác định thay vì controlled trial.
