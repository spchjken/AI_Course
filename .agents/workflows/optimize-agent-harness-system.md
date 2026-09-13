# Khung quy trình tối ưu hệ thống harness tác nhân

- **Trạng thái:** `Proposed` — chỉ được chạy thử có kiểm soát khi Chủ sở hữu kho cho phép.
- **Mục tiêu:** Cải thiện độ tin cậy, an toàn, khả năng truy vết, khả năng sử dụng và chi phí/thời gian vận hành của hệ thống hướng dẫn và điều phối tác nhân, dựa trên bằng chứng vận hành.
- **Đầu vào dự kiến:** Bằng chứng từ lượt chạy, phản hồi của người dùng hoặc người vận hành, lỗi lặp lại, tình huống mơ hồ, và thay đổi của môi trường công cụ.
- **Bàn giao dự kiến:** Một đề xuất thay đổi có phạm vi, hồ sơ quyết định, kế hoạch chạy thử có kiểm soát và điều kiện hoàn tác; các sửa đổi chuẩn chỉ được thực hiện sau quyết định phù hợp.

Ghi chú tại [`design-notes/optimize-agent-harness-system.md`](design-notes/optimize-agent-harness-system.md) chỉ giữ bối cảnh; đặc tả dưới đây là nguồn vận hành.

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

Chuỗi trên được cụ thể hóa ở các giai đoạn dưới đây và chỉ chạy sau một lệnh cho phép pilot/controlled trial tường minh của Chủ sở hữu.

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

## Thực thi khi được cho phép

### A — Intake, baseline và thiết kế thử

Chỉ mở lượt khi có lỗi lặp lại qua hai lượt đối chiếu được, một sự cố `High`/`Critical`, thay đổi môi trường làm hướng dẫn không khả thi, metric đã chốt vượt ngưỡng, hoặc yêu cầu khảo sát của Chủ sở hữu. Điều phối viên ghi mệnh đề kiểm tra được, evidence thuận/nghịch, dữ liệu cấm ghi, full SHA, nhánh đích và worktree riêng. Không cô lập được Git thì `Baseline not verified` và dừng.

Tái hiện bằng dữ liệu không nhạy cảm; nếu không tái hiện được, ghi giới hạn. Tạo baseline, nguyên nhân cạnh tranh, phương án giữ nguyên, thay đổi nhỏ nhất, impact map, rollback và `trial-contract.md`. Hợp đồng khóa scope/tệp, metric/ngưỡng, kiểm tra âm, điều kiện dừng, authority và thời hạn. Mỗi tệp có nhãn `Update`, `Reverify`, `Invalidate`, `No change` hoặc `Not verified` cùng chủ sở hữu. Rules hay thay đổi liên workflow/skill/quyền hạn phải có decision record.

### B — Cổng quyết định và áp dụng tạm thời

Chủ sở hữu chọn `Reject`, `Defer`, `Revise` hoặc `Approve trial`; im lặng không là chấp thuận. Chỉ `Approve trial` cho phép sửa đúng tệp đã duyệt trên nhánh `codex/<run-id>`; mỗi áp dụng/sửa finding là commit hẹp. Metadata, chỉ mục và context package chỉ pilot ở nút định tuyến hẹp; không di trú toàn kho hay xây RAG/graph chỉ vì có sẵn công cụ.

`validation-report.md` phải có lệnh, phiên bản, output và bốn lớp: positive, negative (chặn suy đoán/vượt quyền/bỏ cổng), regression và comparison trên cùng kịch bản trước–sau. Không đổi bộ kiểm tra hay ngưỡng sau khi biết kết quả.

### C — Review, phân xử và áp dụng

Reviewer quản trị độc lập đọc trực tiếp nguồn, decision record, trial contract, diff, impact map và báo cáo kiểm tra. `Pass` chỉ khi contract đạt, không còn `Blocker`/`Major`, rollback khả thi và tính độc lập được chứng minh.

Áp dụng mục 6.4–6.5 của [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). Người thực hiện phản hồi append-only; chỉ `Accept` mới cho sửa cục bộ. Người phân tích ảnh hưởng là phía thứ ba của `Out of scope`, cần hai trong ba xác nhận. `High`/`Critical`, phản đối của reviewer, tranh chấp dữ kiện hoặc `Not verified` đã cạn đường kiểm tra chuyển `Awaiting adjudication`; tranh chấp dữ kiện dùng Evidence adjudicator mới, độc lập. Tối đa hai vòng sửa một finding.

Sau `Pass`, Chủ sở hữu chọn `Ratify`, `Revise`, `Reject` hoặc `Defer`. Chỉ `Ratify` cho phép tích hợp đúng commit đã kiểm định, migration và làm mất hiệu lực evidence cũ có chọn lọc. Trước tích hợp, `Reject`/`Defer` giữ nhánh đích nguyên trạng; sau tích hợp chỉ rollback bằng commit mới đảo đúng phạm vi, không `reset --hard`.

## Điều kiện đóng

Lượt chỉ đóng khi quyết định Chủ sở hữu, baseline/commit/phạm vi, disposition mọi finding, review độc lập, metric thuộc trial contract, migration/handoff và vòng đời tác nhân (nếu có) đều truy vết được. `Not verified` và `Independent review not verified` không thể tự thành `Pass`.
