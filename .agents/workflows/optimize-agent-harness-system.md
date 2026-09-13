# Khung quy trình tối ưu hệ thống harness tác nhân

- **Trạng thái:** `Placeholder` — chưa được thực thi.
- **Mục tiêu:** Cải thiện độ tin cậy, an toàn, khả năng truy vết, khả năng sử dụng và chi phí/thời gian vận hành của hệ thống hướng dẫn và điều phối tác nhân, dựa trên bằng chứng vận hành.
- **Đầu vào dự kiến:** Bằng chứng từ lượt chạy, phản hồi của người dùng hoặc người vận hành, lỗi lặp lại, tình huống mơ hồ, và thay đổi của môi trường công cụ.
- **Bàn giao dự kiến:** Một đề xuất thay đổi có phạm vi, hồ sơ quyết định, kế hoạch chạy thử có kiểm soát và điều kiện hoàn tác; các sửa đổi chuẩn chỉ được thực hiện sau quyết định phù hợp.

Kế hoạch khung và các câu hỏi đang mở được lưu tại [`design-notes/optimize-agent-harness-system.md`](design-notes/optimize-agent-harness-system.md). Ghi chú đó không phải workflow và không cấp quyền thực thi.

## Ranh giới

Hệ thống harness trong quy trình này gồm `AGENTS.md`, `.agents/rules/`, `.agents/skills/`, `.agents/workflows/`, giao thức phân công tác nhân, biểu mẫu, script kiểm tra và hồ sơ vận hành liên quan.

Quy trình này không:

- Viết, thay thế hoặc tự phê duyệt nội dung bài học, mục tiêu học tập hay lộ trình học.
- Tự nâng trạng thái của kỹ năng, quy trình, cổng chất lượng hoặc tài liệu chuẩn.
- Thay đổi cấu hình tài khoản, quyền truy cập hay hệ thống bên ngoài kho nếu chưa có uỷ quyền riêng.
- Dùng một quan sát đơn lẻ hoặc trí nhớ hội thoại làm bằng chứng đủ để thay đổi quy tắc dùng chung.

Thay đổi làm ảnh hưởng ranh giới mục tiêu, quan hệ phụ thuộc hoặc cam kết chương trình vẫn phải chuyển sang `change-curriculum-architecture`. Thay đổi trong nội dung bài học vẫn thuộc quy trình hay kỹ năng sở hữu bài học đó.

## Khi cần định tuyến tới đây

Đây là điểm tập hợp để thiết kế cải tiến khi có một trong các dấu hiệu sau:

- Một lỗi, chỗ mơ hồ hoặc đường vòng trong harness lặp lại qua các lượt chạy.
- Quy tắc, kỹ năng, workflow hoặc giao thức phân công tạo ra kết quả không thể kiểm chứng, không an toàn, khó dùng, tốn kém hoặc chậm bất hợp lý.
- Công cụ hay môi trường chạy làm một hướng dẫn hiện có không còn khả thi.
- Người dùng yêu cầu xem xét cách các tác nhân được hướng dẫn, kiểm chứng hoặc điều phối.

Việc định tuyến không đồng nghĩa với việc thay đổi đã được chấp thuận.

## Bằng chứng tối thiểu cho một đề xuất tương lai

Mỗi vấn đề cần có hồ sơ bền vững, ít nhất ghi:

1. Tệp, quy tắc, kỹ năng hoặc workflow bị ảnh hưởng và phiên bản đã quan sát.
2. Hành vi kỳ vọng, hành vi thực tế và bằng chứng trực tiếp cho chênh lệch đó.
3. Phạm vi ảnh hưởng, mức độ rủi ro và khả năng tái hiện; phân biệt rõ phần chưa kiểm chứng.
4. Các giả thuyết cạnh tranh, gồm khả năng lỗi do đầu vào, điều phối, công cụ hoặc hướng dẫn.
5. Chủ sở hữu quyết định, các câu hỏi chưa giải quyết và điều kiện cần để kết luận.

Nhật ký trong `.agents/workflow-runs/` là bằng chứng vận hành, không tự trở thành nguồn chuẩn hay hồ sơ quyết định.

## Chuỗi thiết kế dự kiến

```text
Evidence intake
    → classify the issue and its scope
    → formulate competing hypotheses, impact, and rollback
    → human decision
    → controlled trial
    → independent governance review
    → activate, revise, or revert
```

Chuỗi trên chỉ là khung thiết kế, không phải các bước được phép chạy ở trạng thái `Placeholder`.

## Câu hỏi phải được chốt trước khi chuyển sang `Proposed`

- Tiêu chí khởi động, dừng, hủy và đánh giá một lượt tối ưu là gì?
- Ai sở hữu từng loại tệp; hồ sơ quyết định và nguồn chuẩn nào phải được cập nhật?
- Bằng chứng runtime nào được thu, lưu ở đâu, và giới hạn riêng tư hoặc an toàn của nó là gì?
- Cách chạy thử có kiểm soát, so sánh với đường cơ sở và hoàn tác thay đổi sẽ được xác định ra sao?
- Ai có thẩm quyền chấp thuận, và kiểm định quản trị độc lập diễn ra ở cổng nào?
- Finding của kiểm định được phản biện, phân xử và ghi `Not verified` theo mục 6.4 của `agent-dispatch-protocol.md` như thế nào; vai trò nào là phía thứ ba cho đánh giá `Out of scope`?
- Một thay đổi ảnh hưởng nhiều rules, skills hoặc workflows sẽ có kế hoạch di trú và kiểm chứng chéo thế nào?
- Ranh giới định tuyến tới `change-curriculum-architecture`, `complete-goal-lessons` và các quy trình nội dung khác được ghi nhận thế nào?

## Bàn giao khi khung được hoàn thiện

Một phiên bản `Proposed` trong tương lai phải nêu rõ đầu vào/đầu ra, các cổng quyết định của con người, chủ sở hữu tệp, bằng chứng kiểm thử, điều kiện rollback và kiểm định độc lập. Nếu kiểm định tạo finding trọng yếu, nó phải kế thừa mục 6.4 của `agent-dispatch-protocol.md`, không quay về mô hình reviewer đưa verdict một chiều. Khi thay đổi quy tắc, phải có hồ sơ trong `.agents/decisions/`, đánh giá phạm vi ảnh hưởng và kiểm định quản trị độc lập theo `AGENTS.md`. Khi thay đổi kỹ năng, phải dùng quy trình tạo/cập nhật kỹ năng của kho và chạy kiểm tra tương ứng. Khi thay đổi workflow, phải đồng bộ danh mục, trạng thái và các ranh giới trách nhiệm bị ảnh hưởng.

Không được bổ sung các giai đoạn thực thi hoặc chạy thử quy trình này cho tới khi người sở hữu chấp thuận phiên bản `Proposed`.
