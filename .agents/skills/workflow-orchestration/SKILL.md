---
name: workflow-orchestration
description: Run repository workflows with dynamic work-unit dispatch, scoped subagent delegation, lifecycle evidence, file ownership, and independent-review verification. Use when executing a multi-role workflow in .agents/workflows; do not use for a single specialist task or to bypass human decision gates.
---

# Điều phối quy trình

Điều hành một quy trình nhiều vai trò mà không đồng nhất vai trò với tác nhân.

## Chuẩn bị lượt chạy

1. Đọc `.agents/rules/README.md`, `.agents/workflows/README.md`, quy trình được chọn và `.agents/workflows/agent-dispatch-protocol.md`.
2. Xác nhận quy trình là `Active`, hoặc người dùng đã cho phép chạy thử trạng thái `Proposed`.
3. Tạo mã lượt và `.agents/workflow-runs/<run-id>/orchestration-log.md`.
4. Ghi phạm vi, nguồn chuẩn, cổng quyết định của con người, giới hạn đồng thời và điều kiện kết thúc.
5. Mở skill trace cho chính `$workflow-orchestration`; gắn `parent_workflow_run` bằng run id vừa tạo. Nếu runtime chưa có recorder, ghi `Not verified` thay vì giả lập trace.

## Phân công theo ngữ cảnh

Trước mỗi đơn vị công việc, lập hợp đồng đầu vào, đầu ra, tệp cho phép, kỹ năng, điều kiện đạt và điều kiện dừng. Áp dụng cổng phân công trong giao thức rồi chọn đúng một hành động: Điều phối viên tự làm, tái sử dụng tác nhân, sinh tác nhân chuyên trách, sinh Người kiểm định mới hoặc trì hoãn.

Được phép sinh tác nhân con trong phạm vi quy trình mà người dùng đã yêu cầu chạy. Không dùng quyền này để mở rộng mục tiêu, tác động hệ thống ngoài phạm vi hoặc vượt cổng phê duyệt.

Không sinh tác nhân chỉ để phản chiếu tên vai trò. Không chạy song song các công việc phụ thuộc nhau hoặc có quyền ghi cùng tệp.

## Sinh và quản lý tác nhân

- Gửi cho tác nhân đúng hợp đồng công việc và các tệp nguồn cần đọc; không dựa vào trí nhớ hội thoại.
- Với mỗi repository-local skill trong task contract, yêu cầu tác nhân mở/đóng trace theo `AGENTS.md` và trả `execution_id`/`trace_path`; ghi kết quả vào sổ điều phối.
- Dùng lại tác nhân cho chuỗi cần giữ mạch nếu nó không phải Người kiểm định độc lập.
- Với kiểm định độc lập, sinh một lượt mới không kế thừa hội thoại khi công cụ cho phép và chỉ truyền tệp, tiêu chí cùng phạm vi kiểm tra.
- Ghi mã tác nhân hoặc tên nhiệm vụ chuẩn, tác nhân cha, hành động phân công, thời điểm, trạng thái và đầu ra từ dữ liệu công cụ.
- Chờ, ngắt hoặc giao tiếp việc chỉ qua Điều phối viên; không để tác nhân tự mở rộng cây phân công nếu hợp đồng không cho phép.

## Kiểm chứng việc phân tách

Khi chưa biết phiên hiện tại có thực sự hỗ trợ tác nhân con, chạy phép thử không ghi tệp ở mục 6.1 của giao thức. Chỉ ghi `Spawn verified` khi có định danh tác nhân con mới do công cụ trả về, quan hệ cha–con quan sát được, mã thử khớp và trạng thái hoàn thành.

Chỉ ghi `Independent review verified` khi định danh Người kiểm định khác người tạo/sửa, lượt đó được sinh mới và kết luận dựa trên việc đọc trực tiếp đầu ra. Nếu không chứng minh được, ghi `Not verified` và không cấp `Pass` cho cổng độc lập.

## Tích hợp và kết thúc

1. Kiểm tra đầu ra của mỗi tác nhân tại vị trí cam kết trước khi mở đơn vị phụ thuộc.
2. Trả lỗi về đúng bên sở hữu; không tạo một tác nhân sửa chung khi có thể định tuyến chính xác.
3. Cập nhật sổ sau mọi thay đổi trạng thái.
4. Đóng hoặc ngừng tái sử dụng tác nhân khi công việc của nó kết thúc.
5. Kết thúc lượt chỉ khi đạt điều kiện của quy trình chuyên môn và mục 8 của giao thức.
