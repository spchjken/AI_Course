# Quy trình hoàn thiện bài học theo mục tiêu

- **Trạng thái:** `Proposed` — chờ hoàn tất cơ chế nghiên cứu nguồn bên ngoài và quyết định kích hoạt
- **Mục tiêu:** biến bản định hướng thiết kế của một mục tiêu `gNN` thành bộ tài liệu bài học có thể kiểm định và tối thiểu `Pilot-ready`, không đồng nhất việc tạo đủ tệp với việc hoàn thành.
- **Phạm vi:** hoàn thiện lần lượt các bài học chuẩn trong `ai-native-builder/goals/gNN-*`.
- **Ngoài phạm vi:** đổi kết quả, ranh giới, điều kiện tiên quyết, quan hệ phụ thuộc hoặc cam kết chương trình của mục tiêu; ghép lộ trình; dạy thử và cấp `Validated`; tự động hóa hoặc thay đổi công cụ ngoài phạm vi bằng chứng.
- **Đơn vị xử lý:** một thư mục mục tiêu trong mỗi vòng lặp.
- **Hồ sơ vận hành:** mỗi mục tiêu dùng một `run-id` riêng trong `.agents/workflow-runs/<run-id>/` và không ghi hồ sơ vận hành vào nguồn chuẩn.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Dùng quy trình này khi cần hoàn thiện hoặc sửa có kiểm soát một bộ bài học
thuộc đúng một mục tiêu `gNN`, bao gồm:

1. Tạo bộ tài liệu lần đầu từ `README.md` của mục tiêu.
2. Bổ sung một tệp, sản phẩm trung gian, bằng chứng hoặc cổng kiểm tra còn
   thiếu trong bộ bài học.
3. Sửa finding cục bộ sau kiểm định mà không đổi hợp đồng mục tiêu.
4. Tái nhập một mục tiêu sau khi nguồn chuẩn hoặc bằng chứng được quy trình
   sở hữu cập nhật.

Không dùng quy trình này để thay đổi kiến trúc mục tiêu, ghép lịch/lộ trình,
phân tích bằng chứng dạy thử hoặc tự kiểm tra lại claim biến động ngoài phạm vi
đã khóa.

### 1.2. Định tuyến khi không thuộc phạm vi

| Nguyên nhân gốc | Quy trình chịu trách nhiệm |
|---|---|
| Đổi kết quả, ranh giới, điều kiện tiên quyết, quan hệ phụ thuộc hoặc cam kết chương trình | `change-curriculum-architecture` |
| Ghép mục tiêu, lịch, thời lượng hoặc buổi thực hành | `compose-learning-run` |
| Thu thập/phân tích bằng chứng từ người học thật hoặc cấp `Validated` | `pilot-and-validate` |
| Kiểm tra lại claim về công cụ, API, mô hình, giá, quyền hạn hoặc chính sách | `refresh-volatile-content` |

### 1.3. Nguyên tắc điều phối

Phần nguyên tắc chi tiết được giữ trong phụ lục A.1 bên dưới để bảo toàn các
quy tắc sở hữu tệp và ranh giới đã được dùng trong các lượt trước.

## 2. Hai chế độ thực hiện

| Chế độ | Khi dùng | Đầu ra hợp lệ | Giới hạn |
|---|---|---|---|
| `Full completion` | Bộ bài học chưa hoàn chỉnh hoặc chưa có hợp đồng thiết kế/bằng chứng cần thiết. | Bộ tệp chuẩn, hồ sơ nghiên cứu, review độc lập và trạng thái tối đa `Pilot-ready`/`Release-ready`. | Không cấp `Validated`; không bỏ qua B, C, D hoặc E vì muốn nhanh hơn. |
| `Targeted repair` | Có finding, thiếu cổng hoặc lỗi truy vết cục bộ trong bộ đã tồn tại. | Finding disposition, thay đổi tối thiểu, bằng chứng kiểm tra lại và review lại đúng phạm vi. | Không dùng để âm thầm đổi mục tiêu; finding tranh chấp/thiếu bằng chứng phải qua §6.4 của `agent-dispatch-protocol.md`. |

`Targeted repair` có thể quay lại B, C hoặc D khi finding làm hỏng hợp đồng,
nghiên cứu hoặc quyền sở hữu tệp. Không coi việc quay lại một giai đoạn là mở
toàn bộ phạm vi viết lại.

## 3. Sơ đồ tổng thể và trạng thái

```text
TRIGGER
  ↓
INTAKE → PREFLIGHT → LEARNING-DESIGN CONTRACT → CONTENT TRACE
                                      ↓
                              EXTERNAL RESEARCH
                                      ↓
                                  AUTHORING
                                      ↓
                         LOCAL / DETERMINISTIC CHECKS
                                      ↓
                            INDEPENDENT REVIEW
                 ┌───────────────┴────────────────┐
                 │                                │
       Finding disposition                    Quality recorded
                 │                                ↓
        repair / re-entry /              READY FOR HANDOFF
        adjudication / stop
```

`Queued`, `In progress`, `Awaiting decision` và `Closed` là trạng thái của
lượt chạy. `Preflight`, `Authoring`, `Independent review` và `Ready for
handoff` là nhãn giai đoạn hoặc điều kiện chuyển tiếp; chúng không thay thế
trạng thái chất lượng trong `review.md`. `Needs revision`, `Pilot-ready`,
`Release-ready` và `Validated` chỉ được ghi ở đúng quy trình sở hữu.

## 4. Đầu vào, trách nhiệm chuẩn bị và đầu ra

Điều phối viên phải khóa đầu vào, người cung cấp, người ghi và người nghiệm thu
trước khi giao từng đơn vị công việc. Các bảng chi tiết và cấu trúc tệp nằm ở
phụ lục A.2–A.3; phần tóm tắt chuẩn hóa ở đây là hợp đồng điều phối.

### 4.1. Đầu vào tối thiểu

| Đầu vào | Bên cung cấp | Trách nhiệm chuẩn bị |
|---|---|---|
| Quy tắc và nguồn chuẩn | Kho dự án | Đọc trực tiếp, ghi baseline và xung đột; không tự tạo nguồn thứ hai. |
| `README.md` của mục tiêu | Chủ sở hữu mục tiêu | Xác nhận kết quả, phạm vi, sản phẩm, bằng chứng, an toàn và bàn giao. |
| Điều kiện tiên quyết | Mục tiêu trước/lộ trình liên quan | Xác nhận sản phẩm thật hoặc ghi `Not applicable`/`Missing input` có lý do. |
| Bằng chứng và kết quả cũ | Hồ sơ mục tiêu/lượt chạy | Chỉ dùng khi truy được phiên bản, phạm vi và giới hạn kết luận. |

### 4.2. Đầu ra và chủ sở hữu

| Đầu ra | Bên tạo/cập nhật | Bên nghiệm thu |
|---|---|---|
| `lesson.md`, `practice.md`, `instructor-guide.md`, `assessment.md`, `pilot-feedback-form.md` | Người soạn theo từng đơn vị D | Người tích hợp cục bộ rồi reviewer độc lập |
| `references.md` | Người nghiên cứu | Reviewer độc lập đối với claim trọng yếu |
| `review.md` | Reviewer độc lập | Điều phối viên kiểm tra tính đầy đủ, không đổi verdict |
| `finding-disposition.md` trong hồ sơ run | Bên xử lý finding/evidence adjudicator | Reviewer độc lập kiểm tra đường phản hồi và re-review |
| `learning-design-contract.md`, `content-trace.md` | Người thiết kế/B0 | Điều phối viên và các đơn vị bị ảnh hưởng |
| `progress-tracker.md` và hồ sơ run | Điều phối viên | Chủ sở hữu kho/đơn vị nhận bàn giao |

## 5. Vai trò và mô hình điều phối tác nhân

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Khóa scope, baseline, trạng thái, phân công và bàn giao | Tự thay Chủ sở hữu hoặc tự cấp `Pass` |
| Người thiết kế/B0 | Thiết kế sản phẩm trung gian, ánh xạ đánh giá và content trace | Đổi kết quả mục tiêu |
| Người nghiên cứu | Khảo sát nguồn, ghi claim/evidence và giới hạn | Sửa bài học hoặc tự quyết đánh đổi |
| Người soạn/tích hợp | Ghi đúng tệp sở hữu và chạy local gate | Sửa tệp của đơn vị khác hoặc xóa finding |
| Reviewer độc lập | Đọc trực tiếp nguồn, đầu ra và bằng chứng; ghi `review.md` | Tự nghiệm thu phần vừa tạo/sửa |
| Evidence adjudicator | Phân xử bất đồng dữ kiện trọng yếu theo §6.4–§6.5 của `agent-dispatch-protocol.md` | Thay Chủ sở hữu quyết định đánh đổi |
| Chủ sở hữu giáo trình | Quyết định khi đổi phạm vi, ưu tiên, chi phí hoặc trạng thái | Ghi `Pass` từ bằng chứng chưa kiểm chứng |

Phân công cụ thể phải tuân thủ `agent-dispatch-protocol.md`; vai trò không mặc
định tương đương một tác nhân riêng. E phải là lượt/tác nhân mới; finding
`Dispute`, `Need evidence`, `Out of scope` hoặc `Not verified` trọng yếu không
được biến thành lệnh sửa mà thiếu disposition và đường phân xử.

## 6. Các giai đoạn thực hiện

| Giai đoạn | Đầu ra chính | Điều kiện chuyển |
|---|---|---|
| A — Intake/preflight | Baseline, input manifest, conflict classification | Không còn thiếu đầu vào ảnh hưởng kết quả/an toàn |
| B — Learning design | `learning-design-contract.md`, `content-trace.md` | Sản phẩm, quyết định, evidence và quyền sở hữu rõ |
| C — Research | `references.md`, claim/evidence register | Claim trọng yếu được hỗ trợ, thu hẹp hoặc chuyển cấp |
| D — Authoring/integration | Bộ bài học và local checks | Từng tệp qua cổng cục bộ, không còn placeholder |
| E — Independent review | `review.md`, verdict và findings | Có review độc lập trực tiếp, không tự nghiệm thu |
| F — Bounded repair | Disposition, diff, expected evidence, re-review | Finding được đóng, chuyển cấp hoặc `Awaiting adjudication` |
| G — Handoff/close | Run record, trạng thái, bàn giao | Không còn blocker chưa định tuyến; trạng thái trung thực |

Chi tiết thao tác A–G và quyền ghi vẫn được giữ trong phụ lục A.6.

## 7. Cách kiểm chứng

Kiểm chứng gồm bốn lớp, chạy theo phạm vi thực tế:

1. **Local/deterministic:** cấu trúc tệp, liên kết, placeholder, thời lượng,
   quyền sở hữu, schema và truy vết.
2. **Negative:** thiếu đầu vào, lỗi an toàn, claim không có nguồn, scope
   conflict và đường sửa sai bị chặn.
3. **Independent semantic review:** tám hard gate trong
   `.agents/rules/quality-gates.md` được ghi `Pass`/`Fail`/`Not verified`; tám
   tiêu chí chất lượng được chấm `0–2`, kèm findings và trạng thái.
4. **Re-review/handoff:** chỉ reviewer độc lập xác nhận thay đổi; `Validated`
   phải do `pilot-and-validate` cấp sau dạy thử thực tế.

Mọi finding `Blocker`, `Major`, hard gate `Fail`/`Not verified` hoặc finding có
thể đổi phạm vi phải ghi ở `review.md`, phản hồi append-only trong
`finding-disposition.md`, và áp dụng §6.4–§6.5 của `agent-dispatch-protocol.md`.

## 8. Hoàn tác và xử lý thất bại

- `Missing input` ảnh hưởng kết quả, bằng chứng hoặc an toàn → `Awaiting input`,
  không suy đoán.
- Xung đột mục tiêu/kiến trúc/nguồn chuẩn → dừng và bàn giao
  `change-curriculum-architecture`; không sửa nội dung để né xung đột.
- Finding cục bộ `Accept` → sửa tối thiểu rồi kiểm định lại; `Dispute`/`Need
  evidence`/`Out of scope` → phản hồi, thu hẹp hoặc phân xử trước khi sửa.
- Sau tối đa hai vòng vẫn còn lỗi chặn, tranh chấp hoặc `Not verified` trọng
  yếu → `Awaiting adjudication` cho Chủ sở hữu; không lặp vô hạn.
- Phát hiện sửa nhầm tệp, canonical mutation hoặc scope drift → khóa tích hợp,
  ghi baseline/diff, khôi phục đúng hunk đã biết hoặc bàn giao cho quy trình
  sở hữu; không dùng thao tác phá rộng.

## 9. Hợp đồng giao việc cho tác nhân AI nhẹ

Mỗi đơn vị chỉ có một vai trò chính, một giai đoạn, một danh sách tệp rõ ràng
và một local gate:

```text
Role: <Coordinator | Researcher | Learning designer | Lesson author | Assessment designer | Feedback-form author | Integrator | Independent reviewer | Evidence adjudicator | Repair owner>
Goal folder: <ai-native-builder/goals/gNN-*>
Mode: <Full completion | Targeted repair>
Phase: <A | B | C | D | E | F | G>
Work package: <A1-A6 | B1-B7 and B0 | C1-C6 | D1-D6 | E1-E6 | F1-F5 | G1-G6>
Allowed files: <explicit file list>
Canonical inputs: <required files to read>
Required skills: <ordered `$skill-name` values or None>
Required outputs: <files, sections, evidence, and finding disposition/adjudication when applicable>
Decision status: <Not required | Awaiting decision | Confirmed | Awaiting adjudication>
Local gate: <pass conditions from section 7 and Appendix A.4.10>
Stop conditions: <conflict, missing input, unsafe action, scope change, failed gate>
Do not: <change goals, copy shared content, raise status, expand scope, self-approve>
```

## 10. Điều kiện đóng quy trình

1. Có run-id, baseline, input manifest và hồ sơ tiến độ.
2. Đầu ra đúng mode, đúng chủ sở hữu, không sao chép nguồn dùng chung.
3. Tất cả local gate và cổng bắt buộc đã có bằng chứng; finding còn lại đã
   được sửa, thu hẹp, rút, chuyển cấp hoặc ghi `Awaiting adjudication`.
4. Reviewer độc lập ghi trạng thái chất lượng trung thực; không tự nâng lên
   `Validated`.
5. Có bàn giao tới mục tiêu/quy trình tiếp theo và ghi giới hạn còn lại.

## 11. Điều kiện chuyển quy trình sang `Active`

Workflow này hiện giữ `Proposed` theo hồ sơ quyết định về cổng nghiên cứu nguồn
bên ngoài. Chỉ chuyển sang `Active` sau khi có bằng chứng rằng: bộ tệp
chuẩn và quyền sở hữu không mơ hồ; B/C/D/E/F/G có thể chạy trên ít nhất một
mục tiêu; review độc lập và phân xử finding hoạt động; tối đa hai vòng sửa được
giữ; rollback/handoff khả thi; và hồ sơ agent-dispatch chứng minh được các lượt
được phân công. Không dùng việc workflow đã tồn tại lâu hoặc đã tạo đủ tệp làm
bằng chứng.

## Phụ lục A — Đặc tả chi tiết và hướng dẫn triển khai

Phần dưới đây giữ các bảng, mẫu tệp, tiêu chí local gate, state machine chi tiết
và hướng dẫn A–G của phiên bản trước. Các tham chiếu `A.x` trong phần này là
chi tiết triển khai của Phụ lục A; các cổng điều phối chuẩn hiện hành là mục
1–11 ở trên.

### A.1. Nguyên tắc điều phối

1. Xử lý một mục tiêu tại một thời điểm theo quan hệ phụ thuộc trong `ai-native-builder/curriculum-map.md`, trừ khi người dùng chỉ định mục tiêu khác.
2. `README.md` trong thư mục mục tiêu là bản định hướng thiết kế kiêm đặc tả. Tác nhân AI triển khai không được tự đổi kết quả, điều kiện tiên quyết, phạm vi hoặc sản phẩm trung gian đã quy định.
3. Khi bản định hướng mâu thuẫn với kế hoạch chung, kiến trúc nội dung hoặc quy tắc, dừng mọi thay đổi phụ thuộc và áp dụng quy trình xử lý xung đột trong `.agents/rules/README.md`.
4. Tách vai trò người soạn và người kiểm định ở cả trách nhiệm lẫn ngữ cảnh thực thi. Người soạn được tự kiểm tra nhưng không được là thẩm quyền duy nhất cấp `Pass`; người kiểm định phải là người khác hoặc một lượt tác nhân AI độc lập, đọc trực tiếp đầu ra và bằng chứng trước khi kết luận.
5. Mỗi vòng sửa chỉ xử lý phát hiện đã nêu hoặc quan hệ phụ thuộc phát sinh trực tiếp. Không mở rộng tính năng hay viết lại toàn bài vô cớ.
6. Không bàn giao năng lực hoặc sản phẩm trung gian cho mục tiêu kế tiếp khi cổng bắt buộc liên quan còn `Fail` hoặc `Not verified`. Có thể chuẩn bị một mục tiêu khác khi công việc đó không sử dụng và không giả định phần chưa được kiểm chứng; mục tiêu hiện tại vẫn giữ trạng thái `Needs revision`.
7. `Beginner clarity` và `Time feasibility` không được chấm `2` trước dạy thử với đúng đối tượng.

### A.2. Đầu vào bắt buộc

Điều phối viên phải lập danh mục đầu vào trước khi giao việc cho tác nhân AI. Bảng dưới đây là phần giải thích cho người đọc quy trình, không phải schema của một hồ sơ vận hành mà tác nhân phải tạo:

| Đầu vào | Mức áp dụng | Ghi chú |
|---|---|---|
| `.agents/rules/README.md` và các quy tắc được chuyển từ đó | Bắt buộc | Áp dụng cho mọi mục tiêu. |
| `AI-native-builder-curriculum-plan.md` | Bắt buộc | Áp dụng cho mọi mục tiêu. |
| `curriculum-content-architecture.md` | Bắt buộc | Áp dụng cho mọi mục tiêu. |
| `ai-native-builder/curriculum-map.md` | Bắt buộc | Chỉ dùng để xác định thứ tự và quan hệ phụ thuộc; không ghi hồ sơ vận hành vào đây. |
| `README.md` của mục tiêu đang xử lý | Bắt buộc | Bản định hướng thiết kế của bài học. |
| Sản phẩm trung gian hoặc bài học điều kiện tiên quyết từ mục tiêu trước | Có điều kiện | `Not applicable` với mục tiêu không có điều kiện tiên quyết, như G01. |
| Lộ trình liên quan | Có điều kiện | Chỉ bắt buộc khi lộ trình đã đặt ràng buộc về thời lượng hoặc mức trưởng thành. |
| Mẫu, phương pháp thực hành và chính sách dùng chung được `README.md` của mục tiêu liên kết | Có điều kiện | Chỉ đọc khi bài học thực sự sử dụng chúng. |
| Kết quả kiểm định hoặc bằng chứng dạy thử hiện có | Có điều kiện | Không áp dụng với bài chưa từng được kiểm định hoặc dạy thử. |

`Not applicable` là một kết luận hợp lệ có nêu lý do, không phải đầu vào thiếu. Với đầu vào đang áp dụng mà không có, tác nhân AI phải ghi `Missing input`, đánh giá tác động và chuyển sang `Awaiting input` khi phần thiếu làm thay đổi kết quả, bằng chứng hoặc an toàn. Chỉ tiếp tục khi phần thiếu không làm thay đổi các yếu tố đó.

### A.3. Bộ tài liệu đầu ra của một mục tiêu

Giữ `README.md` làm bản định hướng thiết kế. Toàn bộ vòng lặp tạo ra bộ tệp tối thiểu sau; mỗi tệp do đúng vai trò được quy định ở phụ lục A.6 sở hữu:

```text
gNN-slug/
├── README.md              # Canonical design brief; already exists
├── lesson.md              # Learner-facing content and learning flow
├── practice.md            # Practice, failure case, and artifact instructions
├── instructor-guide.md    # Facilitation, timing, intervention, and recovery
├── assessment.md          # Evidence blueprint, rubric, and retry protocol
├── pilot-feedback-form.md # Learner feedback form for a future pilot
├── references.md          # External comparison, claims, evidence, and recheck metadata
└── review.md              # Hard gates, quality score, findings, and status
```

Chỉ tạo khi cần:

```text
└── assets/                # Lesson-specific starter, fixture, or media
```

Không sao chép mẫu, chính sách hoặc bài thực hành dùng chung vào thư mục mục tiêu. Hãy liên kết tới `ai-native-builder/shared/` và đề xuất hoàn thiện nguồn dùng chung nếu còn thiếu.

Người soạn sở hữu `lesson.md`, `practice.md`, `instructor-guide.md`, `assessment.md` và `pilot-feedback-form.md`. Người nghiên cứu sở hữu `references.md`. Người kiểm định độc lập sở hữu `review.md`; người soạn không tạo trước nội dung hoặc phán quyết trong tệp đó.

`assets/` là thư mục chứa, không phải một tệp có một chủ duy nhất. Mỗi tệp bên trong phải được hợp đồng đơn vị công việc gán đúng một người ghi: tài nguyên minh họa thuộc D1, tệp khởi đầu hoặc fixture phục vụ thực hành thuộc D2, tài nguyên chẩn đoán dành cho giảng viên thuộc D3, trừ khi hợp đồng ghi ngoại lệ cụ thể. D6 chỉ đọc và kiểm tra liên kết; không tự sửa asset của đơn vị khác.

Mỗi lượt chạy còn tạo các hồ sơ bàn giao bền vững ngoài thư mục bài học. Chúng không phải nguồn chuẩn của giáo trình và không phải mẫu dùng chung:

```text
.agents/workflow-runs/<run-id>/
├── input-manifest.md
├── progress-tracker.md
├── learning-design-contract.md
├── content-trace.md
└── finding-disposition.md   # required when a finding needs response/adjudication
```

Điều phối viên sở hữu `input-manifest.md` và `progress-tracker.md`, Người thiết kế sở hữu `learning-design-contract.md`, B0 sở hữu `content-trace.md`, còn bên xử lý finding/evidence adjudicator sở hữu `finding-disposition.md` khi tệp này được kích hoạt. `progress-tracker.md` và `input-manifest.md` được tạo ở A; hai hợp đồng thiết kế còn lại được tạo ở B trước lượt nghiên cứu C. Các tệp được giữ nguyên như hồ sơ bàn giao khi đóng lượt chạy, không bị sửa âm thầm sau khi đóng. Lượt chạy sau phải có `run-id` mới và tham chiếu hồ sơ cũ nếu cần. Nội dung đã được triển khai phải truy vết được tới bộ tệp bài học hoặc `review.md` trước khi đóng lượt chạy.

### A.4. Hướng dẫn xây nội dung cho từng tệp

Phần này là đặc tả trực tiếp cho tác nhân AI nhẹ. Tác nhân không được chỉ tạo đủ tiêu đề; mỗi phần phải thực hiện đúng chức năng, có đầu vào, đầu ra và khả năng truy vết về bản định hướng thiết kế.

#### A.4.0 Ranh giới giữa quy trình và kỹ năng soạn bài

Quy trình này sở hữu gói tệp bắt buộc, thứ tự B0 rồi D1–D6, quyền ghi tệp, cổng kiểm tra cục bộ và cách bàn giao cho mô hình nhẹ. `$lesson-authoring` sở hữu phương pháp sư phạm tái sử dụng để biến kết quả học tập thành chuỗi hoạt động; `$assessment-design` sở hữu phương pháp thiết kế đánh giá năng lực. Khi được gọi từ quy trình này, các kỹ năng phải tuân thủ cấu trúc và ranh giới tệp tại đây.

Nếu thay đổi một yêu cầu xuất hiện ở cả quy trình và kỹ năng, người sửa phải kiểm tra tệp còn lại, ghi phạm vi ảnh hưởng và chỉ giữ một nguồn quy định chi tiết. Không được xóa đặc tả tệp khỏi quy trình với lý do nó đã xuất hiện trong kỹ năng: đây là hợp đồng thực thi dành cho tác nhân nhẹ.

#### A.4.1 Lập bảng truy vết nội dung trước khi viết

Trước khi nghiên cứu nguồn bên ngoài hoặc tạo tệp bài học, B0 — người tích hợp dàn ý — phải đọc `learning-design-contract.md` của giai đoạn B và lập bảng sau trong `content-trace.md` từ đặc tả mục tiêu, hợp đồng sản phẩm trung gian và bản thiết kế đánh giá năng lực:

| Thành phần đặc tả trong `README.md` | Nội dung cần dạy hoặc thực hiện | Tệp sở hữu | Phần dự kiến | Bằng chứng tạo ra |
|---|---|---|---|---|
| Kết quả quan sát được | Hành vi giúp đạt kết quả | `lesson.md`/`practice.md` | Tên phần | Sản phẩm trung gian hoặc phần trình diễn |
| Quyết định thuộc về học viên | Tình huống buộc học viên lựa chọn | `practice.md` | Bước N | Hồ sơ quyết định |
| Vai trò của AI | Việc AI được và không được làm | `lesson.md`/`practice.md` | Tên phần | Đề xuất của AI và phản hồi của học viên |
| Điểm chạm mã nguồn | Nội dung cần quan sát, kiểm định, sửa hoặc chẩn đoán | `practice.md` | Bước N | Phần thay đổi, nhật ký hoặc lời giải thích lại |
| Đường xử lý lỗi | Lỗi có chủ đích và cách phục hồi | `practice.md`/`instructor-guide.md` | Tên phần | Bằng chứng trước và sau |
| Sản phẩm trung gian | Hướng dẫn tạo và lưu | `practice.md` | Đầu ra | Sản phẩm trung gian hoàn chỉnh |
| Bằng chứng đánh giá năng lực | Cách người kiểm định đưa ra phán đoán | `assessment.md` | Thiết kế bằng chứng | Tiêu chí và kết quả |
| An toàn | Ranh giới và điểm cần phê duyệt | Tệp nơi hành động xảy ra | Tên phần | Kết quả kiểm tra hoặc quyết định an toàn |
| Bàn giao | Phần mà mục tiêu sau sẽ sử dụng | `lesson.md`/`practice.md` | Kết thúc | Đường dẫn tới sản phẩm trung gian |

Không bắt đầu viết văn bản diễn giải nếu còn thành phần đặc tả chưa có tệp hoặc phần sở hữu. Mỗi nội dung chỉ nên có một tệp sở hữu; tệp khác chỉ liên kết hoặc tóm tắt tối đa một câu khi cần điều hướng.

#### A.4.2 Cách viết `lesson.md`

`lesson.md` là tài liệu dành cho học viên, giúp họ hình thành mô hình tư duy vừa đủ trước và trong khi thực hành. Đây không phải kịch bản cho giảng viên, bản chép lời bài giảng hoặc bản sao của `README.md`.

Dùng cấu trúc bắt buộc:

```md
# <Tên học phần>

## Bạn sẽ làm được gì
## Vì sao năng lực này cần thiết
## Trước khi bắt đầu
## Các khái niệm cốt lõi
## Quy trình ra quyết định
## Ví dụ xuyên suốt
## Các sai lầm thường gặp
## Tự kiểm tra trước thực hành
## Thực hành và đầu ra
## Điều mang sang học phần tiếp theo
```

Điền từng phần như sau:

- **Bạn sẽ làm được gì:** viết một kết quả bằng động từ quan sát được, sản phẩm trung gian phải tạo và cách chứng minh; không dùng “hiểu”, “biết” nếu không kèm hành vi.
- **Vì sao năng lực này cần thiết:** mở bằng một lỗi thực tế của người mới và hậu quả đối với sản phẩm; tối đa hai đoạn, không dùng lời quảng cáo hoặc hứa hẹn chung chung.
- **Trước khi bắt đầu:** liệt kê năng lực tiên quyết, sản phẩm trung gian hoặc tệp cần có, công cụ, thiết lập và cách học viên tự kiểm tra mức sẵn sàng. Mỗi điều kiện tiên quyết phải đến từ mục tiêu trước hoặc được hỗ trợ nền ngay trong bài học.
- **Các khái niệm cốt lõi:** chỉ giữ 2–5 khái niệm cần để ra quyết định. Với mỗi khái niệm, cung cấp định nghĩa bằng ngôn ngữ thông thường, công dụng, một ví dụ trong tình huống xuyên suốt, một phản ví dụ hoặc ngộ nhận và câu hỏi kiểm tra nhanh.
- **Quy trình ra quyết định:** mô tả các bước học viên thực hiện, đầu vào của mỗi bước, câu hỏi phải trả lời, đầu ra tạo ra và điều kiện dừng. Không biến thành một công thức nhắc lệnh cố định.
- **Ví dụ xuyên suốt:** dùng cùng một tình huống từ đầu tới cuối; trình bày `weak draft → problem detection → learner decision → revision → evidence`. Ghi rõ phần AI đề xuất và phần học viên chốt.
- **Các sai lầm thường gặp:** lấy trực tiếp từ đường xử lý lỗi trong README; với mỗi lỗi nêu dấu hiệu quan sát được, nguyên nhân có thể có và hành động chẩn đoán đầu tiên. Không chỉ viết “tránh làm X”.
- **Tự kiểm tra trước thực hành:** 3–5 câu hỏi hoặc nhiệm vụ nhỏ buộc học viên giải thích hoặc lựa chọn, kèm bằng chứng dự kiến; tránh câu hỏi chỉ kiểm tra trí nhớ thuật ngữ.
- **Thực hành và đầu ra:** liên kết sang `practice.md`, nêu thời lượng, sản phẩm trung gian, quyết định thuộc về học viên và bằng chứng hoàn thành trong tối đa một đoạn ngắn.
- **Điều mang sang học phần tiếp theo:** nêu tệp/sản phẩm trung gian nào được tái sử dụng, mục tiêu nào tiêu thụ nó và điều kiện khiến nó đủ dùng.

Yêu cầu chất lượng riêng:

- Mỗi khái niệm phải phục vụ một bước trong bài thực hành; xóa khái niệm không được dùng.
- Không nhúng lời nhắc khiến AI trả lời thay toàn bộ phần việc của học viên. Lời nhắc mẫu phải yêu cầu AI đặt câu hỏi, đề xuất hoặc phản biện và để học viên tự quyết định.
- Chỉ dẫn riêng cho từng công cụ phải nằm ở phần riêng, có nguồn, ngày kiểm tra hoặc liên kết tới `references.md`.
- Không trộn hướng dẫn giảng viên vào văn bản dành cho học viên.

#### A.4.3 Cách viết `practice.md`

`practice.md` là trung tâm của bài học. Nó phải tạo sản phẩm trung gian và bằng chứng thật, không phải danh sách câu hỏi đọc hiểu.

Dùng cấu trúc bắt buộc:

```md
# Thực hành: <Tên nhiệm vụ>

## Nhiệm vụ
## Đầu vào và thiết lập
## Đầu ra bắt buộc
## Ràng buộc và quyền quyết định
## Các bước thực hiện
## Thử thách xử lý lỗi
## Kiểm chứng đầu ra
## Nộp gì để được kiểm định
## Nếu chưa đạt
```

Điền từng phần như sau:

- **Nhiệm vụ:** một tình huống có người dùng/kết quả rõ, nối trực tiếp với kết quả; tránh yêu cầu giả lập không liên quan dự án học viên.
- **Đầu vào và thiết lập:** chỉ rõ tệp khởi đầu, tài khoản hoặc công cụ, trạng thái ban đầu, dữ liệu giả và cách kiểm tra mức sẵn sàng. Có phương án dự phòng nếu thiết lập bên ngoài không ổn định.
- **Đầu ra bắt buộc:** chỉ rõ đường dẫn hoặc tên sản phẩm trung gian, lược đồ hoặc mẫu dùng chung bắt buộc và giới hạn độ dài hoặc phạm vi phù hợp với thời gian.
- **Ràng buộc và quyền quyết định:** liệt kê điều AI được làm, điều AI không được tự quyết, ranh giới an toàn, mục tiêu loại trừ và điều kiện dừng.
- **Các bước thực hiện:** mỗi bước dùng hoạt động đặc tả dưới đây; không gộp nhiều quyết định lớn vào một bước.
- **Thử thách xử lý lỗi:** đưa ra một lỗi cụ thể có thể quan sát và phục hồi. Không tiết lộ ngay đáp án; cung cấp đủ dấu vết để học viên chẩn đoán.
- **Kiểm chứng đầu ra:** chuyển bằng chứng chấp nhận thành thao tác học viên có thể chạy hoặc quan sát; ghi kết quả dự kiến, thực tế và phán quyết `Pass`, `Fail` hoặc `Not verified`.
- **Nộp gì để được kiểm định:** liệt kê sản phẩm trung gian, bằng chứng quyết định, hồ sơ kiểm chứng và phần giải thích ngắn; không mặc định nộp toàn bộ lịch sử trò chuyện.
- **Nếu chưa đạt:** điều hướng học viên theo loại lỗi tới thử lại, thu hẹp phạm vi, bổ sung điều kiện tiên quyết hoặc hoàn tác; không chỉ bảo “thử lại”.

Mỗi bước trong `Các bước thực hiện` phải theo cấu trúc:

```md
### Bước N — <Hành vi của học viên>

- Mục đích:
- Thời lượng:
- Đầu vào:
- Học viên thực hiện:
- Việc giao cho AI:
- Học viên phải quyết định:
- Đầu ra/bằng chứng:
- Điều kiện qua điểm kiểm tra:
- Nếu sai hoặc thiếu:
```

Quy tắc cho hoạt động:

- Mỗi bước phải tạo hoặc biến đổi một phần sản phẩm trung gian/bằng chứng.
- Tối thiểu một bước yêu cầu học viên phản biện, sửa hoặc từ chối đề xuất AI.
- Điểm chạm mã nguồn phải xuất hiện trong bước có mục đích sản phẩm rõ, với câu hỏi học viên cần trả lời về tệp, phần thay đổi, nhật ký hoặc hành vi.
- Tổng giới hạn thời gian các bước phải khớp ngân sách trong README/lộ trình và có 10–20% khoảng dự phòng phục hồi.
- Thử thách xử lý lỗi phải có đường đặt lại hoặc hoàn tác trước khi học viên kích hoạt nó.

#### A.4.4 Cách viết `instructor-guide.md`

`instructor-guide.md` giúp một giảng viên khác triển khai bài học nhất quán mà không phải đoán thời lượng, dấu hiệu học viên mắc kẹt hoặc mức hỗ trợ được phép.

Dùng cấu trúc bắt buộc:

```md
# Hướng dẫn giảng viên: <Tên học phần>

## Mục tiêu quan sát
## Chuẩn bị trước buổi học
## Kế hoạch thời gian
## Hướng dẫn theo từng chặng
## Bản đồ can thiệp
## Quy trình xử lý lỗi và phục hồi
## Tổng kết
## Bằng chứng cần lưu
## Sau buổi học
```

Yêu cầu cho từng phần:

- **Mục tiêu quan sát:** kết quả, quyết định của học viên và bằng chứng giảng viên phải thấy; không chép toàn bộ `README.md`.
- **Chuẩn bị:** công cụ và phiên bản, trạng thái ban đầu, kiểm thử tài khoản hoặc dữ liệu giả, kiểm tra liên kết, đường đặt lại và phương án dự phòng không phụ thuộc dịch vụ ngoài.
- **Kế hoạch thời gian:** bảng gồm chặng, số phút, hành động của học viên, AI, giảng viên và bằng chứng. Tổng thời gian phải khớp lộ trình hoặc ghi rõ phiên bản ngắn và đầy đủ.
- **Hướng dẫn theo từng chặng:** nêu câu hỏi mở đầu, chỉ dẫn cần nói, điểm quan sát và điều kiện chuyển bước; không viết bài thoại dài để đọc nguyên văn.
- **Bản đồ can thiệp:** nối dấu hiệu quan sát được với chẩn đoán khả dĩ, câu hỏi gợi mở đầu tiên, mức trợ giúp tối đa và thời điểm dừng hoặc thu hẹp phạm vi.
- **Quy trình xử lý lỗi và phục hồi:** cách kích hoạt lỗi an toàn, triệu chứng dự kiến, thao tác đặt lại hoặc hoàn tác và phương án khi môi trường khác dự kiến.
- **Tổng kết:** câu hỏi buộc học viên giải thích quyết định, bằng chứng, đóng góp của AI và điều sẽ làm khác; tránh lấy cảm nhận chung chung làm trọng tâm.
- **Bằng chứng cần lưu:** sản phẩm trung gian và phiên bản, kết quả đánh giá năng lực, thời gian hoàn thành, mức hỗ trợ, lỗi quan sát được và ghi chú phục vụ phân tích dạy thử.
- **Sau buổi học:** bàn giao sang mục tiêu hoặc buổi sau và tiêu chí để giao bài bổ trợ.

Không cho giảng viên sửa sản phẩm trung gian hoặc điều khiển tác nhân AI thay học viên. Mọi trợ giúp phải giữ quyền quyết định của học viên.

#### A.4.5 Cách viết `assessment.md`

`assessment.md` đánh giá năng lực học viên, không đánh giá chất lượng giáo trình và không sao chép điểm chất lượng 16 điểm.

Dùng cấu trúc bắt buộc:

```md
# Đánh giá năng lực: <Tên học phần>

## Khẳng định năng lực
## Thiết kế bằng chứng
## Bảng tiêu chí đánh giá
## Lỗi nghiêm trọng
## Cách thực hiện đánh giá
## Phản hồi và thử lại
## Quyết định bàn giao
```

Yêu cầu:

- **Khẳng định năng lực:** một câu chỉ khẳng định đúng kết quả mà bằng chứng có thể chứng minh; nêu rõ điều đánh giá không thể kết luận.
- **Thiết kế bằng chứng:** dùng bảng `outcome/decision → task → evidence location → criterion → review method`.
- **Bảng tiêu chí đánh giá:** mỗi tiêu chí dùng ba mức `Not yet`, `Meets`, `Extends` với hành vi/bằng chứng quan sát được; không dùng từ mơ hồ như “tốt”, “đủ hiểu”, “chuyên nghiệp” nếu không định nghĩa.
- **Lỗi nghiêm trọng:** lỗi về an toàn, kiểm chứng hoặc quyền sở hữu quyết định của học viên không được bù bằng tổng điểm.
- **Cách thực hiện:** ai đánh giá, thời điểm, giới hạn thời gian, công cụ hoặc hỗ trợ được phép, câu hỏi giải thích lại và cách tránh chấm độ trau chuốt của đầu ra AI thay cho năng lực học viên.
- **Phản hồi và thử lại:** mỗi tiêu chí `Not yet` phải dẫn tới một hành động sửa và bằng chứng mới cần nộp; không bắt học viên làm lại toàn bài nếu lỗi cục bộ.
- **Quyết định bàn giao:** điều kiện `Ready for next goal`, `Ready with remediation` hoặc `Not ready`, cùng sản phẩm trung gian được phép chuyển tiếp.

#### A.4.6 Cách viết `references.md`

Mọi mục tiêu phải có tệp này sau lượt khảo sát nền bắt buộc ở giai đoạn C, kể cả khi kết luận là giữ nguyên thiết kế.

Người nghiên cứu ở giai đoạn C sở hữu việc tạo và cập nhật tệp này. Các đơn vị soạn bài chỉ sử dụng mã khẳng định đã có; nếu phát hiện thiếu nguồn hoặc cần đổi phán quyết, phải trả một lượt kiểm tra có mục tiêu về giai đoạn C.

Dùng ba bảng:

```md
## Đối chiếu tiền lệ giáo trình

| Mã nguồn | Loại nguồn | Đối tượng/phạm vi | Kết quả và cấu trúc đáng chú ý | Điểm giống/khác | Khả năng áp dụng | Hệ quả thiết kế |
|---|---|---|---|---|---|---|

## Sổ khẳng định

| Mã khẳng định | Khẳng định | Loại khẳng định | Độ cập nhật cần thiết | Tác động quyết định | Mức rủi ro | Phán quyết | Ngày kiểm tra | Phiên bản/phạm vi | Vị trí sử dụng | Điều kiện kiểm tra lại | Ngày kiểm tra tiếp theo |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Sổ bằng chứng

| Mã khẳng định | Mã nguồn | Nguồn | Thẩm quyền | Ngày công bố/cập nhật | Ngày kiểm tra | Phiên bản/phạm vi | Chiều bằng chứng | Phần được hỗ trợ | Giới hạn |
|---|---|---|---|---|---|---|---|---|---|
```

Giá trị chuẩn cho `Độ cập nhật cần thiết` là `Stable`, `Version-bound` hoặc `Rapidly changing`; `Mức rủi ro` là `Low`, `Medium`, `High` hoặc `Critical`; `Chiều bằng chứng` là `Supporting`, `Falsifying` hoặc `Limiting`. `Ngày kiểm tra tiếp theo` dùng `YYYY-MM-DD` hoặc `—` nếu điều kiện kiểm tra lại không dựa trên ngày.

- Mỗi nguồn phải hỗ trợ, bác bỏ hoặc làm hẹp đúng khẳng định tại vị trí đã ghi trong bài học.
- Một khóa học tương tự chỉ là tiền lệ thiết kế, không tự là bằng chứng về hiệu quả sư phạm.
- Mọi điểm khác biệt phải được đánh giá bằng mục tiêu, đối tượng, ràng buộc và bằng chứng của chương trình; không đổi thiết kế chỉ để giống nguồn ngoài.
- Ghi cả bằng chứng hạn chế/chứng ngụy nếu nó làm hẹp chỉ dẫn.
- Không dùng bài tổng hợp khi có tài liệu chính thức, đặc tả hoặc nghiên cứu gốc phù hợp.
- Không sao chép toàn bộ tài liệu hướng dẫn; chỉ ghi kết luận cần cho quyết định dạy học.
- `references.md` là nguồn sở hữu cục bộ của khẳng định; lượt bảo trì dùng `refresh-volatile-content` để cập nhật sổ này và bàn giao mọi sửa đổi nội dung sang quy trình sở hữu.

#### A.4.7 Cách viết `review.md`

Người kiểm định tạo tệp này sau khi đọc đầu ra thật; Người soạn không được điền sẵn kết quả `Pass`.

Dùng cấu trúc:

```md
# Kiểm định chất lượng: <Tên học phần>

## Phạm vi và bằng chứng đã kiểm tra
## Phát hiện theo mức độ nghiêm trọng
## Các cổng bắt buộc
## Điểm chất lượng
## Truy vết xuyên tầng
## Kết luận
## Nội dung bắt buộc sửa
## Nhật ký kiểm định lại
```

- **Phạm vi và bằng chứng:** liệt kê phiên bản hoặc tệp đã đọc. Với bằng chứng chưa thể kiểm tra, ghi nguyên nhân, phần hoặc quyền truy cập còn thiếu, bên chịu trách nhiệm, bước tiếp theo và phạm vi kiểm định lại.
- **Phát hiện:** mỗi phát hiện có mức độ nghiêm trọng, vị trí, bằng chứng, hệ quả và thay đổi nhỏ nhất đủ tin cậy.
- **Các cổng bắt buộc:** dùng đúng tám cổng và ba phán quyết trong `.agents/rules/quality-gates.md`.
- **Điểm chất lượng:** giải thích từng điểm; áp dụng trần trước dạy thử.
- **Truy vết xuyên tầng:** ít nhất một dòng truy từ kế hoạch chung và mục tiêu qua hoạt động, sản phẩm trung gian, đánh giá năng lực tới bàn giao và lộ trình.
- **Kết luận:** tính trạng thái từ gate/score, không chọn trạng thái trước rồi điều chỉnh điểm.
- **Nhật ký kiểm định lại:** ghi phát hiện nào đã được sửa, bằng chứng mới và phán quyết mới; không xóa lịch sử phát hiện.

#### A.4.8 Cách viết `pilot-feedback-form.md`

Tệp này chỉ chuẩn bị công cụ thu thập dữ liệu cho lần dạy thử sau này; quy trình hiện tại không tự tổ chức hoặc phân tích buổi dạy thử.

Dùng cấu trúc bắt buộc:

```md
# Phiếu phản hồi sau bài học: <Tên học phần>

## Thông tin phiên học
## Mức độ hoàn thành
## Những điểm gây vướng mắc
## Cách bạn đã dùng AI
## Mức độ tự tin do học viên tự báo cáo — bằng chứng bổ trợ
## Phản hồi mở
## Đồng ý sử dụng dữ liệu
```

Yêu cầu:

- Chỉ thu dữ liệu cần để kiểm chứng độ rõ ràng, tính khả thi về thời gian và khả năng tự thực hiện của học viên.
- Kết hợp câu hỏi có thang đo với câu hỏi yêu cầu nêu tình huống hoặc bằng chứng cụ thể.
- Tách rõ nội dung học viên tự làm, AI hỗ trợ và giảng viên can thiệp.
- Không thu dữ liệu cá nhân không cần thiết; nêu rõ phạm vi sử dụng và quyền từ chối.
- Không tự suy ra chất lượng bài học từ một phản hồi đơn lẻ. Việc tổng hợp và kết luận thuộc `pilot-and-validate`.
- Không dùng mức độ tự tin tự báo cáo làm bằng chứng duy nhất để nâng điểm `Beginner clarity`, `Time feasibility` hoặc cấp trạng thái `Validated`.

#### A.4.9 Quy chuẩn viết chung cho mô hình nhẹ

1. Viết tiếng Việt rõ, câu trực tiếp; chỉ giữ thuật ngữ tiếng Anh khi đó là nhãn hoặc định danh học viên cần nhận diện trong công cụ, và giải thích ở lần đầu.
2. Mỗi phần mở bằng mục đích hoặc hành vi, không mở bằng định nghĩa hàn lâm dài.
3. Dùng cùng một tình huống xuyên suốt bài học; không đổi bối cảnh giữa phần giải thích, bài thực hành và đánh giá năng lực.
4. Mỗi ví dụ phải có nhãn `Ví dụ`, `Phản ví dụ` hoặc `Tình huống lỗi`; không để học viên nhầm đầu ra mẫu với yêu cầu bắt buộc.
5. Không phát minh dữ kiện, kết quả đo, hành vi công cụ hoặc thực hành tốt nhất. Chuyển khẳng định cần kiểm chứng sang giai đoạn C.
6. Không dùng nội dung độn như “AI đang thay đổi thế giới”, lịch sử chung hoặc danh sách lợi ích không tác động tới quyết định của học viên.
7. Không giả định học viên biết dòng lệnh, Git, cây tệp, JSON, API hoặc kiểm thử. Nếu cần, liên kết điều kiện tiên quyết hoặc hỗ trợ nền thao tác tối thiểu tại điểm dùng.
8. Mọi chỉ dẫn phải trả lời đủ: làm gì, dùng đầu vào nào, tạo đầu ra gì, biết đúng bằng cách nào và làm gì khi sai.
9. Giữ ranh giới trách nhiệm giữa các tệp; không sao chép cùng một đoạn nội dung vào nhiều tệp.
10. Khi bản định hướng không đủ để quyết định, ghi `Open question` trong bàn giao; không âm thầm lựa chọn thay người dùng.

#### A.4.10 Cổng kiểm tra cục bộ trước khi bàn giao từng tệp

| Tệp | Chỉ được bàn giao khi |
|---|---|
| `lesson.md` | Mọi khái niệm được dùng trong bài thực hành; có ví dụ yếu rồi được sửa; kết quả, sản phẩm trung gian và bàn giao nhất quán với `README.md`. |
| `practice.md` | Mỗi bước có đặc tả hoạt động; tổng thời lượng hợp lệ; có quyết định của học viên, phản biện đề xuất AI, bằng chứng, lỗi và phục hồi. |
| `instructor-guide.md` | Thời lượng khớp bài thực hành; can thiệp dựa trên dấu hiệu quan sát được; có phương án thiết lập dự phòng và cách lưu bằng chứng. |
| `assessment.md` | Mọi tiêu chí trỏ tới bằng chứng thật; bảng tiêu chí không chấm độ trau chuốt; có lỗi nghiêm trọng và cách thử lại. |
| `pilot-feedback-form.md` | Câu hỏi gắn với giả thuyết cần kiểm chứng; tách tự làm, AI hỗ trợ và giảng viên can thiệp; có thông báo sử dụng dữ liệu. |
| `references.md` | Có đối chiếu tiền lệ và khả năng áp dụng; mọi khẳng định có nguồn, ngày, phạm vi và vị trí; có bằng chứng làm hẹp/phản bác khi liên quan; không có trích dẫn mồ côi. |
| `review.md` | Người kiểm định đã đọc đầu ra thật; đủ cổng, điểm, truy vết, phát hiện và trạng thái; không có kết luận đạt khi thiếu bằng chứng. |

Tệp không qua cổng kiểm tra cục bộ phải được tác nhân AI sửa ngay trong đơn vị công việc hiện tại; không đẩy lỗi cấu trúc hiển nhiên sang kiểm định độc lập.

### A.5. Máy trạng thái

```text
Queued → Preflight
  ├── Awaiting input → Preflight
  ├── Conflict → Conflict classification
  │     ├── Local decision required → Awaiting decision → Preflight
  │     └── Architecture change required
  │           → Handoff: change-curriculum-architecture
  │           → Canonical sources updated
  │           → Re-entry: Preflight
  └── Learning design → Content trace → Baseline external research → Authoring

Authoring
  ├── Targeted claim check (if authoring reveals a material new claim) → Authoring
  └── Independent review
        ├── Finding disposition and adjudication
        │     ├── Accepted local repair → Independent review
        │     ├── Design revision → Learning design → Content trace refresh
        │     │     → Impact routing → Targeted authoring → Independent review
        │     ├── Disputed evidence → Independent adjudication or Awaiting adjudication
        │     └── Semantic/scope conflict → Conflict classification
        └── Quality recorded → Ready for handoff
```

Các nhãn trong sơ đồ là **trạng thái thực thi**, không phải trạng thái chất lượng. Sau kiểm định độc lập, Người kiểm định ghi một giá trị chất lượng trong `review.md`: `Needs revision`, `Pilot-ready` hoặc — trong trường hợp ngoại lệ nhưng hợp lệ theo quy tắc — `Release-ready`. `Ready for handoff` chỉ đạt khi giá trị đó là `Pilot-ready` hoặc `Release-ready`. `Validated` chỉ có thể được cấp bởi `pilot-and-validate` sau khi có bằng chứng dạy thử thực tế.

Mọi giai đoạn đang hoạt động có thể chuyển sang `Conflict classification` khi phát hiện mâu thuẫn về phạm vi, điều kiện tiên quyết, quan hệ phụ thuộc, lời hứa chương trình hoặc nguồn chuẩn. Không dùng nhánh này để xử lý lỗi nội dung cục bộ; lỗi đó quay về gói công việc sở hữu tệp.

Trước dạy thử, đích tự động hóa mặc định là `Pilot-ready`. Tổng điểm tối đa trước dạy thử là `14/16`; vì `Release-ready` cần ít nhất `13/16`, trạng thái này chỉ khả thi khi sáu tiêu chí không bị trần đạt tổng ít nhất `11/12` và hai tiêu chí bị trần đều đạt `1`. Chỉ ghi `Release-ready` khi Người kiểm định chứng minh không còn thay đổi bắt buộc đã biết; không dùng nó như một suy diễn rằng bài đã có bằng chứng pilot hoặc đã được phát hành.

### A.6. Vòng lặp hoàn thiện một mục tiêu

#### Giai đoạn A — Chọn và khóa đặc tả

**Vai trò:** Điều phối viên

1. Chọn mục tiêu tiếp theo từ hàng đợi và kiểm tra xem thư mục điều kiện tiên quyết đã có đầu ra cần thiết chưa.
2. Lập danh mục đầu vào theo phụ lục A.2; ghi rõ `Not applicable` hoặc `Missing input` cùng lý do thay vì suy đoán một đầu vào có tồn tại.
3. Đọc bản định hướng thiết kế; trích ra kết quả, phạm vi, quyết định của học viên, sản phẩm trung gian, bằng chứng, yêu cầu an toàn, đường xử lý lỗi và bàn giao.
4. Lập bản chụp hợp đồng trong báo cáo điều phối; không tạo thêm nguồn chuẩn có thẩm quyền mới.
5. Kiểm tra xung đột với kế hoạch chung, kiến trúc, bản đồ và lộ trình.
6. Nếu có đầu vào thiếu ảnh hưởng kết quả, bằng chứng hoặc an toàn, chuyển `Awaiting input` và dừng. Nếu có xung đột ảnh hưởng thiết kế, chuyển `Conflict` và dừng trước soạn bài. Nếu việc giải quyết đòi hỏi đổi mục tiêu, điều kiện tiên quyết, quan hệ phụ thuộc, lời hứa chương trình hoặc nguồn chuẩn, bàn giao sang `change-curriculum-architecture`; chỉ quay lại `Preflight` sau khi nguồn chuẩn đã được cập nhật và kiểm định.

**Điều kiện kết thúc:** đặc tả rõ, quan hệ phụ thuộc có sẵn hoặc được hỗ trợ nền hợp lệ, không còn xung đột chưa giải quyết.

#### Giai đoạn B — Thiết kế sản phẩm trung gian và khung nội dung

**Vai trò:** Người thiết kế; B0 do Người tích hợp dàn ý thực hiện

1. Dùng `$learner-artifact-design` để cụ thể hóa sản phẩm trung gian trong bản định hướng mà không đổi kết quả.
2. Dùng `$assessment-design` để lập ánh xạ `outcome → learner action → evidence → criterion → feedback → retry`.
3. Xác định quyết định thuộc về học viên và cách phân biệt nó với đầu ra do AI tạo.
4. Thiết kế ít nhất một tình huống lỗi có thể phát hiện và phục hồi an toàn.
5. Chốt bằng chứng tối thiểu trước khi viết phần giải thích.
6. Ghi `learning-design-contract.md` trong hồ sơ lượt chạy. Tệp phải có hợp đồng sản phẩm trung gian, ánh xạ đánh giá, quyết định của học viên, tình huống lỗi/phục hồi, bằng chứng tối thiểu và liên kết tới bản định hướng.
7. Chạy B0: đọc hợp đồng vừa tạo và lập `content-trace.md` với bảng truy vết nội dung, tình huống xuyên suốt, danh sách từ vựng, bản đồ quyền sở hữu tệp và câu hỏi cần đối chiếu với nguồn ngoài. Không viết văn bản diễn giải dài.

Đầu ra của B là bản thiết kế cam kết và khung nội dung đủ cụ thể để nghiên cứu so sánh, không phải bản nháp của các tệp bài học. D2 và D4 phải hiện thực hóa hợp đồng này mà không âm thầm đổi nó.

**Điều kiện kết thúc:** `learning-design-contract.md` và `content-trace.md` tồn tại; sản phẩm trung gian, đánh giá, dàn ý và câu hỏi nghiên cứu đủ cụ thể; chưa viết văn bản bài học.

#### Giai đoạn C — Khảo sát nguồn bên ngoài và phản biện khung nội dung

**Vai trò:** Người nghiên cứu

1. Đọc bản định hướng, `learning-design-contract.md` và `content-trace.md`; xác lập các câu hỏi so sánh về phạm vi, thứ tự, thực hành, sản phẩm và bằng chứng.
2. Gọi `$curriculum-reference-research` để chạy đúng một khảo sát nền cho mục tiêu, dùng ngân sách mặc định của skill.
3. Tìm cả tiền lệ giáo trình phù hợp và tài liệu chính thức hoặc nghiên cứu gốc cho các claim trọng yếu; mở nguồn gốc và tìm bằng chứng phản bác hoặc giới hạn.
4. Tạo `references.md` với bảng đối chiếu thiết kế, sổ khẳng định, sổ bằng chứng, phán quyết, giới hạn và hệ quả đề xuất.
5. Không coi nguồn ngoài là chuẩn. Giữ, sửa hoặc bác bỏ khung hiện tại bằng lập luận dựa trên mục tiêu, đối tượng, ràng buộc và chất lượng bằng chứng.
6. Nếu phát hiện yêu cầu sửa cục bộ khung thiết kế, trả đúng phần về B rồi cập nhật đối chiếu trước khi đóng C. Nếu phát hiện ảnh hưởng ranh giới mục tiêu, điều kiện tiên quyết hoặc cam kết chương trình, bàn giao sang `change-curriculum-architecture`.

Sau khi C đóng, không lặp lại toàn bộ khảo sát nền. Nếu D1–D6 làm lộ một claim trọng yếu mới, chạy lượt kiểm tra có mục tiêu cho claim đó và cập nhật `references.md` trước khi tiếp tục phần phụ thuộc.

**Điều kiện kết thúc:** khảo sát nền đã được ghi; mọi claim trọng yếu là `Supported`, `Partially supported` sau khi thu hẹp, hoặc `Inconclusive` có giới hạn không gây rủi ro; không giữ claim `Not supported` hay `Contradicted` trong thiết kế; mọi hệ quả đã được xử lý hoặc bàn giao.

#### Giai đoạn D — Soạn bộ tài liệu bài học

**Vai trò:** người soạn theo từng đơn vị công việc; đơn vị công việc giới hạn phạm vi đầu ra, không bắt buộc sinh một tác nhân mới cho mỗi đơn vị D1–D6.

1. Dùng `$lesson-authoring` làm hợp đồng soạn bài bao quát, nhưng gọi kỹ năng theo từng đơn vị công việc thay vì coi một lần gọi là đủ cho toàn giai đoạn.
2. Thực hiện tuần tự; mỗi đơn vị công việc chỉ được bắt đầu khi đầu ra trước đã qua cổng kiểm tra cục bộ:
   - **D1 — người soạn phần khái niệm:** gọi `$lesson-authoring`; chỉ viết `lesson.md` theo phụ lục A.4.2 và chạy cổng kiểm tra cục bộ của tệp.
   - **D2 — người soạn bài thực hành:** gọi `$lesson-authoring`; đọc `lesson.md` và `learning-design-contract.md`, chỉ viết `practice.md` theo phụ lục A.4.3 và kiểm tra tổng giới hạn thời gian.
   - **D3 — người soạn hướng dẫn giảng viên:** gọi `$lesson-authoring`; đọc bài học và bài thực hành, chỉ viết `instructor-guide.md` theo phụ lục A.4.4; không đổi nhiệm vụ của học viên để làm hướng dẫn dễ viết hơn.
   - **D4 — người thiết kế đánh giá năng lực:** gọi `$assessment-design`; đọc `learning-design-contract.md`, đặc tả sản phẩm trung gian và bằng chứng trong bài thực hành, rồi chỉ viết `assessment.md` theo phụ lục A.4.5. D4 hiện thực hóa bản thiết kế C, không thiết kế một hệ đánh giá thứ hai.
   - **D5 — người soạn phiếu phản hồi:** không có kỹ năng bắt buộc riêng; làm theo phụ lục A.4.8 và chỉ viết `pilot-feedback-form.md`. Không gọi `$pilot-feedback-analysis`, không thực hiện hoặc phân tích dạy thử.
   - **D6 — người tích hợp bộ tài liệu:** gọi `$lesson-authoring`; kiểm tra thuật ngữ, tình huống, đường dẫn, thời lượng, sản phẩm trung gian, bằng chứng, tài liệu tham khảo và bàn giao xuyên tệp. Chỉ sửa điểm thiếu nhất quán nhỏ; trả thay đổi nội dung về đơn vị sở hữu và trả claim trọng yếu chưa được kiểm chứng về giai đoạn C.
3. Mỗi đơn vị công việc báo cáo đầu vào đã đọc, tệp đã đổi, thành phần hợp đồng đã bao phủ, bằng chứng qua cổng cục bộ, câu hỏi còn mở và đơn vị công việc tiếp theo.
4. Liên kết tới tài nguyên dùng chung; không sao chép chính sách, mẫu hoặc bài thực hành.
5. D6 chạy kiểm tra cấu trúc, liên kết nội bộ, phần giữ chỗ, đặt tên và độ bao phủ của bảng truy vết nội dung trước khi chuyển kiểm định.

**Điều kiện kết thúc:** bộ tài liệu đủ để một giảng viên khác dạy thử mà không phải tự đoán hoạt động, bằng chứng hoặc cách xử lý lỗi.

#### Giai đoạn E — Kiểm định chất lượng độc lập

**Vai trò:** Người kiểm định độc lập, không dùng kết luận tự đánh giá của Người soạn làm bằng chứng

1. Gọi `$curriculum-quality-review` và đọc trực tiếp toàn bộ bộ tài liệu cùng các nguồn chuẩn.
2. Kiểm tra `references.md`: nguồn gốc đã được mở trực tiếp, đối chiếu không coi tiền lệ là chuẩn, claim trọng yếu có bằng chứng thuận/nghịch hoặc giới hạn, và hệ quả nghiên cứu truy được tới thiết kế hay nội dung.
3. Chấm từng cổng bắt buộc `Pass`, `Fail` hoặc `Not verified`, kèm tệp, phần hoặc hoạt động làm bằng chứng. Với `Not verified`, ghi nguyên nhân, bằng chứng hoặc quyền truy cập còn thiếu, bên chịu trách nhiệm, bước tiếp theo và phạm vi kiểm định lại.
4. Chấm đủ tám tiêu chí chất lượng; áp dụng trần trước dạy thử.
5. Truy vết `plan promise → goal outcome → external evidence → lesson activity → artifact → assessment → run checkpoint`.
6. Ghi phát hiện theo `Blocker`, `Major`, `Minor`, `Open question` và lưu vào `review.md`.
7. Không sửa nội dung trong lượt kiểm định đầu tiên.
8. Với mọi `Blocker`, `Major`, hard gate `Fail`/`Not verified` hoặc finding có thể đổi phạm vi, áp dụng mục 6.4 của [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). `review.md` giữ finding; `finding-disposition.md` trong hồ sơ lượt chạy giữ phản hồi, phân xử và liên kết kiểm định lại.

**Điều kiện kết thúc:** có kiểm định độc lập, có thể lặp lại và chỉ rõ thay đổi nhỏ nhất đủ tin cậy cho lỗi chặn hoặc lỗi `Major`.

#### Giai đoạn F — Vòng sửa có giới hạn

**Vai trò:** Bên sửa chịu trách nhiệm cho đơn vị công việc sở hữu tệp bị ảnh hưởng

1. Nhận bản định hướng thiết kế, bộ tài liệu hiện tại và phát hiện; không nhận nhiệm vụ “làm hay hơn” chung chung.
2. Trước khi sửa, bên sở hữu tệp phải ghi disposition theo mục 6.4 của `agent-dispatch-protocol.md`. Trong workflow này, phía thứ ba đánh giá `Out of scope` là Người thiết kế học tập hoặc Người tích hợp dàn ý không sở hữu tệp bị finding và độc lập với reviewer. `Not verified` chỉ được tạo sau khi cạn đường kiểm tra; nó khóa việc nâng trạng thái hoặc bàn giao phần phụ thuộc và chuyển `Awaiting adjudication` cho Chủ sở hữu giáo trình.
3. Chỉ finding `Accept` thuộc lỗi cục bộ mới được sửa tự động, theo thứ tự lỗi chặn → `Major` → `Minor` có lợi ích rõ. Phân loại finding trước khi sửa:
   - Với phát hiện do ranh giới mục tiêu, điều kiện tiên quyết, quan hệ phụ thuộc, lời hứa chương trình hoặc xung đột nguồn chuẩn, không sửa bài học. Bàn giao sang `change-curriculum-architecture` và chỉ quay lại `Preflight` sau khi nguồn chuẩn đã được cập nhật.
   - Với phát hiện cho thấy `learning-design-contract.md` không còn chứng minh được kết quả — như sản phẩm trung gian không lộ quyết định của học viên hoặc ánh xạ đánh giá không đủ bằng chứng — trả về B để sửa hợp đồng. Sau đó B0 phải cập nhật `content-trace.md`, C cập nhật phần nghiên cứu chịu ảnh hưởng; Điều phối viên xác định gói D bị ảnh hưởng và chỉ giao lại các gói đó. D2 và D4 thường bị ảnh hưởng, nhưng không được giả định D1, D3 hoặc D5 không bị ảnh hưởng nếu bảng truy vết nói khác.
   - Với lỗi cục bộ thuộc một tệp, trả về đúng đơn vị công việc sở hữu tệp đó.
4. Ghi ánh xạ `finding → file/change → expected evidence`.
5. Người kiểm định chạy lại mọi cổng bị ảnh hưởng và kiểm tra tính nhất quán của chuỗi truy vết. Reviewer đầu chỉ kiểm định lại finding `Accept` thuộc lỗi cục bộ; finding từng tranh chấp hoặc bị thu hẹp trọng yếu cần reviewer mới theo mục 6.4. Với nhánh sửa hợp đồng B, phạm vi kiểm định lại phải gồm hợp đồng đã sửa, `content-trace.md`, phần nghiên cứu C chịu ảnh hưởng và mọi gói D được định tuyến lại.

Giới hạn mặc định: tối đa **hai vòng sửa** cho cùng một bộ phát hiện. Sau hai vòng vẫn còn cùng lỗi chặn, tranh chấp hoặc `Not verified` trọng yếu, chuyển `Awaiting adjudication` cho Chủ sở hữu với mệnh đề đối lập, dossier bằng chứng và các phương án; không lặp vô hạn.

**Điều kiện kết thúc:** tất cả các cổng bắt buộc `Pass`, không có tiêu chí `0`, tổng điểm đạt ít nhất `11/16`, hoặc vấn đề đã được chuyển cấp trung thực.

#### Giai đoạn G — Bàn giao và đóng lượt chạy

**Vai trò:** Điều phối viên

1. Xác nhận `review.md` phản ánh đúng phiên bản hiện tại của bộ tài liệu.
2. Đọc trạng thái chất lượng do Người kiểm định ghi trong `review.md`; không tự chấm lại hoặc tự nâng trạng thái. Bàn giao nếu trạng thái là `Pilot-ready`, hoặc `Release-ready` khi Người kiểm định đã chứng minh điều kiện ngoại lệ này; không ghi `Validated` trước dạy thử phù hợp.
3. Tóm tắt đầu ra/sản phẩm trung gian mà mục tiêu kế tiếp được phép dùng.
4. Kiểm tra lộ trình chỉ liên kết tới bài học chuẩn, không sao chép nội dung.
5. Đối chiếu sổ đăng ký tác nhân với đầu ra và xác nhận lượt E đạt `Independent review verified`.
6. Đóng lượt chạy của mục tiêu hiện tại, rồi bàn giao việc chọn mục tiêu tiếp theo cho Điều phối viên. Nếu tiếp tục xây bài khác, phải tạo một lượt chạy mới; nếu dạy thử, tạo nhiệm vụ trong `pilot-and-validate`.

**Điều kiện kết thúc:** bộ tài liệu bài học, trạng thái kiểm định và quan hệ phụ thuộc bàn giao nhất quán.

### A.7. Mô hình điều phối và đặc tả lời nhắc

#### A.7.1. Phân biệt vai trò, đơn vị công việc và tác nhân

- **Vai trò** xác định trách nhiệm và điều không được làm.
- **Đơn vị công việc** xác định một đầu ra hẹp, tệp được phép sửa và cổng kiểm tra cục bộ.
- **Tác nhân** là một ngữ cảnh thực thi có thể đảm nhận một hoặc nhiều đơn vị công việc tương thích.

Tên vai trò hoặc mã B0/D1–D6 không phải lệnh tự động sinh tác nhân con. Điều phối viên phải tạo tác nhân tường minh khi cần và có thể tiếp tục giao đơn vị kế tiếp cho cùng tác nhân nếu việc giữ mạch giúp tăng tính nhất quán.

Khi chạy quy trình, gọi `$workflow-orchestration` và áp dụng `.agents/workflows/agent-dispatch-protocol.md` trước mỗi đơn vị công việc. Cấu trúc dưới đây chỉ là gợi ý để Điều phối viên đánh giá sau khi đã có ngữ cảnh:

```text
ROOT ORCHESTRATOR
  ├── Learning-design agent: B → B0
  ├── Research agent: C
  ├── Authoring agent: D1 → D2 → D3
  ├── Assessment agent: D4
  ├── Feedback-form agent: D5, or reuse the authoring agent
  ├── Integration agent: D6
  ├── Independent review agent: E
  ├── Evidence adjudicator: only for material disputed findings
  ├── Owning agent repair: F → affected work unit
  └── ROOT ORCHESTRATOR: A and G
```

Quy tắc áp dụng:

1. Điều phối viên chính giữ mục tiêu của lượt chạy, phiên bản đầu ra, trạng thái và các lượt bàn giao; nó thực hiện A và G.
2. Mỗi mục tiêu đều phải chạy khảo sát nền C. Tác nhân nghiên cứu và tác nhân thiết kế học tập được tách khi khối lượng hoặc nhu cầu cô lập lập luận đủ lớn; nếu dùng cùng một tác nhân, hai vai trò vẫn phải có hợp đồng công việc và đầu ra tách biệt.
3. Một tác nhân soạn bài có thể thực hiện tuần tự D1–D3 bằng các lời nhắc riêng. Sau mỗi đơn vị, nó phải ghi đầu ra vào tệp và vượt cổng cục bộ trước khi nhận đơn vị tiếp theo.
4. D4 dùng tác nhân có kỹ năng `$assessment-design` để tránh việc phần giải thích tự quyết định cách nó được chấm.
5. D5 có thể dùng lại tác nhân soạn bài vì đây là công cụ thu dữ liệu trước dạy thử, không phải kết luận kiểm định. Không gọi `$pilot-feedback-analysis` ở đây.
6. D6 nên dùng một tác nhân tích hợp khác tác nhân soạn D1–D3 khi có đủ năng lực thực thi. D6 chỉ kiểm tra tính nhất quán và không thay E.
7. E bắt buộc dùng tác nhân hoặc lượt thực thi mới không tham gia B–D. Người kiểm định đọc nguồn chuẩn và tệp đầu ra trực tiếp, không nhận bản tóm tắt kết luận của Người soạn làm bằng chứng.
8. F không mặc định giao cho một “tác nhân sửa bài” chung. Phát hiện cục bộ quay về đơn vị sở hữu tệp; phát hiện làm sai hợp đồng B quay về B rồi B0 lập lại bảng truy vết và C cập nhật phần nghiên cứu chịu ảnh hưởng trước khi định tuyến các gói D; sau đó E kiểm định lại phạm vi chịu ảnh hưởng.
9. Không sinh tác nhân mới chỉ để đổi tên vai trò. Tách tác nhân khi cần chuyên môn khác, cô lập ngữ cảnh, thực hiện độc lập hoặc đáp ứng yêu cầu kiểm định.

Nếu môi trường không hỗ trợ tác nhân con, có thể chạy các đơn vị tuần tự trong cùng tác nhân chính và dùng tệp làm điểm bàn giao. Cách này vẫn dùng được cho A–D, F và G, nhưng một lần “đổi vai” trong cùng ngữ cảnh không tạo ra kiểm định độc lập. Khi chưa có một lượt E độc lập, `review.md` phải ghi `Not verified` cho điều kiện độc lập và bài học chưa được nâng lên `Pilot-ready` hay `Release-ready`.

Ràng buộc phân công riêng của quy trình này:

```text
Required isolation: E; a fresh Evidence adjudicator for material disputed findings
Preferred continuity: B → B0; D1 → D2 → D3
Conditional specialists: C, D4, D6
Reusable unit: D5 may reuse the authoring agent
Repair routing: F → owning work unit
Parallel-safe units: only read-only research with non-overlapping claims
Shared-file exclusion: one writer per lesson file
Spawn verification: required before the first delegated work unit in an unverified runtime
```

#### A.7.2. Đặc tả lời nhắc cho tác nhân AI nhẹ

Mỗi lượt chỉ giao một vai trò, một giai đoạn và một gói công việc. Giai đoạn A và G dùng vai trò Điều phối viên; các giai đoạn còn lại dùng vai trò chuyên trách tương ứng. “Giai đoạn” chỉ vị trí trong vòng đời; “gói công việc” chỉ phần việc hẹp có đầu ra và quyền ghi riêng. Lời nhắc tối thiểu phải có:

```text
Role: <Coordinator | Researcher | Learning designer | Lesson author | Assessment designer | Feedback-form author | Integrator | Independent reviewer | Evidence adjudicator | Repair owner>
Goal folder: <ai-native-builder/goals/gNN-*>
Mode: <Full completion | Targeted repair>
Phase: <A | B | C | D | E | F | G>
Work package: <A1-A6 | B1-B7 and B0 | C1-C6 | D1-D6 | E1-E6 | F1-F5 | G1-G6>
Allowed files: <explicit file list>
Canonical inputs: <required files to read>
Required skills: <ordered `$skill-name` values or None>
Required outputs: <files, sections, evidence, and finding disposition/adjudication when applicable>
Decision status: <Not required | Awaiting decision | Confirmed | Awaiting adjudication>
Local gate: <pass conditions from section 7 and Appendix A.4.10>
Stop conditions: <conflict, missing input, unsafe action, scope change, failed gate>
Do not: <change goals, copy shared content, raise status, expand scope, self-approve>
```

Không giao cùng lúc nghiên cứu, soạn bài, kiểm định và sửa bài cho một tác nhân AI nhẹ. Trong giai đoạn D, mặc định `Allowed files` chỉ chứa một tệp đầu ra; D6 là ngoại lệ nhưng chỉ được sửa điểm thiếu nhất quán nhỏ. Bàn giao phải dựa trên tệp và bằng chứng, không dựa vào trí nhớ hội thoại.

### A.8. Hồ sơ tiến độ của lượt chạy

Trong quy trình này, một `run-id` chỉ bao phủ đúng một vòng hoàn thiện cho một mục tiêu `gNN`. Điều phối viên tạo `run-id` mới khi bắt đầu mục tiêu khác, kể cả khi mục tiêu đó đứng kế tiếp trong `ai-native-builder/curriculum-map.md`.

Khi bắt đầu hoặc tiếp tục lượt chạy hiện tại, Điều phối viên duy trì đúng một sổ vận hành tại `.agents/workflow-runs/<run-id>/progress-tracker.md`. Sổ ghi mã mục tiêu lấy từ `ai-native-builder/curriculum-map.md`, nhưng không được sửa bản đồ này.

```text
| Goal ID | Workflow state | Current phase | Input status | Blocking issue | Review file | Quality status at last check | Next action |
|---|---|---|---|---|---|---|---|
```

`progress-tracker.md` chỉ ghi tiến độ thực thi, lỗi chặn và liên kết tới bằng chứng. `review.md` trong thư mục mục tiêu là nguồn duy nhất cấp trạng thái chất lượng và phát hiện kiểm định; sổ tiến độ chỉ ghi giá trị được đọc từ `review.md` cùng thời điểm kiểm tra, không tự tạo hay đổi phán quyết. Không sao chép nội dung bài học hoặc kiểm định bằng chứng chi tiết vào sổ này.

### A.9. Rào chắn chống “sản xuất rác hàng loạt”

- Không soạn hàng loạt mọi mục tiêu trong một lượt trước khi bài học đầu tiên đi hết vòng lặp và quy trình được hiệu chỉnh.
- Chạy thử quy trình xây dựng với **G01**, sau đó với một mục tiêu có điểm chạm mã nguồn hoặc công cụ như **G04** hoặc **G07** trước khi mở rộng.
- Không dùng số tệp, số chữ, giao diện đẹp hoặc việc tác nhân AI tự báo thành công làm bằng chứng hoàn thành.
- Không cho người soạn tự xóa hoặc hạ mức phát hiện trong `review.md`; người kiểm định phải xác nhận bằng bằng chứng mới.
- Không sửa chuẩn đặc tả mục tiêu để làm đầu ra hiện tại dễ đạt.
- Không tiếp tục mục tiêu sau nếu sản phẩm trung gian điều kiện tiên quyết chưa đủ dùng thật.
- Không đẩy lỗi thiếu tiêu đề, liên kết hỏng, phần giữ chỗ, thời lượng lệch hoặc bảng tiêu chí đánh giá không trỏ bằng chứng sang Người kiểm định; cổng kiểm tra cục bộ phải bắt các lỗi này trước.
- Không yêu cầu một mô hình nhẹ tạo toàn bộ bộ tài liệu trong một lời nhắc.

### A.10. Tiêu chí duyệt quy trình (lịch sử)

Đây là bản tiêu chí lịch sử được giữ để truy vết; không thay thế cổng hiện hành
ở mục 11. Khi workflow còn `Proposed`, chỉ chuyển sang `Active` khi người dùng
chấp nhận:

1. Một mục tiêu mỗi vòng lặp thay vì làm hàng loạt;
2. Đầu ra bộ tài liệu mặc định gồm bảy tệp ngoài `README.md`: năm tệp do người soạn sở hữu, một `references.md` do Người nghiên cứu sở hữu và một `review.md` do Người kiểm định độc lập sở hữu;
3. Sản phẩm trung gian/đánh giá năng lực được thiết kế trước văn bản diễn giải;
4. Người soạn và Người kiểm định là hai vai trò tách biệt;
5. Tối đa hai vòng sửa trước khi chuyển cấp;
6. Chạy thử quy trình xây dựng trên G01 rồi một mục tiêu có điểm chạm mã nguồn hoặc công cụ;
7. `Pilot-ready`, hoặc `Release-ready` khi đủ điều kiện, là đích tự động hóa trước dạy thử; không phải `Validated`.
8. Khung thiết kế và `content-trace.md` được hoàn tất ở B/B0; khảo sát nguồn bên ngoài chạy một lần ở C trước khi D1–D6 soạn nội dung; mỗi tệp đầu ra có cấu trúc và cổng kiểm tra cục bộ bắt buộc.
9. Skill nghiên cứu quy định công cụ theo năng lực, ngân sách, điều kiện dừng, nguồn được phép dùng và hợp đồng đầu ra; không dùng trí nhớ mô hình thay nguồn không truy được.
10. Mọi lượt sinh tác nhân và kiểm định độc lập có bằng chứng theo `agent-dispatch-protocol.md`; thiếu bằng chứng phải giữ `Not verified`.

Sau khi được duyệt, đồng bộ trạng thái trong workflow này, `.agents/workflows/README.md`
và root `README.md`, rồi tạo sổ theo dõi tiến độ trước lượt chạy đầu tiên.
