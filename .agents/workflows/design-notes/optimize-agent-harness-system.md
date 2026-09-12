# Kế hoạch khung hoàn thiện `optimize-agent-harness-system`

- **Loại tài liệu:** Ghi chú thiết kế, không phải kế hoạch thực thi.
- **Workflow liên quan:** [`optimize-agent-harness-system.md`](../optimize-agent-harness-system.md).
- **Trạng thái:** Đang thiết kế.
- **Mục tiêu gần:** Chuẩn bị đủ quyết định và đặc tả để Chủ sở hữu kho có thể cân nhắc chuyển workflow từ `Placeholder` sang `Proposed`.
- **Không cho phép:** Chạy workflow, giao agent sửa harness, di trú metadata toàn kho hoặc coi các phương án dưới đây là quyết định đã chấp thuận.

## 1. Kết quả cần có trước khi đề nghị `Proposed`

Thiết kế hoàn chỉnh phải tạo được:

1. Đặc tả đầu vào, đầu ra và điều kiện bắt đầu của một lượt tối ưu harness.
2. Cách thu bằng chứng, lập đường cơ sở và phân loại nguyên nhân.
3. Các giai đoạn, cổng quyết định, điều kiện dừng và trạng thái của lượt chạy.
4. Ma trận vai trò, quyền sở hữu tệp và hợp đồng cho từng work unit.
5. Cơ chế thử có kiểm soát, kiểm thử dương, kiểm thử âm và kiểm tra hồi quy.
6. Kế hoạch rollback và cách xử lý đầu ra thử nghiệm.
7. Cổng kiểm định quản trị độc lập và thẩm quyền chấp thuận của con người.
8. Quy tắc di trú khi thay đổi chạm nhiều rules, skills hoặc workflows.
9. Một hợp đồng pilot đủ hẹp để kiểm chứng workflow mà không áp dụng hàng loạt.

## 2. Các quyết định thiết kế cần chốt

### 2.1. Điều kiện kích hoạt

Cần xác định bằng chứng nào đủ để mở một lượt, chẳng hạn lỗi lặp lại, ranh giới mơ hồ, sai lệch có tác động cao, công cụ thay đổi hoặc chi phí vận hành bất hợp lý. Cần phân biệt:

- Quan sát đơn lẻ cần ghi nhận nhưng chưa cần thay đổi.
- Mẫu hình đủ để điều tra.
- Sự cố nghiêm trọng cần chặn ngay đường thực thi liên quan.
- Sở thích cải tiến không có bằng chứng và không nên mở workflow.

### 2.2. Đơn vị thay đổi

Cần định nghĩa một lượt chỉ được sở hữu một vấn đề gốc và một tập tệp có quan hệ trực tiếp. Các loại thay đổi dự kiến:

- Chỉ dẫn gốc hoặc `AGENTS.md`.
- Quy tắc quản trị trong `.agents/rules/`.
- Kỹ năng trong `.agents/skills/`.
- Workflow hoặc giao thức điều phối.
- Script, template hoặc schema hỗ trợ vận hành.

Nếu phát hiện ảnh hưởng nội dung hoặc kiến trúc giáo trình, phải bàn giao sang workflow sở hữu thay vì mở rộng âm thầm.

### 2.3. Bằng chứng và đường cơ sở

Cần chọn tập trường tối thiểu:

- Bối cảnh và phiên bản môi trường.
- Hành vi kỳ vọng và hành vi quan sát được.
- Tệp hoặc bước có thể tái hiện.
- Tần suất, tác động và mức chắc chắn.
- Các nguyên nhân cạnh tranh.
- Chỉ số trước thay đổi và ngưỡng cải thiện mong đợi.

Cần chốt nơi lưu bằng chứng, thời hạn giữ và dữ liệu không được ghi vì riêng tư hoặc an toàn.

### 2.4. Các giai đoạn và cổng

Khung cần cân nhắc, chưa được phép chạy:

```text
Intake
  → reproduce and establish baseline
  → classify root cause and affected owners
  → compare change options and no-change option
  → human approval for controlled trial
  → implement in isolated scope
  → positive, negative, and regression tests
  → independent governance review
  → human decision: adopt, revise, revert, or defer
  → migrate and close
```

Cần mô tả điều kiện vào/ra của từng giai đoạn và đường quay lại khi kiểm thử thất bại.

### 2.5. Vai trò và quyền sở hữu

Cần chốt tối thiểu các trách nhiệm sau mà không mặc định mỗi vai trò là một agent riêng:

- Điều phối và giữ phạm vi.
- Thu và kiểm tra bằng chứng.
- Phân tích nguyên nhân và phương án cạnh tranh.
- Triển khai thay đổi thử nghiệm.
- Kiểm định độc lập.
- Chủ sở hữu kho ra quyết định cuối.

Mỗi work unit sau này phải ghi tệp được đọc, tệp được sửa, đầu vào, đầu ra, kỹ năng bắt buộc, điều kiện đạt và điều kiện dừng.

### 2.6. Thử nghiệm và rollback

Cần xác định:

- Cách cô lập thử nghiệm khỏi nguồn chuẩn đang dùng.
- Cách lưu snapshot hoặc phần chênh lệch trước thay đổi.
- Kiểm thử nào chứng minh lợi ích và kiểm thử nào phát hiện kích hoạt sai.
- Khi nào phải hoàn tác ngay.
- Cách xác nhận hoàn tác không để lại liên kết, metadata hoặc trạng thái mồ côi.

### 2.7. Chấp thuận và kiểm định độc lập

Workflow không được cho người tạo thay đổi tự chấp thuận đầu ra. Cần chốt:

- Thay đổi nào bắt buộc có hồ sơ trong `.agents/decisions/`.
- Bằng chứng nào Người kiểm định phải đọc trực tiếp.
- Cách ghi `Not verified` khi môi trường không cung cấp lượt kiểm định độc lập.
- Ai có quyền chuyển thử nghiệm thành nguồn chuẩn và ngày hiệu lực.

## 3. Các gói thiết kế nhỏ có thể giao sau

Các gói dưới đây chỉ dùng để hoàn thiện thiết kế workflow. Chúng chưa cho phép sửa harness sản xuất.

| Mã | Gói thiết kế | Đầu vào | Đầu ra mong đợi | Không được làm |
|---|---|---|---|---|
| D1 | Kiểm kê bằng chứng và trường dữ liệu | Workflow placeholder, workflow-runs hiện có, rules quản trị | Đề xuất schema bằng chứng và ví dụ ẩn danh | Không tạo log giả hoặc suy ra tần suất chưa đo |
| D2 | Thiết kế trạng thái và cổng | Kết quả D1, trạng thái workflow dùng chung | Sơ đồ trạng thái, điều kiện vào/ra và đường thất bại | Không nâng trạng thái workflow |
| D3 | Thiết kế vai trò và sở hữu | D1–D2, `agent-dispatch-protocol.md` | Ma trận trách nhiệm và mẫu hợp đồng work unit | Không mặc định phải sinh agent cho mọi vai trò |
| D4 | Thiết kế thử nghiệm và rollback | D1–D3, quy tắc an toàn | Ma trận test, tiêu chí dừng và thủ tục rollback | Không chạy thử trên nguồn chuẩn |
| D5 | Thiết kế hồ sơ và di trú | D1–D4, quy tắc quyết định | Cấu trúc hồ sơ, phân tích ảnh hưởng và kế hoạch di trú | Không di trú tệp hiện tại |
| D6 | Rà soát tính sẵn sàng | Toàn bộ D1–D5 và workflow dự thảo | Danh sách thiếu sót, phản biện và khuyến nghị trạng thái | Không tự chấp thuận phần mình soạn |

Chỉ giao một gói khi các đầu vào của nó ổn định. Agent nhận gói phải dừng và trả lại câu hỏi nếu phát hiện quyết định thuộc quyền Chủ sở hữu kho.

## 4. Ứng viên pilot đầu tiên sau khi workflow đạt `Proposed`

Ứng viên hiện tại là metadata, chỉ mục tri thức và context package. Pilot dự kiến chỉ nên áp dụng trên:

- Một `goals/gNN-*/README.md`.
- Một workflow.
- Một hồ sơ quyết định.
- Skill hiện có chỉ được đọc để kiểm tra khả năng kết nối metadata; không đổi schema riêng của skill trong lượt đầu.

Pilot cần so sánh một phiên tác nhân mới trước và sau thay đổi trên cùng bộ câu hỏi truy xuất. Các chỉ số ứng viên gồm tỷ lệ tìm đúng nguồn chuẩn, số lần dùng nhầm nguồn, số tệp phải đọc, thời gian định tuyến, lỗi metadata và khả năng phát hiện thông tin lỗi thời.

Đây mới là giả thuyết pilot. Phạm vi, schema và ngưỡng đạt phải được Chủ sở hữu kho chấp thuận sau khi workflow đạt `Proposed`.

## 5. Ý chính dành cho thiết kế metadata và chỉ mục sau này

- Không bắt toàn bộ tệp di trú cùng lúc.
- Bắt đầu với các nút định tuyến có giá trị cao: goal README, workflows và decisions.
- Metadata chỉ chứa danh tính, loại, trạng thái và quan hệ máy cần đọc; nội dung chuyên môn vẫn nằm trong Markdown.
- Tệp thiếu metadata vẫn được tìm bằng đường dẫn và tiêu đề; metadata sai phải báo lỗi thay vì âm thầm đoán.
- Chỉ mục là đầu ra sinh tự động và phải được đánh dấu không phải nguồn chuẩn.
- Context package là đầu ra theo tác vụ hoặc lượt chạy, không thay thế việc đọc nguồn trực tiếp.
- Không xây RAG hoặc graph database trước khi kiểm thử truy xuất chứng minh tìm kiếm tệp và chỉ mục nhẹ không đủ.

## 6. Ngưỡng cân nhắc RAG hoặc chế độ xem đồ thị

Chỉ đưa thành phương án khi có bằng chứng đo được, ví dụ:

- Tìm kiếm từ khóa và chỉ mục thường xuyên bỏ sót nguồn liên quan vì khác cách diễn đạt.
- Nguồn trải trên nhiều kho hoặc hệ thống và cần lọc quyền, độ mới hoặc metadata phức tạp.
- Gói ngữ cảnh vẫn thiếu nguồn ở tỷ lệ đáng kể sau khi cấu trúc và chỉ mục đã được sửa.
- Câu hỏi quan hệ nhiều bước như ảnh hưởng, thay thế, nguồn gốc hoặc phụ thuộc trở thành nhu cầu vận hành thường xuyên.
- Lợi ích truy xuất dự kiến lớn hơn chi phí lập chỉ mục, đồng bộ, quyền riêng tư và bảo trì.

## 7. Điều kiện đóng ghi chú thiết kế

Ghi chú này hoàn thành vai trò khi:

1. D1–D5 đã có kết luận được Chủ sở hữu kho chấp thuận hoặc ghi rõ chưa giải quyết.
2. Workflow đã chứa đặc tả thực thi đầy đủ và không phụ thuộc vào ghi chú này để chạy.
3. D6 được thực hiện bởi bên kiểm định độc lập và mọi lỗi chặn đã được xử lý.
4. Có hồ sơ quyết định về việc giữ `Placeholder`, chuyển `Proposed` hoặc dừng thiết kế.
5. Nếu chuyển `Proposed`, một kế hoạch pilot riêng được tạo với phạm vi và quyền sửa cụ thể.
