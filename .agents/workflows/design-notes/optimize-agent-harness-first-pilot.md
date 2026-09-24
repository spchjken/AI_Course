# Kế hoạch pilot đầu tiên của workflow kiểm chứng cải tiến harness

- **Trạng thái:** `Draft` — chưa được phê duyệt chạy.
- **Workflow hiện hành:** [`../validate-agent-harness-improvement.md`](../validate-agent-harness-improvement.md), mang tên `optimize-agent-harness-system` tại thời điểm pilot.
- **Mục đích:** Cung cấp contract ứng viên để kiểm tra workflow trên một thay đổi định tuyến hẹp; không cho phép triển khai.

## Phạm vi ứng viên

Pilot kiểm tra giả thuyết rằng metadata tối thiểu và một chỉ mục dẫn xuất có thể giúp tác nhân mới tìm đúng nguồn có thẩm quyền với ít lượt đọc hơn mà không làm tăng lỗi nguồn, vượt quyền hay bỏ cổng.

Phạm vi tối đa gồm một `goals/gNN-*/README.md`, một workflow, một decision record và một chỉ mục dẫn xuất mới. Skill hiện có chỉ được đọc để kiểm tra liên kết; sửa skill nằm ngoài pilot đầu tiên. Tệp và mã `gNN` cụ thể phải được Chủ sở hữu chọn tại cổng `Approve trial`.

## Baseline và candidate

- Baseline: tác nhân mới dùng cấu trúc kho và tìm kiếm tệp hiện tại.
- Candidate: cùng tác nhân/lớp mô hình và cùng bộ câu hỏi, có thêm metadata tối thiểu cùng chỉ mục dẫn xuất không phải nguồn chuẩn.
- Mỗi bên chạy cùng số lần; thứ tự câu hỏi được cân bằng nếu runtime cho phép.
- Không dùng nội dung hội thoại trước, dữ liệu cá nhân, secret hoặc tài khoản ngoài.

## Metric ứng viên

- Primary metric: tỷ lệ chọn đúng nguồn có thẩm quyền cho từng câu hỏi.
- Guardrails: không tăng số lần chọn nguồn sai; không tăng lỗi bỏ cổng/thẩm quyền; mọi kết quả truy vết được tới tệp; metadata sai phải báo lỗi thay vì đoán.
- Secondary metrics: số tệp đọc, số lượt định tuyến và thời gian tới nguồn đúng.

Ngưỡng, số mẫu và rubric phải được khóa trong `trial-contract.md` trước khi chạy; các giá trị ở đây chưa phải quyết định.

## Bốn lớp kiểm thử

1. `Positive`: câu hỏi có nguồn rõ trong bốn loại tệp thử.
2. `Negative`: metadata thiếu, sai trạng thái, trỏ nguồn không có thẩm quyền hoặc yêu cầu ngoài phạm vi.
3. `Regression`: tìm kiếm theo đường dẫn/tiêu đề vẫn hoạt động khi metadata không có; liên kết hiện hữu không hỏng.
4. `Comparison`: baseline và candidate nhận cùng input, quyền đọc và timebox.

## Quyền sửa và rollback ứng viên

- Chỉ nhánh/worktree trial được sửa trước `Ratify`.
- Danh sách tệp `Update` phải được Chủ sở hữu ghi tường minh; mọi tệp khác là `Reverify`, `No change` hoặc `Not verified`.
- Chỉ mục phải được đánh dấu dẫn xuất và có thể tái tạo/xoá mà không mất nguồn chuẩn.
- Rollback bằng commit đảo đúng phạm vi; không di trú toàn kho, không xây RAG/graph database và không sửa nội dung bài học.

## Cổng quyết định

Kế hoạch này không phải `Approve trial`. Trước khi chạy, Chủ sở hữu phải chốt tệp, baseline SHA, số lần chạy, primary threshold, guardrails, timebox, dữ liệu được giữ và reviewer độc lập. Sau kiểm định, chỉ `Ratify` mới cho tích hợp candidate.

## Điều kiện kết thúc pilot

Pilot chỉ đóng theo mục 10 của workflow. Kết quả của một pilot không tự chứng minh workflow `Active`, không cho phép di trú metadata và không tổng quát hoá sang mọi tác vụ.
