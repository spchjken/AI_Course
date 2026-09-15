# Hoàn thiện quy trình tối ưu hệ thống harness tác nhân

- Ngày: 2026-09-15
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu kho qua yêu cầu trực tiếp hoàn thiện workflow
- Phạm vi ảnh hưởng: `.agents/workflows/optimize-agent-harness-system.md`, `.agents/workflows/README.md`, `README.md`, ghi chú thiết kế liên quan
- Thay thế hồ sơ: `2026-09-12-agent-harness-optimization-workflow.md`

## Bối cảnh và xung đột

Hồ sơ ngày 2026-09-12 chỉ cho phép một `Placeholder` vì chưa có trigger, baseline, quyền sở hữu, controlled trial, rollback, kiểm định độc lập và migration đầy đủ. Sau đó workflow và danh mục đã xuất hiện trạng thái `Proposed` nhưng đặc tả vẫn chỉ có ba giai đoạn rút gọn, còn README gốc và ghi chú thiết kế vẫn mô tả `Placeholder`.

Giữ trạng thái hiện tại sẽ để nguồn vận hành không nhất quán. Hạ toàn bộ về `Placeholder` sẽ bỏ qua yêu cầu trực tiếp của Chủ sở hữu về việc hoàn thiện workflow theo chuẩn các workflow khác.

## Các phương án đã cân nhắc

1. Chỉ sửa câu chữ và giữ workflow ngắn.
2. Đồng bộ trở lại `Placeholder` và hoãn thiết kế.
3. Hoàn thiện đặc tả thực thi, giữ `Proposed`, bắt buộc phê duyệt riêng cho từng trial và yêu cầu bằng chứng thực tế trước khi cân nhắc `Active`.

## Bằng chứng thuận và nghịch

Các workflow hoàn chỉnh trong kho đều có phép thử kích hoạt, trạng thái, đầu vào/đầu ra, quyền sở hữu, giai đoạn có điều kiện ra, kiểm chứng, rollback, hợp đồng tác nhân và điều kiện đóng. `agent-dispatch-protocol.md` đã cung cấp cơ chế phân công, kiểm định độc lập và phân xử finding dùng chung nên workflow mới không cần tạo một cơ chế cạnh tranh.

Mặt khác, chưa có controlled trial nào chứng minh quy trình tối ưu harness vận hành hiệu quả. Vì vậy `Active` chưa có căn cứ; bản đặc tả chỉ đủ để kiểm định và chạy thử hẹp khi được cho phép.

## Quyết định

- Hoàn thiện `optimize-agent-harness-system` thành workflow `Proposed` với hai chế độ `Incident containment` và `Improvement trial`.
- Mỗi lượt phải có trigger, baseline, nguyên nhân cạnh tranh, impact map, contract xác định trước, cô lập Git, bốn lớp kiểm thử, kiểm định quản trị độc lập, cổng `Ratify` và rollback.
- Mỗi controlled trial vẫn cần Chủ sở hữu phê duyệt tường minh; quyết định này không cho phép chạy trial hay sửa harness sản xuất hàng loạt.
- Không coi tối ưu token, thời gian hoặc số tệp là thành công nếu độ đúng, an toàn, tuân thủ thẩm quyền hoặc khả năng truy vết giảm.
- Ghi chú thiết kế được giữ làm bối cảnh lịch sử; workflow là nguồn vận hành duy nhất.
- Kế hoạch pilot đầu tiên được lưu riêng ở trạng thái `Draft`; quyết định này không phải `Approve trial`.

## Hệ quả và phạm vi chuyển đổi

Danh mục gốc và danh mục workflow được đồng bộ về `Proposed`. Không có nội dung, kiến trúc giáo trình, rules, skills hay hệ thống ngoài kho nào được thay đổi bởi quyết định này. Trial tương lai phải tạo hồ sơ riêng trong `.agents/workflow-runs/` và decision record khi chạm các thành phần quản trị đã nêu trong workflow.

Kiểm định D6 tại `.agents/workflow-runs/20260915-1548-optimize-harness-workflow-design/governance-review.md` ban đầu nêu năm finding `Major`. Sau khi tất cả được chấp nhận và sửa, cùng reviewer độc lập xác nhận năm finding `Resolved`, không còn `Blocker`/`Major` và kết luận `Pass` cho chuẩn `Proposed`. `Active` vẫn là `Not verified` vì chưa có controlled trial thật.

## Điều kiện xem xét lại

- Controlled trial đầu tiên cho thấy bộ hồ sơ hoặc cổng tạo chi phí lớn hơn lợi ích.
- Metric không phân biệt được cải thiện thật với biến thiên của mô hình hoặc môi trường.
- Rollback, tính độc lập hay quyền sở hữu tệp không thể chứng minh trong runtime thực tế.
- Xuất hiện nhu cầu thay đổi ranh giới với workflow nội dung hoặc kiến trúc giáo trình.
- Chỉ cân nhắc `Active` sau khi đạt đầy đủ mục 11 của workflow và có quyết định mới của Chủ sở hữu.
