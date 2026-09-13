# Giao thức phân công tác nhân khi chạy quy trình

- **Trạng thái:** `Active` — đã được người dùng duyệt
- **Mục tiêu:** giúp Điều phối viên quyết định tại thời điểm thực thi nên tự làm, tái sử dụng tác nhân, sinh tác nhân mới hay chờ đầu vào.
- **Áp dụng:** mọi quy trình có từ hai vai trò trở lên hoặc yêu cầu kiểm định độc lập.

Vai trò, đơn vị công việc và tác nhân là ba khái niệm khác nhau. Quy trình chuyên môn xác định việc phải làm; giao thức này xác định cách phân công sau khi ngữ cảnh thực tế đã xuất hiện.

## 1. Điều kiện bắt đầu

Điều phối viên chỉ phân công khi đã có một đơn vị công việc với:

- một kết quả cần đạt;
- đầu vào hiện có và đầu vào còn thiếu;
- tệp được phép đọc hoặc sửa;
- kỹ năng cần dùng;
- điều kiện đạt và điều kiện dừng;
- quan hệ phụ thuộc với đơn vị khác.

Nếu chưa lập được hợp đồng trên, Điều phối viên tiếp tục làm rõ phạm vi thay vì sinh tác nhân để khám phá không giới hạn.

## 2. Vòng điều phối động

```text
ENTER WORK UNIT
  ↓
BUILD TASK CONTRACT
  ↓
DELEGATION GATE
  ├── Execute in root agent
  ├── Reuse an existing agent
  ├── Spawn a specialist agent
  ├── Spawn a fresh independent reviewer
  ├── Spawn a fresh evidence adjudicator
  └── Defer until prerequisites are resolved
  ↓
EXECUTE
  ↓
VERIFY OUTPUT
  ├── No material finding → UPDATE AGENT REGISTRY
  └── Material finding → DISPOSITION AND ADJUDICATION (6.4)
  ↓
UPDATE AGENT REGISTRY
  ↓
NEXT WORK UNIT
```

Cổng phân công được chạy khi bắt đầu một đơn vị công việc, sau thay đổi phạm vi và trước khi giao lại việc sửa sau kiểm định. Sơ đồ tác nhân trong từng quy trình chỉ là cấu trúc gợi ý, không thay thế cổng này.

## 3. Cổng phân công

Điều phối viên trả lời theo thứ tự:

1. Công việc có cần quyết định của con người không?
2. Phạm vi, đầu vào và điều kiện đạt đã đủ rõ chưa?
3. Có kết quả tiên quyết chưa hoàn thành không?
4. Có bắt buộc độc lập với người tạo đầu ra không?
5. Có tác nhân hiện hữu đang sở hữu đúng chuỗi suy luận không?
6. Công việc có chuyên môn riêng, đủ lớn và khép kín để đáng tách không?
7. Có thể chạy song song mà không đọc kết quả chưa ổn định hay sửa cùng tệp không?
8. Còn vị trí thực thi và ngân sách phù hợp không?

```text
if task.requires_human_decision:
    keep_in_root_and_await_decision
elif task.requires_evidence_adjudication:
    spawn_fresh_evidence_adjudicator
elif task.requires_independent_review:
    spawn_fresh_reviewer
elif task.has_unresolved_scope or task.has_missing_prerequisites:
    defer
elif existing_agent.owns_reasoning_chain(task):
    reuse_existing_agent
elif task.is_bounded and task.has_acceptance_criteria and task.has_no_file_collision:
    spawn_specialist_agent
else:
    execute_in_root
```

### 3.1. Bắt buộc sinh lượt mới

- Kiểm định độc lập đầu ra do tác nhân khác tạo hoặc sửa.
- Phản biện độc lập khi quy trình yêu cầu hai cách lập luận tách biệt.
- Phân xử dữ kiện theo mục 6.4 sau khi reviewer và bên thực hiện vẫn bất đồng trọng yếu.
- Công việc cần cô lập ngữ cảnh theo quy tắc hoặc quyết định đã duyệt.

Lượt kiểm định độc lập phải dùng ngữ cảnh mới, ưu tiên không kế thừa hội thoại. Chỉ truyền nguồn chuẩn, tệp đầu ra, tiêu chí, phạm vi và câu hỏi kiểm định.

### 3.2. Ưu tiên tái sử dụng tác nhân

- Các đơn vị kế tiếp cùng sử dụng một mô hình vấn đề hoặc tình huống xuyên suốt.
- Lượt sửa quay về đúng tệp và trách nhiệm mà tác nhân đó sở hữu.
- Chi phí tái tạo ngữ cảnh lớn hơn lợi ích cô lập.

### 3.3. Không sinh tác nhân

- Phạm vi hoặc tiền đề đang tranh chấp.
- Chưa có tiêu chí nghiệm thu hoặc danh sách tệp cho phép.
- Hai tác nhân sẽ sửa cùng một tệp.
- Công việc quá nhỏ so với chi phí bàn giao và kiểm tra.
- Tác nhân mới phải dựa chủ yếu vào trí nhớ hội thoại chưa được ghi thành tệp.

## 4. Quy tắc chạy song song và sở hữu tệp

- Chỉ chạy song song các đơn vị không phụ thuộc kết quả của nhau.
- Một tệp chỉ có một tác nhân được quyền ghi tại một thời điểm.
- Điều phối viên giữ quyền ghi duy nhất đối với sổ đăng ký tác nhân.
- Tác nhân con không tự sinh thêm tác nhân nếu hợp đồng không cho phép.
- Khi hết vị trí thực thi, ưu tiên kiểm định bắt buộc, công việc chặn đường phụ thuộc, rồi mới tới nghiên cứu hoặc cải tiến không chặn.

## 5. Sổ đăng ký tác nhân

Mỗi lượt chạy tạo một hồ sơ tại:

```text
.agents/workflow-runs/<run-id>/orchestration-log.md
```

Điều phối viên ghi một hàng cho cả công việc tự thực hiện và công việc giao đi:

| Trường | Nội dung bắt buộc |
|---|---|
| Mã lượt | Mã ổn định của lần phân công |
| Định danh tác nhân | Mã tác nhân hoặc tên nhiệm vụ chuẩn do công cụ điều phối trả về; không dùng tên vai trò tự đặt thay thế |
| Tác nhân cha | Mã của Điều phối viên hoặc tác nhân được phép phân công |
| Vai trò và đơn vị | Trách nhiệm cùng mã giai đoạn |
| Hành động phân công | `root`, `reuse`, `spawn`, `fresh-review`, `fresh-adjudication` hoặc `defer` |
| Lý do | Kết quả cổng phân công |
| Tệp được phép sửa | Danh sách chính xác hoặc `none` |
| Đầu vào | Tệp và bằng chứng đã truyền |
| Thời điểm | Bắt đầu và kết thúc |
| Trạng thái | `queued`, `running`, `completed`, `failed`, `cancelled` hoặc `not-verified` |
| Đầu ra | Tệp, thông điệp kết quả và phép kiểm tra |
| Finding/phân xử | Mã finding, disposition, kết quả phân xử hoặc `none` |

Không ghi thông tin bí mật, toàn bộ chuỗi suy luận nội bộ hoặc nội dung hội thoại dài vào sổ.

## 6. Kiểm chứng việc tác nhân đã thực sự được sinh

Không dùng câu “đã giao cho tác nhân khác” làm bằng chứng. Điều phối viên phải dựa trên dữ liệu do công cụ điều phối trả về.

### 6.1. Phép thử khả năng khi bắt đầu

Chạy khi quy trình dự kiến cần tác nhân con và chưa có kết quả thử tương thích với phiên môi trường hiện tại:

1. Tạo một mã ngẫu nhiên không chứa dữ liệu nhạy cảm.
2. Yêu cầu sinh một tác nhân thăm dò không được sửa tệp và chỉ trả lại mã đó cùng tên nhiệm vụ chuẩn của nó.
3. Ghi mã tác nhân hoặc tên nhiệm vụ chuẩn từ kết quả tạo tác nhân.
4. Chờ đúng tác nhân đó hoàn thành và đối chiếu mã trả về.
5. Ghi `Spawn verified` chỉ khi định danh do công cụ trả về khác Điều phối viên, quan hệ cha–con quan sát được và thông điệp trả về khớp.
6. Đóng tác nhân thăm dò trước khi bắt đầu công việc thật.

```text
Probe task: Return "SPAWN_PROBE:<nonce>" and your canonical task name.
Allowed files: none
Expected evidence: tool-issued child identifier + observable parent relation + matching nonce + completed status
```

### 6.2. Kiểm chứng mỗi lần phân công

Với từng hành động `spawn`, `fresh-review` hoặc `fresh-adjudication`, phải có:

- mã tác nhân hoặc tên nhiệm vụ chuẩn mới do công cụ trả về;
- quan hệ cha–con hoặc đường nhiệm vụ chuẩn;
- hợp đồng công việc đã gửi;
- trạng thái hoàn thành, thất bại hoặc bị ngắt;
- đầu ra được Điều phối viên kiểm tra tại vị trí đã cam kết.

Thiếu một trong các bằng chứng trên thì ghi `Spawn not verified`; không được coi tác nhân mới đã tồn tại chỉ dựa trên văn phong khác hoặc lời tự nhận.

### 6.3. Kiểm chứng tính độc lập của Người kiểm định

Để ghi `Independent review verified`, sổ phải chứng minh:

1. Định danh Người kiểm định khác mọi định danh đã tạo hoặc sửa đầu ra được kiểm định.
2. Lượt kiểm định được sinh mới thay vì tái sử dụng tác nhân soạn hay thực hiện.
3. Gói đầu vào không chứa kết luận tự đánh giá của người tạo như bằng chứng bắt buộc phải tin.
4. Người kiểm định đọc trực tiếp nguồn chuẩn và đầu ra.
5. Kết luận có dẫn chứng tệp/phần và được trả về độc lập.

Nếu môi trường không cung cấp mã tác nhân hoặc không thể tạo ngữ cảnh mới, ghi `Independent review not verified`. Có thể tự kiểm tra để sửa lỗi, nhưng không được cấp `Pass` tại cổng yêu cầu độc lập.

### 6.4. Phản biện và phân xử finding trọng yếu

Áp dụng mục này thay cho vòng đơn giản `review → repair → re-review` khi một reviewer độc lập nêu finding có thể làm đổi kết quả, trạng thái chất lượng, phạm vi, bằng chứng bắt buộc hoặc bàn giao. Workflow chuyên môn có thể bổ sung cổng an toàn chặt hơn, nhưng không được bỏ các rào chắn dưới đây.

Mỗi finding ghi trong tệp review do workflow chuyên môn chỉ định (`review-findings.md` nếu có, nếu không là `review.md`); phản hồi ghi bổ sung, không ghi đè, vào `finding-disposition.md` trong hồ sơ lượt chạy. Reviewer sở hữu mệnh đề, mức độ và bằng chứng của finding; bên thực hiện sở hữu phản hồi, commit sửa và bằng chứng phản hồi; Điều phối viên chỉ kiểm tra đủ trường và định tuyến. Không bên nào tự sửa phần hồ sơ thuộc sở hữu của bên kia.

```text
Finding
  → disposition by owner of the affected work
  → Accept → bounded repair → re-review
  → Dispute / Need evidence → one reviewer response
       → resolved → repair, narrow, or withdraw
       → material disagreement → independent evidence adjudication
  → Out of scope → two-of-three scope confirmation → handoff
  → Requires human decision → Awaiting adjudication
```

`Accept`, `Dispute`, `Need evidence`, `Out of scope` và `Requires human decision` là các disposition hợp lệ. Mọi disposition phải chỉ rõ mệnh đề đang tranh luận, nguồn/tệp đã đọc, thay đổi hoặc bàn giao dự kiến, và phép kiểm tra sẽ xác nhận kết quả. Không giao sửa trước disposition; khuyến nghị của reviewer không tự là lệnh sửa.

**Out of scope.** Ba phía đánh giá là: bên thực hiện, reviewer và một Người đánh giá ảnh hưởng độc lập với hai bên kia. Mỗi phía phải đối chiếu finding với quyết định đã khóa, danh sách tệp được duyệt và impact map. Chỉ bàn giao `Out of scope` khi ít nhất hai trong ba phía xác nhận, đồng thời ghi workflow nhận, chủ sở hữu và điều kiện tái nhập. Điều phối viên không là một phiếu nội dung. Với finding `High`/`Critical`, hoặc khi reviewer phản đối việc coi là ngoài phạm vi, không được dùng đa số để bỏ qua rủi ro: chuyển `Awaiting adjudication` cho Chủ sở hữu.

**Tranh chấp dữ kiện.** Sau một phản hồi của reviewer, finding còn bất đồng trọng yếu phải được một Người phân xử bằng chứng độc lập kiểm tra. Người này khác cả bên thực hiện lẫn reviewer đầu, và nhận dossier gồm: nguồn chuẩn/quyết định đã khóa, baseline hoặc phiên bản kiểm định, finding nguyên gốc, disposition, diff hoặc đầu ra liên quan, evidence hai phía, impact map và câu hỏi phân xử. Người phân xử chỉ có thể `Uphold`, `Narrow`, `Withdraw` hoặc `Not verified`; nếu kết quả đòi đổi mục tiêu, phạm vi hay đánh đổi, nó phải chuyển sang cổng quyết định của con người.

**`Not verified` của một finding là trạng thái đã cạn đường kiểm tra, không phải cách né quyết định.** Chỉ được ghi khi: mệnh đề và tiêu chí bằng chứng đã rõ; bên thực hiện đã phản hồi; reviewer đã trả lời một lần; nguồn khả dụng theo ngân sách đã được kiểm tra; Người phân xử bằng chứng xác nhận không đủ dữ kiện hoặc không thể truy cập dữ kiện quyết định; và không thể thu hẹp an toàn về phần còn kiểm chứng được. Khi đó Điều phối viên ghi `Awaiting adjudication`, thông báo Chủ sở hữu và khóa việc tích hợp, nâng trạng thái hoặc sử dụng phần phụ thuộc. Công việc thật sự độc lập có thể tiếp tục trên nhánh/lượt riêng. Chủ sở hữu chọn: bổ sung bằng chứng, thu hẹp phạm vi, trì hoãn/giữ trạng thái, hoặc từ chối–hoàn tác; không có thời hạn vắng mặt nào tự biến `Not verified` thành `Pass`. Quy tắc này không thay thế `Independent review not verified` ở mục 6.3: thiếu lượt reviewer độc lập cũng luôn chặn `Pass`, nhưng được ghi như lỗi năng lực runtime thay vì finding đã phân xử.

Reviewer đầu chỉ re-review finding `Accept` thuộc lỗi triển khai cục bộ. Finding từng `Dispute`, `Need evidence`, bị thu hẹp/rút ở mức trọng yếu, hoặc tác động nguồn chuẩn, trạng thái chất lượng hay lời hứa phải có lượt review mới xác nhận kết quả cuối. Giới hạn số vòng sửa do workflow chuyên môn đặt ra; hết giới hạn thì chuyển `Awaiting adjudication`, không tiếp tục tranh luận tự động.

### 6.5. Kiểm chứng tính độc lập của Người phân xử bằng chứng

Để công nhận một kết quả phân xử, sổ phải chứng minh Người phân xử có định danh mới khác cả bên thực hiện lẫn reviewer đầu, nhận đúng dossier quy định ở mục 6.4, đọc trực tiếp các nguồn/tệp được tranh luận và trả về một trong bốn kết quả được phép. Nếu thiếu năng lực này, không thay reviewer đầu bằng một “vai trò mới” cùng ngữ cảnh; ghi finding là chưa đủ điều kiện phân xử và chuyển `Awaiting adjudication` cho Chủ sở hữu.

## 7. Xử lý thất bại và cải tiến

| Dấu hiệu | Chẩn đoán cần ghi | Hướng xử lý |
|---|---|---|
| Không có công cụ sinh tác nhân | Khả năng không được cung cấp trong phiên | Chạy tuần tự; giữ cổng độc lập ở `Not verified` |
| Lệnh sinh thành công nhưng không có định danh mới | Không đủ bằng chứng về tiến trình riêng | Không công nhận lượt tách; kiểm tra cấu hình môi trường |
| Tác nhân không nhận đúng đầu vào | Gói ngữ cảnh thiếu hoặc sai | Sửa hợp đồng và thử lại một lần |
| Hai tác nhân sửa cùng tệp | Lỗi khóa phạm vi | Dừng cả hai, chọn một bên sở hữu và kiểm tra phần chênh lệch |
| Tác nhân mới lặp lại kết luận của người viết | Cô lập ngữ cảnh không đủ | Sinh lại lượt kiểm định với ngữ cảnh sạch hơn |
| Chi phí bàn giao vượt lợi ích | Phân mảnh quá mức | Gộp chuỗi công việc tương thích và tái sử dụng tác nhân |

Sau mỗi lượt chạy thử, ghi điều kiện phân công nào hoạt động sai, bằng chứng và thay đổi đề xuất. Không sửa tiêu chí chỉ để hợp thức hóa một lần chạy thất bại.

## 8. Điều kiện đạt của giao thức

Một lượt điều phối chỉ đạt khi:

- mọi quyết định sinh, tái sử dụng, tự làm hoặc trì hoãn có lý do;
- không có xung đột ghi tệp;
- mọi tác nhân con có bằng chứng vòng đời và đầu ra;
- lượt kiểm định bắt buộc có bằng chứng độc lập hoặc được ghi trung thực `Not verified`;
- sổ đăng ký đủ để tái dựng ai đã làm gì mà không dựa vào hội thoại.
