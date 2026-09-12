# Giao thức phân công tác nhân khi chạy quy trình

- **Trạng thái:** `Proposed — kiểm chứng qua từng lượt chạy thực tế`
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
  └── Defer until prerequisites are resolved
  ↓
EXECUTE
  ↓
VERIFY OUTPUT
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
| Hành động phân công | `root`, `reuse`, `spawn`, `fresh-review` hoặc `defer` |
| Lý do | Kết quả cổng phân công |
| Tệp được phép sửa | Danh sách chính xác hoặc `none` |
| Đầu vào | Tệp và bằng chứng đã truyền |
| Thời điểm | Bắt đầu và kết thúc |
| Trạng thái | `queued`, `running`, `completed`, `failed`, `cancelled` hoặc `not-verified` |
| Đầu ra | Tệp, thông điệp kết quả và phép kiểm tra |

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

Với từng hành động `spawn` hoặc `fresh-review`, phải có:

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
