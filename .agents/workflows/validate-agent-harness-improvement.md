# Quy trình kiểm chứng cải tiến harness tác nhân

- **Trạng thái:** `Proposed` — chỉ được chạy thử có kiểm soát khi Chủ sở hữu kho cho phép cho từng lượt.
- **Mục tiêu:** Kiểm chứng và triển khai có kiểm soát một cải tiến ứng viên đối với độ tin cậy, an toàn, khả năng truy vết, khả năng sử dụng hoặc chi phí/thời gian vận hành của harness tác nhân.
- **Đầu vào tối thiểu:** Một `candidate issue` kiểm tra được, bằng chứng trực tiếp hoặc giả thuyết cụ thể do Chủ sở hữu chỉ định, phạm vi harness nghi vấn và người có quyền quyết định.
- **Đầu ra bắt buộc:** Hồ sơ chẩn đoán, baseline, hợp đồng thử, thay đổi cô lập, báo cáo kiểm chứng, kiểm định quản trị độc lập, quyết định cuối và kế hoạch tích hợp/hoàn tác có thể truy vết.

Ghi chú tại [`design-notes/validate-agent-harness-improvement.md`](design-notes/validate-agent-harness-improvement.md) lưu bối cảnh thiết kế lịch sử dưới tên cũ; tệp này là nguồn vận hành duy nhất của quy trình.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Chỉ mở một lượt khi có ít nhất một điều kiện sau:

1. Cùng một lỗi, chỗ mơ hồ hoặc đường vòng xuất hiện trong ít nhất hai lượt chạy có thể đối chiếu.
2. Một sự cố đơn lẻ mức `High` hoặc `Critical` gây mất an toàn, vượt quyền, mất dữ liệu, sai nguồn chuẩn hoặc làm phán quyết không thể kiểm chứng.
3. Môi trường, công cụ hoặc cơ chế điều phối thay đổi khiến hướng dẫn hiện tại không còn khả thi.
4. Một metric xác định trước vượt ngưỡng cảnh báo trong phạm vi có dữ liệu đủ tin cậy.
5. Chủ sở hữu chỉ định một giả thuyết cải tiến cụ thể có hành vi kỳ vọng và quan sát được.

Yêu cầu rà soát chung, một quan sát đơn lẻ dưới mức `High`, sở thích văn phong hoặc ý tưởng dùng công nghệ mới không tự đủ để mở workflow. Dùng `$harness-improvement-discovery` cho khám phá mở; chỉ bàn giao từng candidate `Ready` vào đây. Các quan sát còn lại có thể được ghi để theo dõi hoặc đóng với `No change`.

### 1.2. Đơn vị thay đổi

Một lượt chỉ sở hữu một vấn đề gốc và tập tệp có đường ảnh hưởng trực tiếp. Phạm vi hợp lệ gồm `AGENTS.md`, `.agents/rules/`, `.agents/skills/`, `.agents/workflows/`, giao thức điều phối, script, template, schema và tài sản vận hành hỗ trợ harness.

Nếu hai vấn đề không dùng cùng mệnh đề, metric, chủ sở hữu và rollback, tách thành hai lượt. Không gộp dọn tài liệu hay tái cấu trúc không liên quan vào trial.

### 1.3. Định tuyến khi không thuộc phạm vi

| Phát hiện | Nơi nhận |
|---|---|
| Đổi ranh giới mục tiêu, phụ thuộc hoặc cam kết chương trình | `change-curriculum-architecture` |
| Sửa bài học theo mục tiêu đã chốt | `complete-goal-lessons` hoặc kỹ năng sở hữu |
| Ghép hoặc sửa lịch chương trình dạy | `compose-learning-run` |
| Khẳng định công cụ, API, giá, quyền hạn hay chính sách lỗi thời | `refresh-volatile-content` |
| Lỗi runtime/tài khoản ngoài kho | Chủ sở hữu hệ thống ngoài; cần uỷ quyền riêng |

Workflow có thể ghi finding và impact map cho phần ngoài phạm vi, nhưng không tự nhận quyền sửa phần đó.

## 2. Hai chế độ thực hiện

### 2.1. `Incident containment`

Dùng cho sự cố `High`/`Critical` đang tạo rủi ro. Được phép đề xuất biện pháp chặn hẹp, có expiry và rollback trước khi tối ưu dài hạn; vẫn cần phê duyệt của Chủ sở hữu trước khi áp dụng. Chế độ này không bỏ qua chẩn đoán, kiểm định độc lập hay `Ratify` trước tích hợp chuẩn.

### 2.2. `Improvement trial`

Dùng cho độ tin cậy, khả năng sử dụng, chi phí hoặc thời gian. Phải có baseline, phương án `No change`, thay đổi nhỏ nhất và so sánh trước–sau trên cùng kịch bản. Một tác vụ duy nhất không đủ để tuyên bố cải thiện chung.

## 3. Sơ đồ tổng thể và trạng thái

```text
Ready candidate or owner-nominated testable hypothesis
  → Intake and trigger gate
  → Reproduce and establish baseline
  → Competing hypotheses and options
  → Impact, privacy and rollback design
  → OWNER GATE: Reject | Defer | Revise | Approve trial
  → Isolated implementation
  → Positive + negative + regression + comparison tests
  → Independent governance review
  → Finding disposition and adjudication when needed
  → OWNER GATE: Ratify | Revise | Reject | Defer
  → Integrate or retain/revert trial
  → Selective invalidation, migration and handoff
```

Trạng thái toàn lượt chỉ là `Queued`, `In progress`, `Awaiting decision` hoặc `Closed` theo danh mục workflow. `Awaiting trial approval` và `Awaiting ratification` là giá trị của trường quyết định khi toàn lượt đang ở `Awaiting decision`, không phải trạng thái toàn lượt mới. Kết quả đóng hợp lệ là `Ratified`, `Rejected`, `Deferred`, `No change`, `Rolled back` hoặc `Failed`. `Not verified` không phải kết quả thành công và không tự thành `Pass` theo thời gian.

## 4. Đầu vào, hồ sơ và quyền sở hữu

### 4.1. Đầu vào tối thiểu

- mệnh đề vấn đề kiểm tra được;
- hành vi kỳ vọng và hành vi quan sát được;
- bằng chứng trực tiếp, hoặc nhãn `Owner-nominated hypothesis` cho một giả thuyết cụ thể;
- phạm vi tệp/thành phần nghi vấn;
- mức tác động ban đầu và dữ liệu cấm thu;
- Chủ sở hữu có quyền phê duyệt trial và ratify.

Giả thuyết cụ thể do Chủ sở hữu chỉ định có thể bắt đầu khi bằng chứng còn ít, nhưng phải có hành vi kỳ vọng/quan sát phân biệt được; kết quả giữ nhãn giả thuyết và không được suy ra tần suất hay tác động chưa đo. Yêu cầu “rà soát các run để tìm cơ hội cải tiến” thuộc `$harness-improvement-discovery`, không phải đầu vào trực tiếp của workflow này.

Một candidate `Ready` do `$harness-improvement-discovery` tạo tương thích trực tiếp với đầu vào trên. `Confidence`, `Counterevidence` và `Competing explanations` được giữ làm bối cảnh chẩn đoán, không thay thế tái hiện, baseline hoặc cổng trial.

### 4.2. Hồ sơ bắt buộc của lượt chạy

Mỗi lượt dùng `.agents/workflow-runs/<run-id>/` với tên `<YYYYMMDD-HHMM>-validate-harness-<scope>`:

| Tệp | Nội dung | Bên ghi chính |
|---|---|---|
| `orchestration-log.md` | Phân công và vòng đời tác nhân | Điều phối viên |
| `evidence-intake.md` | Mệnh đề, bằng chứng thuận/nghịch, mức độ, riêng tư | Người phân tích bằng chứng |
| `git-baseline.md` | Full SHA, nhánh đích, vùng cô lập, dirty-state và drift | Điều phối viên |
| `hypothesis-and-options.md` | Nguyên nhân cạnh tranh, `No change`, phương án nhỏ nhất | Người chẩn đoán |
| `impact-map.md` | Tệp, chủ sở hữu và nhãn ảnh hưởng | Người phân tích ảnh hưởng |
| `trial-contract.md` | Scope, metric, ngưỡng, test, quyền, stop condition, timebox | Điều phối viên; Chủ sở hữu duyệt |
| `implementation-log.md` | Commit, tệp sửa, sai lệch contract, tự kiểm tra | Người thực hiện |
| `validation-report.md` | Positive, negative, regression và comparison | Người kiểm chứng |
| `governance-review.md` | Kết luận độc lập và giới hạn | Người kiểm định độc lập |
| `review-findings.md` | Finding do reviewer sở hữu | Người kiểm định độc lập |
| `finding-disposition.md` | Phản hồi append-only và phân xử | Bên thực hiện/Người phân xử |
| `migration-and-rollback.md` | Di trú, mất hiệu lực, rollback, handoff | Người phân tích ảnh hưởng/Điều phối viên |

Không tạo tệp rỗng chỉ để đủ danh sách. Tệp chưa cần được ghi `Pending` trong sổ và phải tồn tại trước cổng sử dụng nó.

### 4.3. Impact map và sở hữu tệp

Mỗi tệp nhận đúng một nhãn: `Update`, `Reverify`, `Invalidate`, `No change` hoặc `Not verified`. Mỗi hàng phải có lý do, chủ sở hữu, phép kiểm tra và rollback. Một tệp chỉ có một bên ghi tại một thời điểm. Điều phối viên giữ `orchestration-log.md`; reviewer giữ finding; bên thực hiện không sửa kết luận review.

### 4.4. Cổng Git và cô lập

Trước thay đổi trial, ghi full SHA, nhánh đích, dirty-state, thay đổi sẵn có của người dùng, nhánh/worktree riêng `codex/<run-id>` hoặc cơ chế tương đương, danh sách tệp duyệt và đường hoàn tác không phá huỷ. Nếu baseline không xác minh được, thay đổi giao nhau chưa cô lập hoặc có nguy cơ ghi đè, ghi `Baseline not verified` và dừng trước triển khai.

### 4.5. Hồ sơ quyết định

Thay đổi đề nghị ratify phải có hồ sơ trong `.agents/decisions/` khi chạm `AGENTS.md`, `.agents/rules/`, giao thức dùng chung, trạng thái workflow/skill, quyền hạn, schema dùng chung hoặc nhiều thành phần harness. Thay đổi cục bộ khác vẫn ghi quyết định cuối trong hồ sơ lượt chạy.

### 4.6. Kỹ năng bắt buộc theo loại tệp

| Loại thay đổi | Kỹ năng/quy tắc bắt buộc |
|---|---|
| Tạo hoặc sửa `.agents/skills/` | `$repo-skill-creator`; không được ghi `Required skills: None` |
| Sửa `.agents/rules/` | Quy trình quản trị trong `.agents/rules/README.md`, decision record và kiểm định quản trị độc lập |
| Sửa workflow/giao thức | Danh mục workflow, `agent-dispatch-protocol.md` và kiểm định quản trị độc lập |
| Chạm khẳng định biến động | `$curriculum-reference-research` hoặc `refresh-volatile-content` theo chủ sở hữu |
| Chạm nội dung/kiến trúc giáo trình | Dừng sửa và bàn giao theo mục 1.3 |

Điều phối viên phải điền kỹ năng từ bảng này vào task contract trước phân công; trial contract không được làm yếu yêu cầu của kỹ năng hay nguồn quản trị sở hữu.

## 5. Vai trò và mô hình điều phối

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Khóa scope, áp dụng cổng phân công, giữ sổ, kiểm tra bàn giao | Tự thay Chủ sở hữu hoặc tự cấp tính độc lập |
| Người phân tích bằng chứng | Chuẩn hóa intake, tái hiện, giới hạn dữ liệu | Suy tần suất/tác động từ bằng chứng không có |
| Người chẩn đoán | Lập nguyên nhân và phương án cạnh tranh | Chọn công nghệ vì mới mà thiếu metric |
| Người phân tích ảnh hưởng | Impact map, migration, rollback | Mở rộng sang nội dung/kiến trúc giáo trình |
| Người thực hiện | Áp dụng đúng contract trên nhánh cô lập | Đổi scope/metric/ngưỡng sau khi thấy kết quả |
| Người kiểm chứng | Chạy test matrix, ghi output tái kiểm tra được | Chỉ báo cáo test thuận |
| Người kiểm định quản trị | Đọc trực tiếp nguồn, diff và bằng chứng | Sửa đầu ra mình kiểm định hoặc tự ratify |
| Người phân xử bằng chứng | Phân xử bất đồng dữ kiện trọng yếu | Quyết định ưu tiên thay Chủ sở hữu |
| Chủ sở hữu kho | Duyệt trial và ratify/reject/defer | Không biến dữ kiện chưa kiểm chứng thành `Pass` |

Vai trò không mặc định là một tác nhân. Khi chạy phải dùng `$workflow-orchestration` và [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). Kiểm định quản trị và phân xử bắt buộc là lượt mới độc lập theo mục 6.3–6.5 của giao thức.

## 6. Các giai đoạn thực hiện

### Giai đoạn A — Tiếp nhận và cổng kích hoạt

**Chủ trì:** Điều phối viên và Người phân tích bằng chứng

Tạo run id và sổ; chuẩn hóa candidate, ghi mệnh đề, kỳ vọng, quan sát, nguồn, môi trường, bằng chứng phản bác, mức `Low`/`Medium`/`High`/`Critical`, trigger, mode, authority và dữ liệu cấm. Trả lại `$harness-improvement-discovery`, định tuyến hoặc đóng `No change` nếu đầu vào vẫn là yêu cầu khám phá mở hay không đủ trigger.

**Điều kiện ra:** vấn đề, mode, phạm vi điều tra và quyền quyết định đã rõ.

### Giai đoạn B — Baseline và tái hiện

**Chủ trì:** Người phân tích bằng chứng

Khóa baseline Git/môi trường; tái hiện bằng dữ liệu giả hoặc ẩn danh; tách lỗi hướng dẫn, đầu vào, công cụ, điều phối và phép đo; ghi số lần chạy, độ biến thiên và phần không tái hiện. Incident có thể đề xuất containment hẹp với expiry/rollback.

**Điều kiện ra:** có baseline đo được; nếu `Baseline not verified`, dừng triển khai và chuyển Chủ sở hữu chọn thu thêm bằng chứng, thu hẹp hoặc đóng.

### Giai đoạn C — Chẩn đoán và phương án

**Chủ trì:** Người chẩn đoán

Lập nguyên nhân cạnh tranh cùng bằng chứng chứng thực/chứng ngụy; so sánh `No change`, containment, thay đổi nhỏ nhất và phương án lớn hơn; chọn trial nhỏ nhất đủ phân biệt giả thuyết; ghi rủi ro do đổi và không đổi.

**Điều kiện ra:** có mệnh đề nhân quả kiểm tra được và lý do chọn trial.

### Giai đoạn D — Impact, riêng tư và hợp đồng thử

**Chủ trì:** Người phân tích ảnh hưởng và Điều phối viên

Lập impact map; xác định dữ liệu được thu, dữ liệu cấm, thời hạn giữ và cách ẩn danh. Viết `trial-contract.md` trước triển khai, gồm baseline, kịch bản/số lần chạy, primary metric, guardrails, ngưỡng, bốn lớp test, tệp được sửa, quyền hạn, stop conditions, timebox, rollback và migration. Tạo/dự thảo decision record khi mục 4.5 yêu cầu.

**Điều kiện ra:** bên khác có thể chạy lại contract mà không cần trí nhớ hội thoại.

### Giai đoạn E — Cổng quyết định trial của con người

**Chủ trì:** Chủ sở hữu kho; không giao cho AI

Chọn `Reject`, `Defer`, `Revise` hoặc `Approve trial`. Im lặng không là chấp thuận. `Approve trial` phải khóa mode, tệp, metric, ngưỡng, timebox và quyền hạn; không đồng nghĩa `Ratify` và không cho tích hợp nhánh đích.

### Giai đoạn F — Triển khai cô lập

**Chủ trì:** Người thực hiện

Xác nhận baseline chưa drift; áp dụng thay đổi nhỏ nhất trên vùng cô lập; ghi commit, tệp, lý do và tự kiểm tra. Nếu đổi scope/metric/ngưỡng/quyền hạn hoặc gặp stop condition, dừng và quay lại cổng phù hợp; không tự nới contract.

**Điều kiện ra:** diff trong phạm vi, commit truy vết được, không có sai lệch chưa duyệt.

### Giai đoạn G — Kiểm chứng trial

**Chủ trì:** Người kiểm chứng

Chạy đúng kịch bản/ngưỡng đã khóa; ghi lệnh, phiên bản, input khử nhạy cảm, output và exit status. Báo cả kết quả thuận, nghịch, độ biến thiên và lỗi công cụ. Không loại mẫu thất bại hay đổi cách tính sau kết quả. Tách `Fail` khỏi `Not verified`.

**Điều kiện ra:** `validation-report.md` đủ tái kiểm tra và mọi guardrail có phán quyết.

### Giai đoạn H — Kiểm định độc lập và phân xử

**Chủ trì:** Người kiểm định quản trị độc lập

Reviewer mới đọc trực tiếp nguồn chuẩn, decision record, baseline, intake, contract, diff/commit, impact map, implementation log, validation và rollback. `Pass` chỉ khi trigger/scope hợp lệ, candidate đúng contract, primary metric đạt, guardrails không thất bại, negative/regression test đạt, rollback khả thi, không còn `Blocker`/`Major` và tính độc lập được chứng minh.

Áp dụng mục 6.4–6.5 của giao thức. Chỉ disposition `Accept` cho phép sửa cục bộ. Khi xét `Out of scope`, dùng Người phân tích ảnh hưởng làm phía thứ ba chỉ nếu sổ chứng minh người đó độc lập với bên thực hiện và reviewer; nếu không, phải sinh một Người đánh giá ảnh hưởng mới, độc lập. Finding trọng yếu, phản đối của reviewer, bất đồng dữ kiện hoặc `Not verified` đã cạn đường kiểm tra chuyển `Awaiting adjudication`. Tối đa hai vòng sửa mỗi finding.

### Giai đoạn I — Ratify, tích hợp và đóng

**Chủ trì:** Chủ sở hữu kho và Điều phối viên

Chủ sở hữu chọn `Ratify`, `Revise`, `Reject` hoặc `Defer`. Chỉ sau `Ratify`, Điều phối viên mới xác nhận target không drift; tích hợp đúng commit đã review; chạy lại kiểm tra chịu ảnh hưởng; đồng bộ danh mục/metadata; làm mất hiệu lực có chọn lọc; bàn giao phần ngoài phạm vi; đóng decision và hồ sơ. Không tự xoá nhánh/worktree sau khi đóng.

## 7. Cách kiểm chứng

### 7.1. Bốn lớp bắt buộc

| Lớp | Câu hỏi |
|---|---|
| `Positive` | Candidate cải thiện hành vi đích trên kịch bản hợp lệ không? |
| `Negative` | Có chặn suy đoán, vượt quyền, bỏ cổng, dữ liệu cấm và ngoài phạm vi không? |
| `Regression` | Hành vi đúng, liên kết, schema, validator và bàn giao cũ còn hoạt động không? |
| `Comparison` | Trên cùng input/điều kiện, candidate khác baseline bao nhiêu và biến thiên thế nào? |

Kiểm tra tĩnh chỉ chứng minh cấu trúc. Đánh giá chủ quan cần rubric xác định trước và người chấm độc lập nếu dùng làm primary metric.

### 7.2. Metric và diễn giải

Mỗi trial có đúng một primary metric và có thể có nhiều guardrails. Có thể đo độ đúng nguồn, tuân thủ cổng, lỗi vượt quyền/scope, khả năng truy vết, số lượt sửa, tệp đọc, thời gian/chi phí để đạt cùng chất lượng, hoặc false positive/negative của validator.

Không coi giảm token, thời gian hay số tệp là lợi ích nếu `Accuracy`, `Safety`, `Authority compliance` hoặc `Traceability` giảm. Không tạo điểm gộp sau khi có kết quả. Dữ liệu ít phải báo bất định thay vì khẳng định tổng quát.

### 7.3. Kiểm tra xác định tối thiểu

- liên kết và đường dẫn trong phạm vi hợp lệ;
- schema/validator liên quan chạy thành công;
- diff không vượt nhãn `Update`;
- không có secret, dữ liệu cá nhân, hội thoại dài hay output nhạy cảm;
- trạng thái và nguồn chuẩn nhất quán;
- rollback chỉ chạm commit/tệp của trial;
- sổ, decision record và commit khớp nhau.

Kiểm tra thủ công phải ghi từng phép và bằng chứng, không chỉ ghi “đã kiểm tra”.

## 8. Hoàn tác và xử lý thất bại

- Trước tích hợp, nhánh đích phải nguyên trạng; `Reject`, `Defer` hoặc lỗi trial chỉ giữ nhánh lượt chạy và hồ sơ.
- Containment phải có expiry, chủ sở hữu và tín hiệu buộc gỡ.
- Sau tích hợp, chỉ đảo đúng commit của lượt bằng commit mới trên nhánh sửa chữa; không `reset --hard`, xoá lịch sử hay ghi đè thay đổi đến sau.
- Trước rollback, xác minh commit, tệp và phần giao với thay đổi mới; có xung đột thì dừng xin quyết định.
- Sau rollback, chạy lại guardrail/tham chiếu; trạng thái là `Rolled back`, không phải `Verified`.
- Lỗi công cụ, thiếu quyền/reviewer hoặc không tái hiện baseline được ghi `Not verified` và khóa phần phụ thuộc.
- Rủi ro mới `High`/`Critical` buộc dừng tác động, bảo toàn bằng chứng đã khử nhạy cảm và chuyển Chủ sở hữu.

## 9. Hợp đồng giao việc cho tác nhân AI nhẹ

```text
Role: <Orchestrator | Evidence analyst | Diagnostician | Impact analyst | Implementer | Verifier | Governance reviewer | Evidence adjudicator>
Mode: <Incident containment | Improvement trial>
Current phase: <A | B | C | D | E | F | G | H | I>
Run ID: <stable identifier>
Baseline commit: <full SHA>
Run branch/worktree: <name and path>
Problem statement: <testable claim>
Allowed reads: <explicit paths>
Allowed writes: <explicit paths or none>
Canonical inputs: <sources and decisions>
Required skills: <skill names or None>
Required outputs: <artifacts and locations>
Metrics and thresholds: <locked values or Not applicable>
Run status: <Queued | In progress | Awaiting decision | Closed>
Decision or outcome: <Awaiting trial approval | Approved trial | Revise | Awaiting adjudication | Awaiting ratification | Ratified | Rejected | Deferred | No change | Rolled back | Failed>
Finding IDs and disposition: <IDs/state or None>
Stop conditions: <authority, drift, scope, sensitive data, metric change, guardrail, dispute>
Do not: <edit outside scope, change thresholds after results, expose secrets, self-approve, infer Pass from Not verified, mutate target before Ratify>
```

Tác nhân không tự chuyển giai đoạn. Nó trả đầu ra, phép kiểm tra, giới hạn, sai lệch và lý do dừng cho Điều phối viên; không dùng trí nhớ hội thoại thay nguồn tệp.

## 10. Điều kiện đóng quy trình

### 10.1. Điều kiện chung

1. Trigger hoặc yêu cầu khảo sát, mode, vấn đề gốc, phạm vi và kết quả đóng đã được ghi.
2. Mọi finding đã phát sinh có disposition; finding trọng yếu chưa xác minh đã được Chủ sở hữu quyết định.
3. Không có tham chiếu mồ côi hoặc handoff thiếu nơi nhận.
4. Hồ sơ không chứa dữ liệu cấm và có thời hạn giữ bằng chứng.
5. Nếu có tác nhân con, mục 8 của giao thức đạt; cổng độc lập bắt buộc không còn `Not verified`.
6. Lượt sau tiếp tục được từ tệp, không cần hội thoại.

### 10.2. Nhánh đóng không triển khai trial

Lượt bị loại ở intake, chọn `No change`, `Rejected` hoặc `Deferred` trước triển khai không cần tạo nhánh/worktree, commit triển khai, validation hay rollback giả. Nó chỉ đóng khi bằng chứng đã thu, lý do không tiếp tục, người quyết định và điều kiện tái nhập (nếu có) được ghi; `git-baseline.md` ghi `Not required — no implementation` nếu chưa mở cổng Git.

### 10.3. Nhánh đã triển khai trial hoặc containment

Ngoài mục 10.1, phải đạt:

1. Baseline, nhánh đích, vùng cô lập và commit truy vết được.
2. Có `Approve trial` trước triển khai và một kết quả đóng hợp lệ ở mục 3.
3. Mọi finding có re-review/phân xử theo giao thức.
4. `Ratified` chỉ áp dụng đúng commit được review độc lập `Pass` và đã kiểm tra sau tích hợp.
5. Migration, rollback, expiry containment và phần mất hiệu lực có chủ sở hữu.

Workflow chỉ chứng minh thay đổi đạt contract trong phạm vi trial; không chứng minh hiệu quả cho mọi tác vụ hay môi trường.

## 11. Điều kiện chuyển sang `Active`

Chỉ đề nghị `Active` sau ít nhất một controlled trial thật đã đóng, có baseline/candidate tái hiện được, negative và regression tests, rollback hoặc quyết định không tích hợp an toàn, kiểm định độc lập được chứng minh, bằng chứng chi phí điều phối hợp lý và decision record của Chủ sở hữu về phạm vi hiệu lực/di trú. Một trial `Pass` không tự nâng workflow lên `Active`.
