# Xác định quan hệ giữa vai trò và tác nhân trong quy trình

- Ngày: 2026-09-05
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/workflows/change-curriculum-architecture.md`, `.agents/workflows/complete-goal-lessons.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Hai quy trình dùng nhiều vai trò nhưng chưa nói rõ một vai trò có tương ứng với một tác nhân con hay không. Việc mặc định sinh tác nhân cho mọi vai trò làm tăng bàn giao và mất mạch; việc để một tác nhân đổi vai xuyên suốt lại không tạo được kiểm định độc lập.

## Các phương án đã cân nhắc

1. Một tác nhân duy nhất đổi vai trong toàn bộ lượt thực thi.
2. Sinh một tác nhân mới cho mỗi tên vai trò hoặc mỗi đơn vị công việc.
3. Dùng mô hình lai: tái sử dụng tác nhân khi cần giữ mạch, tách theo chuyên môn và bắt buộc ngữ cảnh độc lập tại cổng kiểm định.

## Bằng chứng thuận và nghịch

- Chẩn đoán, thiết kế và phân tích ảnh hưởng cần dùng chung mô hình vấn đề; chia nhỏ quá mức dễ tạo sai lệch giữa các bản bàn giao.
- Nghiên cứu, đánh giá năng lực và kiểm định có mục tiêu cùng thiên kiến khác với soạn nội dung nên có lợi khi tách ngữ cảnh.
- Tác nhân con làm tăng chi phí điều phối, vì vậy không nên sinh chỉ để phản chiếu tên vai trò.
- Người soạn tự kiểm tra hữu ích để bắt lỗi cục bộ nhưng không đáp ứng quy tắc kiểm định độc lập.

## Quyết định

- Vai trò là ranh giới trách nhiệm; đơn vị công việc là ranh giới đầu ra; tác nhân là ngữ cảnh thực thi. Ba khái niệm không đồng nhất.
- Điều phối viên phải quyết định tường minh khi nào tạo hoặc tái sử dụng tác nhân.
- Dùng `.agents/workflows/agent-dispatch-protocol.md` làm cổng phân công chung và `$workflow-orchestration` để thực thi cổng đó.
- Dùng lại cùng tác nhân cho chuỗi công việc cần giữ mạch; tách tác nhân theo chuyên môn, khả năng chạy độc lập hoặc nhu cầu cô lập ngữ cảnh.
- Cổng kiểm định bắt buộc dùng người khác hoặc một lượt tác nhân mới không tham gia tạo và sửa đầu ra được kiểm định.
- Nếu không có khả năng tạo ngữ cảnh kiểm định độc lập, được phép tự kiểm tra nhưng không được cấp kết quả `Pass` hay nâng trạng thái chất lượng.
- Không công nhận việc sinh tác nhân nếu thiếu định danh mới do công cụ trả về, quan hệ cha–con, hợp đồng công việc, trạng thái và đầu ra được kiểm tra. Lượt chạy lưu bằng chứng tại `.agents/workflow-runs/<run-id>/orchestration-log.md`.

## Hệ quả và phạm vi chuyển đổi

- `change-curriculum-architecture` mặc định dùng Điều phối viên chính, một tác nhân kiến trúc xuyên B–D–E, nghiên cứu có điều kiện, thực hiện và kiểm định độc lập.
- `complete-goal-lessons` có thể dùng một tác nhân soạn xuyên D0–D3 thay vì sinh mới cho từng tệp; D4 tách theo chuyên môn, D6 ưu tiên tách để tích hợp và E luôn độc lập.
- Tác nhân sửa ở giai đoạn F được định tuyến về đơn vị sở hữu phát hiện thay vì trở thành một vai trò sửa chung thiếu ngữ cảnh.
- Mỗi môi trường chưa được kiểm chứng phải chạy phép thử sinh tác nhân không ghi tệp trước lần phân công đầu tiên; thất bại được ghi `Spawn not verified` để làm dữ liệu cải tiến.
- Phép thử ngày 2026-09-05 trên phiên Codex extension hiện tại đã đạt `Spawn verified`; bằng chứng nằm trong `.agents/workflow-runs/20260905-235254-agent-dispatch-probe/orchestration-log.md`. Môi trường trả tên nhiệm vụ chuẩn làm định danh quan sát được, không trả thêm mã tác nhân dạng số.
- README gốc và README của hệ thống quy trình phải phân biệt gọi kỹ năng với chạy quy trình, trỏ tới giao thức phân công, mô tả hồ sơ vận hành và dùng “định danh do công cụ trả về” thay cho giả định luôn có mã tác nhân dạng số.

## Điều kiện xem xét lại

- Môi trường thực thi không hỗ trợ tái sử dụng tác nhân con qua nhiều lượt giao việc.
- Chi phí bàn giao lớn hơn lợi ích của việc tách chuyên môn.
- Thử nghiệm cho thấy cùng một tác nhân ở D0–D3 tạo thiên kiến hoặc lỗi nhất quán mà D6 không bắt được.
- Nền tảng cung cấp cơ chế kiểm định độc lập có bảo đảm mạnh hơn việc dùng một lượt tác nhân mới.
