# Đồng bộ workflow hoàn thiện bài học với template chuẩn

- Ngày: 2026-09-16
- Trạng thái: Đã chấp thuận (`Ratified`)
- Bên quyết định: Chủ sở hữu kho — quyết định tường minh `Ratify` ngày 2026-09-16
- Phạm vi ảnh hưởng: `.agents/workflows/complete-goal-lessons.md`, `.agents/workflows/README.md`, hồ sơ run tương ứng, derived index
- Thay thế hồ sơ: Không có
- Run: `.agents/workflow-runs/20260916-1627-complete-goal-lessons-template/`
- Kiểm định cuối: `Pass` — reviewer độc lập xác nhận không còn `Major`

## Bối cảnh và xung đột

`complete-goal-lessons.md` được hoàn thiện sớm hơn các workflow còn lại nên vẫn
dùng cấu trúc cũ: thiếu phép thử kích hoạt, hai chế độ thực hiện, mô hình trạng
thái ở cấp run, bảng trách nhiệm, cổng kiểm chứng, rollback, hợp đồng giao việc
chuẩn hóa và điều kiện đóng/chuyển trạng thái. Phần đặc tả nội dung đã có giá trị
nhưng các tiêu đề cấp cao và tham chiếu nội bộ không còn đồng nhất với template
đang dùng trong các workflow mới hơn.

## Các phương án đã cân nhắc

1. Giữ nguyên cấu trúc cũ và chỉ sửa từng chỗ khi chạy thực tế.
2. Viết lại toàn bộ, có nguy cơ làm mất đặc tả soạn bài đã được dùng.
3. Thêm lớp template chuẩn ở đầu workflow, giữ đặc tả cũ trong Phụ lục A,
   sửa các tham chiếu bị lệch và kiểm định độc lập. Đây là phương án đang triển khai.

## Bằng chứng thuận và nghịch

- Các workflow chuẩn hơn đều có cùng nhóm cổng: kích hoạt, đầu vào/đầu ra,
  vai trò, giai đoạn, kiểm chứng, xử lý thất bại, hợp đồng tác nhân và đóng run.
- Đặc tả cũ chứa nhiều quy tắc chuyên môn chi tiết; giữ chúng trong Phụ lục A
  giảm rủi ro tạo nguồn chuẩn thứ hai hoặc làm mất hành vi đã được duyệt.
- Việc thêm lớp template tăng số mục đọc, nhưng làm rõ ranh giới run, phase,
  quality state và quyền reviewer.
- Review quản trị độc lập ban đầu là `Pass-with-findings`; W3 xác nhận các sửa
  chính; W4 kết luận `Pass` và không còn `Major`.

## Quyết định

- Chuẩn hóa `complete-goal-lessons.md` theo template chung mà không đổi phạm vi
  xây bài học, quyền sở hữu nguồn chuẩn hoặc quy trình cấp `Validated`.
- Đồng bộ nhãn workflow về `Proposed` theo quyết định cổng nghiên cứu nguồn bên
  ngoài đã có; thay đổi này không phải là một lần chuyển sang `Active`.
- Giữ phần đặc tả triển khai hiện có trong Phụ lục A và sửa các tham chiếu cũ
  để không trỏ nhầm vào các mục cấp cao mới.
- Bắt buộc kiểm định độc lập, kiểm tra liên kết/cấu trúc và cập nhật derived index
  trước khi đóng run hoặc xem thay đổi là chuẩn vận hành.

### Phê chuẩn của Chủ sở hữu

Chủ sở hữu kho đã quyết định `Ratify` bản sửa này. Việc ratify phê chuẩn lớp
template, các rào chắn, hồ sơ governance và sự đồng bộ registry được ghi ở trên.
Nó không chuyển `complete-goal-lessons` sang `Active`, không cấp `Validated`,
không thay đổi nguồn chuẩn giáo trình và không mở rộng phạm vi của workflow.

## Hệ quả và phạm vi chuyển đổi

- Tác nhân chạy workflow sẽ có một hợp đồng đọc thống nhất trước khi đi vào
  hướng dẫn soạn bài chi tiết.
- Không có bài học hoặc mục tiêu nào được coi là đã hoàn thành chỉ vì workflow
  được sửa cấu trúc.
- Run evidence và decision record này là hồ sơ quản trị; workflow vẫn là nguồn
  vận hành duy nhất.

## Điều kiện xem xét lại

- Reviewer phát hiện thay đổi ngữ nghĩa ngoài phạm vi hoặc tham chiếu không phân
  giải được.
- Một workflow peer đổi template chung khiến phần đầu chuẩn hóa không còn đồng bộ.
- Lượt chạy thực tế cho thấy hai chế độ, trạng thái, rollback hoặc hợp đồng giao
  việc không đủ để điều phối một mục tiêu mà không mở rộng phạm vi.
