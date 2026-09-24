# Giáo trình AI-native Builder

Kho dự án này chứa kế hoạch, kiến trúc và nội dung nguồn cho chương trình AI-native Builder dành cho người mới bắt đầu xây dựng sản phẩm cùng AI.

## Bắt đầu đọc từ đâu

1. [`AI-native-builder-curriculum-plan.md`](AI-native-builder-curriculum-plan.md) nêu mục đích, đối tượng, phạm vi và đầu ra của chương trình.
2. [`curriculum-content-architecture.md`](curriculum-content-architecture.md) xác định mục tiêu học tập, ranh giới năng lực và quan hệ phụ thuộc.
3. [`ai-native-builder/curriculum-map.md`](ai-native-builder/curriculum-map.md) trình bày thứ tự vận hành và liên kết điều hướng giữa các mục tiêu.
4. [`ai-native-builder/README.md`](ai-native-builder/README.md) dẫn tới bài học, lộ trình học và hồ sơ dạy thử.

## Làm việc với Codex hoặc tác nhân AI

Đọc [`AGENTS.md`](AGENTS.md) trước khi yêu cầu tác nhân tạo, sửa, kiểm định hoặc điều phối nội dung. Tệp này xác định cách chọn kỹ năng và quy trình, thứ tự đọc nguồn chuẩn, các bất biến vận hành và yêu cầu lưu bằng chứng.

Các quy tắc chi tiết vẫn thuộc về [hệ thống quy tắc](.agents/rules/README.md); `AGENTS.md` chỉ là điểm vào ngắn gọn, không phải bản sao của chúng.

## Hệ thống quy tắc

| Quy tắc | Trách nhiệm |
|---|---|
| [`curriculum-contract.md`](.agents/rules/curriculum-contract.md) | Nguồn chuẩn có thẩm quyền, quan hệ phụ thuộc, đơn vị nội dung và cấu trúc kho dự án. |
| [`glossary.md`](.agents/rules/glossary.md) | Nghĩa chuẩn và cách dùng tiếng Việt của thuật ngữ trong toàn hệ thống. |
| [`authoring-standard.md`](.agents/rules/authoring-standard.md) | Tiêu chuẩn bắt buộc khi viết bài học, hoạt động, sản phẩm trung gian hoặc tài liệu giảng viên. |
| [`quality-gates.md`](.agents/rules/quality-gates.md) | Các cổng bắt buộc, điểm chất lượng và trạng thái từ `Needs revision` đến `Validated`. |
| [`safety-and-currency.md`](.agents/rules/safety-and-currency.md) | Dữ liệu, thông tin xác thực, quyền hạn, hoàn tác và thông tin thay đổi theo thời gian. |

Yêu cầu mới nhất và rõ ràng của người dùng có ưu tiên cao nhất đối với mục tiêu, phạm vi, lựa chọn ưu tiên và quyết định sản phẩm. Điều đó không tự biến một khẳng định thực tế thành đúng. Khi có xung đột có thể làm thay đổi kết quả, phải áp dụng quy trình suy luận–kiểm chứng trong `.agents/rules/README.md`, giải quyết xung đột rồi mới triển khai phần phụ thuộc vào quyết định đó.

## Các kỹ năng chính

Kỹ năng là hướng dẫn thực hiện công việc chuyên biệt trong phạm vi hẹp. Danh mục dưới đây giúp người đọc nhận biết khả năng có sẵn; cách gọi, giới hạn phạm vi và cách kết hợp kỹ năng thuộc [`AGENTS.md`](AGENTS.md).

| Cú pháp gọi | Dùng khi |
|---|---|
| `$curriculum-goal-design` | Tạo, phân rã, sắp xếp hoặc thay đổi mục tiêu học tập và quan hệ phụ thuộc. |
| `$curriculum-reference-research` | Khảo sát tiền lệ giáo trình, nghiên cứu và nguồn chính thức trước khi soạn; kiểm chứng các claim trọng yếu hoặc dễ lỗi thời. |
| `$lesson-authoring` | Tạo hoặc sửa một bài học thuộc `goals/gNN-*`. |
| `$learner-artifact-design` | Thiết kế sản phẩm trung gian do học viên tạo. |
| `$assessment-design` | Thiết kế bảng tiêu chí, điểm kiểm tra và phản hồi đánh giá học viên. |
| `$learning-path-composition` | Ghép bài học thành chương trình thực hành ngắn hoặc lộ trình 1-1. |
| `$curriculum-quality-review` | Kiểm định bài học, chuỗi mục tiêu hoặc lộ trình theo tiêu chuẩn chất lượng. |
| `$pilot-feedback-analysis` | Phân tích đợt dạy thử để đề xuất cải tiến dựa trên bằng chứng. |
| `$harness-improvement-discovery` | Rà soát mở bằng chứng vận hành để tìm vấn đề harness và tạo candidate tương thích với workflow kiểm chứng; không tự sửa harness. |
| `$workflow-orchestration` | Chạy quy trình nhiều vai trò, phân công tác nhân động và lưu bằng chứng thực thi. |
| `$repo-skill-creator` | Tạo hoặc cập nhật kỹ năng cục bộ được ghim phiên bản trong kho dự án. |

Xem nội dung và điều kiện dùng từng kỹ năng trong [`.agents/skills/`](.agents/skills/).

## Các quy trình chính

| Quy trình | Dùng khi | Trạng thái hiện tại |
|---|---|---|
| [`complete-goal-lessons.md`](.agents/workflows/complete-goal-lessons.md) | Hoàn thiện một mục tiêu `gNN` thành bộ bài học có thể dạy thử; đang hoàn thiện cơ chế nghiên cứu nguồn bên ngoài. | `Proposed` |
| [`compose-learning-run.md`](.agents/workflows/compose-learning-run.md) | Ghép các bài học chuẩn thành một lộ trình học. | `Active` |
| [`pilot-and-validate.md`](.agents/workflows/pilot-and-validate.md) | Dạy thử, phân tích bằng chứng thực tế và xác nhận chất lượng. | `Proposed` |
| [`change-curriculum-architecture.md`](.agents/workflows/change-curriculum-architecture.md) | Thay đổi mục tiêu, quan hệ phụ thuộc hoặc cam kết cấp giáo trình. | `Proposed` *(đã chạy thử; chờ quyết định)* |
| [`refresh-volatile-content.md`](.agents/workflows/refresh-volatile-content.md) | Rà soát thông tin phụ thuộc công cụ, API, quyền hạn hoặc chính sách. | `Proposed` |
| [`validate-agent-harness-improvement.md`](.agents/workflows/validate-agent-harness-improvement.md) | Kiểm chứng và triển khai có kiểm soát một cải tiến candidate đối với rules, skills, workflows hoặc điều phối tác nhân. | `Proposed` |

Đọc [kiến trúc và ranh giới giữa các quy trình](.agents/workflows/README.md) trước khi thực hiện công việc nhiều giai đoạn hoặc cần bàn giao giữa nhiều vai trò.

## Vai trò của tài liệu trong thư mục con

- `README.md` trong `goals/gNN-*`: bản định hướng thiết kế chuẩn của từng bài học.
- `README.md` trong `runs/`: hợp đồng hoặc kiểm kê của từng lộ trình học.
- `README.md` trong `pilots/`: cách tổ chức hồ sơ dạy thử đã ẩn danh.
- `README.md` trong `.agents/rules/` và `.agents/workflows/`: chỉ mục của hệ thống quy tắc và quy trình tương ứng.

Hiện không dùng `AGENTS.md` lồng nhau: các thư mục con đều đã có vai trò tài liệu rõ ràng nhưng chưa có chỉ dẫn vận hành cục bộ cần được ưu tiên hơn chỉ dẫn ở gốc. Khi xuất hiện ngoại lệ thực sự, chỉ dẫn đó sẽ được đặt trong `AGENTS.md` gần phạm vi áp dụng.
