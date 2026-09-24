# Hệ thống quy trình xây dựng giáo trình

Thư mục này chứa các quy trình điều phối nhiều giai đoạn, kỹ năng, vai trò và lượt bàn giao để đưa giáo trình từ nguồn chuẩn tới nội dung có thể dạy, kiểm chứng và bảo trì.

## Phân biệt quy tắc, kỹ năng và quy trình

- `rules/` quy định điều không được vi phạm và tiêu chuẩn nghiệm thu.
- `skills/` hướng dẫn thực hiện một loại công việc chuyên biệt trong phạm vi hẹp.
- `workflows/` điều phối nhiều kỹ năng hoặc vai trò theo thứ tự, quản lý trạng thái và chuyển sản phẩm trung gian giữa các giai đoạn để hoàn thành một kết quả lớn.

Không tạo quy trình chỉ để bọc một kỹ năng. Chỉ cần quy trình khi công việc có nhiều giai đoạn, nhánh quyết định, điểm dừng hoặc lượt bàn giao bền vững giữa nhiều tác nhân AI.

Quy trình không thay thế quy tắc hay kỹ năng, không sao chép nội dung bài học và không tạo thêm nguồn chuẩn cho mục tiêu. Khi có xung đột ảnh hưởng kết quả, áp dụng `.agents/rules/README.md`, ghi hồ sơ quyết định phù hợp và chỉ quay lại quy trình sau khi tiền đề đã được giải quyết.

## Cơ chế điều phối tác nhân dùng chung

Mọi quy trình nhiều vai trò phải dùng [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md) và gọi `$workflow-orchestration` khi thực thi. Từng quy trình quy định trách nhiệm và ràng buộc chuyên môn; giao thức dùng chung quyết định tại thời điểm chạy nên tự làm, tái sử dụng tác nhân, sinh tác nhân mới hay chờ đầu vào.

Sơ đồ tác nhân trong từng quy trình là cấu trúc gợi ý, không phải lệnh sinh tác nhân cố định. Điều phối viên phải chạy cổng phân công trước mỗi đơn vị công việc và lưu bằng chứng vòng đời tác nhân trong `.agents/workflow-runs/<run-id>/orchestration-log.md`.

Không công nhận việc tách tác nhân chỉ dựa trên tên vai trò hoặc lời tự nhận. Cổng kiểm định độc lập chỉ đạt khi hồ sơ thực thi chứng minh Người kiểm định có định danh mới do công cụ điều phối trả về, không tham gia tạo hoặc sửa đầu ra và đã đọc trực tiếp nguồn cần kiểm tra.

## Thành phần điều phối dùng chung

| Thành phần | Trạng thái | Chức năng |
|---|---|---|
| [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md) | `Active` | Quyết định tự làm, tái sử dụng, sinh, trì hoãn, kiểm chứng tác nhân, phản biện và phân xử finding trọng yếu tại thời điểm chạy. |
| [`workflow-runs/`](../workflow-runs/README.md) | Hồ sơ vận hành | Lưu sổ đăng ký và bằng chứng thực thi; không phải nguồn chuẩn hay hồ sơ quyết định. |
| [`$workflow-orchestration`](../skills/workflow-orchestration/SKILL.md) | Có thể gọi | Áp dụng giao thức phân công khi thực thi một quy trình nhiều vai trò. |

Phép thử ngày 2026-09-05 xác nhận rằng tiện ích Codex khi đó thực sự sinh được tác nhân con và trả tên nhiệm vụ chuẩn làm định danh. Giao thức sau đó đã được người dùng duyệt `Active`; tuy vậy, từng workflow vẫn phải ghi `Independent review not verified` nếu lượt chạy cụ thể không chứng minh được tính độc lập, và phải dùng mục 6.4 của giao thức khi có finding trọng yếu.

## Trạng thái của quy trình

| Trạng thái | Ý nghĩa | Có được thực thi không |
|---|---|---|
| `Placeholder` | Mới xác định mục đích, ranh giới và bàn giao; chưa có đầy đủ giai đoạn và điều kiện kết thúc. | Không. Chỉ dùng để định tuyến và thiết kế tiếp. |
| `Proposed` | Đã đủ chi tiết để kiểm định hoặc chạy thử có kiểm soát. | Chỉ khi người dùng cho phép; không tự động xử lý hàng loạt. |
| `Active` | Đã được duyệt, có đặc tả đầu vào/đầu ra và rào chắn đủ dùng. | Có, trong đúng phạm vi được mô tả. |
| `Deprecated` | Không còn là đường thực thi chuẩn. | Không. Phải trỏ tới quy trình thay thế. |

Trạng thái của quy trình khác với trạng thái chất lượng giáo trình (`Needs revision`, `Pilot-ready`, `Release-ready`, `Validated`). Trạng thái toàn lượt thực thi là `Queued`, `In progress`, `Awaiting decision` hoặc `Closed`; trạng thái của một tác nhân hay đơn vị công việc là `queued`, `running`, `completed`, `failed`, `cancelled` hoặc `not-verified`. Không dùng trạng thái hoàn thành của một tác nhân con để suy ra toàn bộ quy trình đã hoàn thành.

Từ “lộ trình” dùng cho chương trình được ghép từ các bài học, không dùng để chỉ một lượt thực thi quy trình.

## Kiến trúc tổng thể

```text
CANONICAL SOURCES
Program plan → Content architecture → Curriculum map → Goal design briefs
                                          │
                                          ├──→ complete-goal-lessons
                                          │          │
                                          │          └──→ Reviewed lesson package
                                          │                     │
                                          │                     ├──→ pilot-and-validate
                                          │                     │     (single-lesson pilot)
                                          │                     │
                                          │                     └──→ compose-learning-run
                                          │                                │
                                          │                                └──→ pilot-and-validate
                                          │                                      (learning-run pilot)
                                          │
                                          └──→ compose-learning-run
                                               (early run design from goal contracts)
```

Luồng xây dựng chính bắt đầu từ các nguồn chuẩn hiện có, không bắt đầu từ một yêu cầu thay đổi. `compose-learning-run` có thể phác thảo lịch và quan hệ phụ thuộc từ đặc tả mục tiêu trước khi mọi bài học hoàn thiện; chỉ được dạy thử lộ trình khi các bài học bắt buộc đạt tối thiểu `Pilot-ready`. Một bài học cũng có thể được dạy thử độc lập mà chưa cần lộ trình hoàn chỉnh.

Hai quy trình dưới đây là vòng phản hồi có điều kiện, không nằm trên đường xây dựng bắt buộc:

```text
Architecture-affecting finding
    → change-curriculum-architecture
    → Update canonical sources
    → Route to affected workflow
```

```text
Volatile claim reaches its recheck trigger
    → refresh-volatile-content
    → No change or route to owning workflow
```

```text
Owner-requested audit or harness operating evidence
    → $harness-improvement-discovery
    → Zero or more workflow-ready candidates
    → validate-agent-harness-improvement (Proposed)
    → Run a human-approved controlled trial; do not auto-apply
```

Thay đổi cục bộ trong bài học không cần đi qua `change-curriculum-architecture`. Chỉ chuyển sang quy trình đó khi phát hiện thực sự làm thay đổi ranh giới mục tiêu, quan hệ phụ thuộc, cam kết của chương trình hoặc nguồn chuẩn cấp cao hơn.

## Danh mục quy trình

| Quy trình | Trạng thái | Khi dùng | Đầu ra hoặc bàn giao chính |
|---|---|---|---|
| [`complete-goal-lessons.md`](complete-goal-lessons.md) | `Proposed` | Biến bản định hướng của một `gNN` thành bộ tài liệu bài học đã được kiểm định độc lập, có khảo sát nguồn ngoài và phân xử finding trọng yếu; chờ hoàn tất cổng nghiên cứu nguồn bên ngoài. | `Pilot-ready` hoặc `Release-ready`, kèm sản phẩm trung gian và bản bàn giao cho dạy thử. |
| [`compose-learning-run.md`](compose-learning-run.md) | `Active` | Ghép mục tiêu và bài học chuẩn thành chương trình thực hành ngắn, lộ trình 1-1 hoặc khóa đầy đủ. | Hợp đồng lộ trình, lịch, ma trận bao phủ, mức sẵn sàng, kiểm định độc lập và bàn giao dạy thử. |
| [`pilot-and-validate.md`](pilot-and-validate.md) | `Proposed` | Dạy thử bài học hoặc lộ trình đã đạt tối thiểu `Pilot-ready` và phân tích bằng chứng thực tế. | Hồ sơ dạy thử ẩn danh, phân tích nguyên nhân, quyết định của chủ sở hữu, trạng thái chất lượng có phạm vi và bàn giao sửa đổi. |
| [`change-curriculum-architecture.md`](change-curriculum-architecture.md) | `Proposed` *(đã chạy thử; chờ quyết định)* | Thay đổi mục tiêu, quan hệ phụ thuộc, cam kết hoặc ranh giới cấp giáo trình. | Quyết định được ghi, nguồn chuẩn được đồng bộ, ảnh hưởng được kiểm định và chuyển tới quy trình sở hữu. |
| [`refresh-volatile-content.md`](refresh-volatile-content.md) | `Proposed` | Rà soát khẳng định phụ thuộc công cụ, API, mô hình, giá, quyền hạn hoặc chính sách. | Hàng đợi dẫn xuất, sổ bằng chứng cập nhật, bản đồ ảnh hưởng, cờ chặn an toàn và bàn giao tới quy trình sở hữu. |
| [`validate-agent-harness-improvement.md`](validate-agent-harness-improvement.md) | `Proposed` | Kiểm chứng và chạy thử có kiểm soát một candidate cải tiến đã có vấn đề kiểm tra được; không dùng để audit mở hoặc tự phát hiện vấn đề. | Thay đổi được kiểm định quản trị, có rollback và chỉ áp dụng sau `Ratify` của Chủ sở hữu. |

## Ranh giới trách nhiệm

### Xây bài học và chuẩn bị dạy thử

`complete-goal-lessons` tạo tài liệu bài học, phần đánh giá năng lực, công cụ thu phản hồi của học viên và kết quả kiểm định trước dạy thử. Quy trình này không tổ chức buổi dạy, không phân tích phản hồi thực tế và không cấp `Validated`.

### Ghép bài học thành chương trình dạy

`compose-learning-run` chỉ điều phối bài học chuẩn. Quy trình này không đổi định nghĩa mục tiêu và không sao chép phần giải thích, bài thực hành, bảng tiêu chí hoặc tài nguyên dùng chung vào `runs/`.

### Kiểm chứng qua dạy thử

`pilot-and-validate` kết hợp phản hồi của học viên, quan sát của giảng viên, sản phẩm của học viên và kết quả đánh giá năng lực. Quy trình này không coi mức hài lòng là bằng chứng duy nhất của kết quả và không tự áp dụng giả thuyết thay đổi chưa được chấp thuận.

### Thay đổi kiến trúc

`change-curriculum-architecture` chịu trách nhiệm cho thay đổi vượt khỏi một bài học: ranh giới hoặc mã mục tiêu, quan hệ phụ thuộc, cam kết chương trình hoặc thay đổi ảnh hưởng nhiều lộ trình. Thay đổi này cần hồ sơ quyết định và cổng quyết định của con người.

### Bảo trì thông tin dễ lỗi thời

`refresh-volatile-content` xác minh khẳng định và đánh giá ảnh hưởng. Quy trình này chuyển sửa đổi tới đúng tệp hoặc quy trình chịu trách nhiệm; không tự thay công cụ, mở rộng bài học hoặc đổi mục tiêu chỉ vì có lựa chọn mới hơn.

### Khám phá và kiểm chứng cải tiến harness tác nhân

`$harness-improvement-discovery` là skill đọc và phân tích bằng chứng để tìm candidate khi vấn đề hoặc giải pháp chưa rõ. Nó có thể trả về không hoặc nhiều candidate, không sửa harness và không tự mở trial.

`validate-agent-harness-improvement` là workflow `Proposed` nhận đúng một candidate `Ready` hoặc giả thuyết cụ thể do Chủ sở hữu chỉ định để kiểm chứng cải tiến `AGENTS.md`, rules, skills, workflows, giao thức phân công và tài sản vận hành. Nó chỉ chạy thử khi Chủ sở hữu cho phép, không tự thay nguồn chuẩn và không sở hữu thay đổi nội dung hoặc kiến trúc giáo trình.

## Quy tắc bàn giao chung

Mọi lượt bàn giao giữa các quy trình phải ghi:

1. Phiên bản nguồn và tệp chuẩn đã dùng.
2. Đầu ra hoặc sản phẩm trung gian được chuyển giao.
3. Trạng thái chất lượng hiện tại cùng người kiểm định và bằng chứng tương ứng.
4. Câu hỏi chưa giải quyết, giới hạn và kết quả `Not verified` còn lại.
5. Quy trình hoặc giai đoạn tiếp theo cùng điều kiện bắt đầu.
6. Phần bằng chứng cũ bị mất hiệu lực nếu đầu ra đã thay đổi.

Không bàn giao bằng trí nhớ hội thoại. Thông tin cần cho lượt sau phải nằm trong tệp chuẩn, kết quả kiểm định, hồ sơ quyết định hoặc hồ sơ thực thi do quy trình quy định.

## Chọn quy trình

- Hoàn thiện nội dung của một mục tiêu đã chốt → `complete-goal-lessons`.
- Lên lịch và ghép nhiều bài học → `compose-learning-run`.
- Chuẩn bị dạy thử hoặc đã dạy thử → `pilot-and-validate`.
- Thay đổi mục tiêu, quan hệ phụ thuộc hoặc cam kết → `change-curriculum-architecture`.
- Kiểm tra lại khẳng định về công cụ hoặc API → `refresh-volatile-content`.
- Chưa biết vấn đề harness nằm ở đâu hoặc muốn audit run định kỳ/theo yêu cầu → `$harness-improvement-discovery`.
- Đã có một candidate harness kiểm tra được → `validate-agent-harness-improvement` (`Proposed`; mỗi controlled trial cần Chủ sở hữu cho phép tường minh).

Nếu một tác vụ chạm nhiều quy trình, bắt đầu tại quy trình chịu trách nhiệm cho nguyên nhân gốc rồi bàn giao. Không gộp toàn bộ vòng đời vào một yêu cầu dành cho tác nhân AI nhẹ.

## Thứ tự hoàn thiện dự kiến

1. Hoàn thiện và chạy thử `complete-goal-lessons` trên một mục tiêu.
2. Thiết kế và chạy thử có kiểm soát `compose-learning-run` ở chế độ phác thảo sớm từ các bản định hướng mục tiêu; chỉ chạy chế độ đóng gói để dạy khi bài học bắt buộc đủ điều kiện.
3. Thiết kế và chạy thử có kiểm soát `pilot-and-validate` trước buổi dạy thử đầu tiên.
4. Chạy thử có kiểm soát `change-curriculum-architecture` khi xuất hiện thay đổi cấu trúc đầu tiên.
5. Thiết kế và chạy thử có kiểm soát `refresh-volatile-content` trước khi phát hành hoặc bắt đầu chu kỳ bảo trì.
6. Dùng `$harness-improvement-discovery` trên một tập run có mẫu tương phản, rồi chạy thử có kiểm soát `validate-agent-harness-improvement` trên đúng một candidate có baseline và rollback hẹp trước khi cân nhắc `Active`.

Tệp ở trạng thái `Placeholder` chỉ ghi ranh giới và yêu cầu thiết kế. Không tự bổ sung giai đoạn rồi thực thi khi chưa được người dùng duyệt.
