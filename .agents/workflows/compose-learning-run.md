# Quy trình ghép lộ trình học

- **Trạng thái:** `Active` — đã được người dùng duyệt
- **Mục tiêu:** ghép các mục tiêu và bộ bài học chuẩn thành lộ trình có thể thực hiện, giữ được quan hệ phụ thuộc, sản phẩm trung gian, nhịp thực hành, thời lượng và trần trưởng thành đã cam kết.
- **Phạm vi:** xác lập hợp đồng lộ trình, chọn mục tiêu, thiết kế chuỗi buổi học và buổi thực hành tích hợp, phân bổ thời lượng, kiểm tra mức sẵn sàng của bài học, tạo tài liệu điều phối trong `ai-native-builder/runs/` và kiểm định độc lập trước dạy thử.
- **Ngoài phạm vi:** thay đổi ranh giới hoặc điều kiện tiên quyết của mục tiêu; viết hoặc sao chép nội dung bài học; dạy thử, phân tích phản hồi thực tế hoặc cấp trạng thái `Validated`.

Quy trình này điều phối các bài học chuẩn, không tạo một phiên bản thứ hai của chúng trong thư mục lộ trình.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Dùng quy trình này khi cần ít nhất một trong các việc sau mà vẫn giữ nguyên định nghĩa mục tiêu và quan hệ phụ thuộc chuẩn:

1. Tạo hoặc điều chỉnh một chương trình thực hành ngắn, lộ trình 1-1 hoặc khóa đầy đủ.
2. Chọn các mục tiêu cần thiết cho một cam kết đầu ra, rồi sắp thành buổi học, buổi thực hành tích hợp và điểm kiểm tra.
3. Kiểm tra một lời hứa có vừa ngân sách thời gian, mức đầu vào và các sản phẩm trung gian cần thiết hay không.
4. Ghép lại lộ trình sau khi bài học hoặc nguồn chuẩn đã thay đổi, nhưng bản thân thay đổi đó đã được quy trình sở hữu xử lý.
5. Xác định bài học còn thiếu, chưa đủ trưởng thành hoặc không thể đưa vào dạy thử.

Không dùng quy trình này chỉ vì các mục tiêu có tên gần nhau hoặc vì muốn nén thêm chủ đề vào cùng một buổi.

### 1.2. Định tuyến khi không thuộc phạm vi

| Nguyên nhân gốc | Quy trình chịu trách nhiệm |
|---|---|
| Cần đổi kết quả, ranh giới, điều kiện tiên quyết hoặc thứ tự phụ thuộc của mục tiêu | `change-curriculum-architecture` |
| Một bài học chuẩn thiếu giải thích, thực hành, sản phẩm trung gian, đánh giá hoặc kiểm định | `complete-goal-lessons` |
| Cần thu thập hoặc diễn giải bằng chứng từ buổi dạy thật | `pilot-and-validate` |
| Cần kiểm tra lại một khẳng định về công cụ, giao diện lập trình, mô hình, giá hoặc chính sách | `refresh-volatile-content` |

Nếu một lời hứa không vừa thời lượng, không được tự bỏ qua thực hành hay kiểm chứng. Điều phối viên phải đưa lựa chọn giảm lời hứa, tăng thời lượng hoặc đổi kiến trúc tới cổng quyết định của con người.

## 2. Hai chế độ thực hiện

| Chế độ | Khi dùng | Đầu ra hợp lệ | Giới hạn |
|---|---|---|---|
| Phác thảo sớm | Có đặc tả mục tiêu đã chốt nhưng một hay nhiều bài học chưa hoàn thiện hoặc chưa đạt `Pilot-ready`. | `README.md`, `schedule.md`, `coverage.md`, `readiness.md` và bản bàn giao; đồ thị bàn giao là một phần của `coverage.md`. | Không tạo `review.md` hoặc `<session>.md`; không được coi là sẵn sàng dạy thử; trạng thái chất lượng giữ `Needs revision`. |
| Đóng gói để dạy | Mọi bài học bắt buộc đã có bộ tài liệu và tối thiểu đạt `Pilot-ready`. | Bộ tệp lộ trình hoàn chỉnh, bao gồm `review.md`, phép kiểm tra và bản bàn giao sang dạy thử; chỉ tạo `<session>.md` khi cần điều phối riêng. | Chỉ được cấp `Pilot-ready` hoặc `Release-ready`; không được cấp `Validated`. |

Chế độ phác thảo sớm là công cụ phát hiện khoảng trống, không phải cách hợp thức hóa việc dạy bằng tài liệu chưa trưởng thành.

## 3. Sơ đồ tổng thể và trạng thái

```text
TRIGGER
  ↓
INTAKE AND MODE SELECTION
  ├── Architecture change required ───→ change-curriculum-architecture
  ├── Lesson package change required ─→ complete-goal-lessons
  └── Run composition
          ↓
      DEFINE PATH CONTRACT
          ↓
      SELECT GOALS BACKWARD FROM PROMISE
          ↓
      BUILD DEPENDENCY AND ARTIFACT GRAPH
          ↓
      COMPOSE SESSIONS AND STUDIOS
          ↓
      CALCULATE TIME AND RECOVERY BUDGET
          ↓
      CHECK LESSON READINESS
          ├── Missing or immature lessons
          │       ↓
          │   EARLY COMPOSITION PACKAGE
          │       ↓
          │   HANDOFF TO LESSON OWNERS → CLOSE
          │
          └── Required lessons ready
                  ↓
              AUTHOR RUN FILES
                  ↓
              OWNER LOCAL CHECKS
                  ↓
              CROSS-FILE DETERMINISTIC CHECKS
                  ↓
              INDEPENDENT REVIEW
                  ├── Fail → Repair → DETERMINISTIC CHECKS → INDEPENDENT REVIEW
                  └── Pass → HANDOFF TO pilot-and-validate → CLOSE
```

```text
Queued → Preflight → Contracted → Mapped → Scheduled → Readiness checked
                                                          ├── Early composition or eligibility unmet → Planning package closed
                                                          └── Delivery eligible → Authored → Deterministically checked → Reviewed
                                                                                  ├── Pass → Closed
                                                                                  └── Fail → Repair → Deterministically checked

Any active state ──→ Awaiting decision ──→ return to the affected state
Any active state ──→ Architecture handoff → change-curriculum-architecture → Close
Any active state ──→ Lesson-package handoff → complete-goal-lessons → Planning package closed
```

`Planning package closed` là kết thúc hợp lệ cho chế độ phác thảo sớm, không phải kết quả đạt chuẩn dạy thử. Trạng thái lượt thực thi khác với trạng thái chất lượng của lộ trình.

## 4. Đầu vào, trách nhiệm chuẩn bị và đầu ra

Điều phối viên bảo đảm từng giai đoạn có đầu vào cần thiết, nhưng không được tự tạo bằng chứng, tự thay đổi cam kết chương trình hoặc tự quyết định đánh đổi thuộc thẩm quyền của con người.

### 4.1. Đầu vào tối thiểu để tiếp nhận

| Đầu vào | Bên cung cấp | Điều phối viên phải làm |
|---|---|---|
| Yêu cầu tạo hoặc sửa lộ trình | Người dùng, chủ sở hữu giáo trình hoặc quy trình bàn giao | Ghi rõ loại lộ trình, đối tượng, lời hứa đầu ra và lý do cần ghép. |
| Ràng buộc giao nhận | Bên yêu cầu hoặc chủ sở hữu giáo trình | Xác nhận hình thức dạy, số buổi, thời lượng, công cụ, giới hạn giữa buổi và yêu cầu an toàn. |
| Bên có thẩm quyền quyết định | Người dùng hoặc chủ sở hữu giáo trình | Xác nhận người chọn khi phải đánh đổi lời hứa, thời lượng hoặc phạm vi. |
| Nguồn chuẩn nền | Kho dự án hiện hành | Đọc kế hoạch chương trình, kiến trúc nội dung, bản đồ chương trình và các bản định hướng mục tiêu liên quan. |

### 4.2. Đầu vào do Điều phối viên tập hợp

Trước khi kết thúc giai đoạn A, Điều phối viên phải tập hợp hoặc ghi lý do không thể tiếp cận:

1. `AI-native-builder-curriculum-plan.md`.
2. `curriculum-content-architecture.md`.
3. `ai-native-builder/curriculum-map.md`.
4. Bản định hướng của các mục tiêu có thể được chọn.
5. Bộ tài liệu bài học, `review.md` và trạng thái chất lượng của các mục tiêu bắt buộc.
6. Các lộ trình hiện có trong `ai-native-builder/runs/` và tài nguyên dùng chung có liên quan.
7. Hồ sơ quyết định, bàn giao hoặc bằng chứng dạy thử ảnh hưởng tới lời hứa của lộ trình, nếu có.

### 4.3. Xử lý đầu vào còn thiếu

- Thiếu đặc tả người học, lời hứa, định dạng hoặc tổng thời lượng: chuyển `Awaiting decision`; không tự suy đoán.
- Chưa biết toàn bộ bài học cần thiết: được tiếp tục để lập bản phác thảo, nhưng phải ghi giả định và không được dạy thử.
- Bài học bắt buộc thiếu hoặc chưa đạt `Pilot-ready`: tạo mục trong `readiness.md`, bàn giao cho `complete-goal-lessons` và dừng ở chế độ phác thảo sớm.
- Ràng buộc chỉ có thể giải quyết bằng đổi mục tiêu, quan hệ phụ thuộc hoặc cam kết: tạo bản bàn giao sang `change-curriculum-architecture`.
- Không truy cập được bằng chứng hoặc tệp: ghi `Not verified`, nguyên nhân, phạm vi kiểm tra lại và bên có thể cung cấp; không suy diễn là `Pass` hoặc `Fail`.

### 4.4. Đầu ra theo chế độ và chủ sở hữu

| Đầu ra | Chế độ | Bên tạo hoặc cập nhật | Bên nghiệm thu |
|---|---|---|
| Hợp đồng lộ trình trong `README.md` | Cả hai | Người thiết kế lộ trình | Người kiểm định độc lập ở chế độ đóng gói để dạy |
| Lịch và ngân sách thời lượng trong `schedule.md` | Cả hai | Người thiết kế lộ trình | Người kiểm định độc lập ở chế độ đóng gói để dạy |
| Ma trận bao phủ, bao gồm đồ thị bàn giao, trong `coverage.md` | Cả hai | Người thiết kế lộ trình | Người kiểm định độc lập ở chế độ đóng gói để dạy |
| Mức sẵn sàng, khoảng trống và bàn giao trong `readiness.md` | Cả hai | Người kiểm tra mức sẵn sàng | Người kiểm định độc lập ở chế độ đóng gói để dạy |
| Tệp điều phối riêng của buổi cần thiết | Chỉ đóng gói để dạy | Người soạn lộ trình | Người kiểm định độc lập |
| Kết quả kiểm định trong `review.md` | Chỉ đóng gói để dạy | Người kiểm định độc lập | Theo các cổng chất lượng hiện hành |
| Bản bàn giao tới quy trình tiếp theo | Cả hai | Điều phối viên | Bên tiếp nhận xác nhận đủ điều kiện |

## 5. Vai trò và mô hình điều phối tác nhân

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Tiếp nhận, khóa phạm vi, quản lý trạng thái, quyết định phân công và bàn giao | Tự đổi lời hứa hoặc thay con người ở cổng quyết định |
| Người thiết kế lộ trình | Xác lập hợp đồng, chọn mục tiêu, thiết kế đồ thị và lịch | Đổi định nghĩa mục tiêu hoặc sao chép nội dung bài học |
| Người kiểm tra mức sẵn sàng | Đối chiếu bài học bắt buộc, trạng thái chất lượng và khoảng trống | Nâng trạng thái bài học bằng suy đoán |
| Người soạn lộ trình | Tạo các tệp điều phối từ phương án đã khóa | Viết lại nội dung chuẩn của bài học |
| Người kiểm định độc lập | Kiểm tra cấu trúc, ý nghĩa, thời lượng và khả năng bàn giao | Tự nghiệm thu phần mình vừa tạo hoặc sửa |
| Chủ sở hữu giáo trình | Chọn giữa các đánh đổi vượt quyền Điều phối viên | — |

`Chủ sở hữu giáo trình` là vai trò con người tại cổng quyết định, không phải vai trò tác nhân AI; vì vậy không xuất hiện trong enum `Role` ở mục 9 và không được sinh như tác nhân con.

Vai trò không mặc nhiên tương ứng một tác nhân AI mới. Khi chạy quy trình, gọi `$workflow-orchestration` và áp dụng [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md) trước mỗi đơn vị công việc.

```text
ROOT ORCHESTRATOR: A, deterministic integration, and I
  ├── Path design agent: B → C → D → E
  ├── Readiness agent: F
  ├── Run author: G
  └── Independent review agent: H
```

- Nên giữ cùng một tác nhân cho B đến E vì các giai đoạn dùng chung mô hình lời hứa, đồ thị và tải thời gian.
- F có thể là một tác nhân chuyên biệt hoặc một đơn vị đọc độc lập khi danh sách bài học lớn; không được sửa các tệp bài học.
- H bắt buộc là một lượt tác nhân mới không tham gia thiết kế, soạn hoặc sửa đầu ra được kiểm định.
- Chỉ tách tác nhân khi công việc đủ khép kín, có tiêu chí đạt và không tranh chấp ghi tệp. Một tệp lộ trình chỉ có một người ghi tại một thời điểm.
- Việc sinh tác nhân chỉ được công nhận khi có định danh do công cụ trả về, quan hệ cha-con, hợp đồng giao việc, trạng thái kết thúc và đầu ra được kiểm tra trong `.agents/workflow-runs/<run-id>/orchestration-log.md`.

```text
Required isolation: H
Preferred continuity: B → C → D → E
Conditional specialist: F
Parallel-safe units: read-only readiness checks after goal selection is stable
Shared-file exclusion: one writer per run file
Spawn verification: required only when the runtime lacks compatible recorded evidence
```

## 6. Các giai đoạn thực hiện

### Giai đoạn A — Tiếp nhận, phân loại và chọn chế độ

**Chủ trì:** Điều phối viên  
**Kỹ năng:** `$learning-path-composition`

1. Ghi người học, lời hứa đầu ra, hình thức, giới hạn thời lượng và lý do cần lộ trình.
2. Áp dụng phép thử kích hoạt và bảng định tuyến.
3. Chọn `Delivery packaging` chỉ khi đối chiếu sơ bộ cho thấy mọi bài học bắt buộc có `review.md` hiện hành với trạng thái tối thiểu `Pilot-ready`. Nếu thiếu tệp, thiếu quyền truy cập hoặc có bất kỳ bài nào chưa đạt, chọn `Early composition`.
4. Định vị các nguồn chuẩn, lộ trình hiện có và tệp có thể bị ảnh hưởng.
5. Nếu yêu cầu đòi đổi mục tiêu hoặc phụ thuộc, tạo bản bàn giao rồi kết thúc lượt này.

**Điều kiện kết thúc:** có chế độ, phạm vi và nguồn đầu vào rõ ràng; hoặc đã định tuyến đúng.

### Giai đoạn B — Xác lập hợp đồng lộ trình

**Chủ trì:** Người thiết kế lộ trình  
**Kỹ năng:** `$learning-path-composition`

Ghi trong `README.md` xuất phát điểm của học viên; lời hứa đầu ra quan sát được; trần trưởng thành; phần loại trừ; hình thức, số buổi, thời lượng và phần việc giữa buổi; công cụ, ràng buộc an toàn; cùng tiêu chí để chuyển sang buổi sau.

Phải đưa tới Chủ sở hữu giáo trình quyết định khi lời hứa không vừa thời lượng, phải bỏ một mục tiêu cần thiết, phải tăng phần việc bắt buộc giữa buổi, phải gộp các vòng thực hành không thể hoàn thành cùng lúc hoặc chưa rõ loại lộ trình cần tạo.

**Điều kiện kết thúc:** lời hứa, giới hạn và trần trưởng thành đã được xác nhận, hoặc lượt ở `Awaiting decision`.

### Giai đoạn C — Chọn mục tiêu ngược từ lời hứa

**Chủ trì:** Người thiết kế lộ trình  
**Kỹ năng:** `$learning-path-composition`

1. Bắt đầu ở năng lực cuối, lần ngược các điều kiện tiên quyết.
2. Phân loại mục tiêu thành bắt buộc, tùy chọn hoặc không thuộc phạm vi.
3. Ghi trong phần `Mục tiêu được chọn và lý do` của `coverage.md` mỗi mục tiêu được chọn cùng lý do, đầu vào và nơi tiêu thụ đầu ra. C là người ghi duy nhất phần này; D chỉ đọc phần đã khóa rồi bổ sung đồ thị, điểm kiểm tra và phục hồi. Nếu C và D do hai tác nhân khác thực hiện, chúng chạy tuần tự và D phải đọc trực tiếp `coverage.md`, không nhận bàn giao bằng trí nhớ hội thoại.
4. Nếu một mục tiêu bắt buộc không vừa giới hạn, quay về cổng quyết định thay vì nén thực hành hoặc kiểm chứng.

**Điều kiện kết thúc:** danh sách mục tiêu có lý do và giữ được mọi điều kiện tiên quyết cần thiết.

### Giai đoạn D — Lập đồ thị phụ thuộc và bàn giao sản phẩm trung gian

**Chủ trì:** Người thiết kế lộ trình  
**Kỹ năng:** `$learning-path-composition`; chỉ dùng `$learner-artifact-design` khi buổi thực hành tích hợp cần một sản phẩm **riêng của lộ trình** để kết nối các đầu ra đã khóa

Mỗi cạnh phải mô tả năng lực hoặc sản phẩm trung gian được truyền đi:

```text
gNN [session outcome]
  └── capability/artifact ──→ gMM [downstream use]
```

Trong `coverage.md`, nối từng mục tiêu với buổi học, sản phẩm đầu vào, sản phẩm đầu ra, điểm kiểm tra, cách phục hồi và buổi hoặc mục tiêu tiếp theo. Phát hiện mục tiêu mồ côi, buổi không có đầu ra, điểm kiểm tra không có bằng chứng và sản phẩm không có nơi sử dụng.

Không dùng `$learner-artifact-design` để đổi schema, bằng chứng, ý nghĩa hoặc điều kiện bàn giao của sản phẩm trung gian thuộc một `gNN`. Nếu cần thay đổi tài liệu triển khai của sản phẩm đó, bàn giao sang `complete-goal-lessons`; nếu cần đổi kết quả, phạm vi hoặc quan hệ phụ thuộc, bàn giao sang `change-curriculum-architecture`.

**Điều kiện kết thúc:** tất cả mục tiêu được chọn có vị trí, sản phẩm trung gian và đường bàn giao rõ ràng.

### Giai đoạn E — Ghép buổi học, buổi thực hành tích hợp và ngân sách thời lượng

**Chủ trì:** Người thiết kế lộ trình  
**Kỹ năng:** `$learning-path-composition`; `$assessment-design` khi thiết kế hoặc sửa cách đánh giá của một điểm kiểm tra cấp lộ trình

Mỗi buổi phải có một năng lực chính, liên kết mục tiêu chuẩn, trạng thái đầu vào, dòng hoạt động, sản phẩm, điểm kiểm tra, cách phục hồi và phần việc giữa buổi có ước tính thời lượng. Với mỗi điểm kiểm tra, ghi tối thiểu: hành vi được phép khẳng định, việc học viên phải làm, bằng chứng trực tiếp, tiêu chí đạt, phương pháp quan sát hoặc xem xét, hỗ trợ được phép và bằng chứng cần nộp lại khi thử lại. Khi điểm kiểm tra thiếu ánh xạ `outcome → task → evidence → criterion → method → feedback → retry`, E gọi `$assessment-design`; không dùng skill này để kiểm định chất lượng lộ trình. Trong văn xuôi, “buổi thực hành tích hợp” là cách gọi tiếng Việt của `studio`; chỉ giữ `studio` trong tên tệp, nhãn định danh hoặc khối kỹ thuật. Buổi thực hành tích hợp dùng để kết nối, phản biện và chuyển giao giữa các mục tiêu; không dùng để đưa vào năng lực mới chưa được khai báo.

Trong `schedule.md`, tính riêng thời lượng cho định hướng, thiết lập, thực hành, kiểm tra, phản hồi, chuyển tiếp, lỗi AI hoặc công cụ, câu hỏi, rà soát sản phẩm và khoảng phục hồi. Phần việc giữa buổi phải được ghi riêng, không ngầm cộng vào thời lượng buổi học.

```text
Workshop: 3 × 180 minutes = 540 minutes
Full path: 16 × 90 + 4 × 120 = 1,920 minutes = 32 hours
```

Với cấu trúc hiện hành, chương trình thực hành ba buổi chỉ nhắm tới nguyên mẫu được kiểm chứng nội bộ và các mục tiêu `g01` đến `g06`; không hứa hẹn phát hành công khai hay bài tốt nghiệp. Lộ trình đầy đủ bao phủ `g01` đến `g11` và có bốn buổi thực hành tích hợp. Mọi thay đổi các ranh giới này phải được chuyển sang `change-curriculum-architecture`.

**Điều kiện kết thúc:** tổng thời lượng khớp hợp đồng, không có phụ thuộc ngược và mọi điểm kiểm tra có thời gian lẫn bằng chứng.

### Giai đoạn F — Kiểm tra mức sẵn sàng bài học

**Chủ trì:** Người kiểm tra mức sẵn sàng  
**Kỹ năng:** Không; đây là đối chiếu chỉ đọc theo `review.md`, bộ tệp bài học và `.agents/rules/quality-gates.md`

1. Đối chiếu từng mục tiêu bắt buộc với bộ tệp bài học, trạng thái chất lượng, sản phẩm trung gian, tài nguyên và kết quả kiểm định.
2. Ghi trong `readiness.md` mỗi kết quả `Pass`, `Fail` hoặc `Not verified`, cùng bằng chứng, người sở hữu và bước bàn giao.
3. Nếu thiếu nội dung hoặc bài học chưa đủ trưởng thành, tạo gói phác thảo sớm, bàn giao rõ ràng về `complete-goal-lessons` rồi đóng lượt mà không nâng trạng thái chất lượng.
4. Nếu A đã chọn `Delivery packaging` nhưng F phát hiện điều kiện trên không đúng, ghi lý do hạ cấp, chuyển chế độ thành `Early composition`, tạo bản bàn giao sang `complete-goal-lessons` và đóng ở `Planning package closed`. Không chạy G hoặc H để cố hợp thức hóa chế độ đã chọn sai.
5. Chỉ cho phép sang G trong chế độ đóng gói để dạy khi tất cả bài học bắt buộc tối thiểu `Pilot-ready` và không còn cổng chặn đối với lộ trình.

**Điều kiện kết thúc:** hoặc có danh sách khoảng trống đã được bàn giao, hoặc tất cả bài học bắt buộc đủ điều kiện đóng gói.

### Giai đoạn G — Soạn bộ tệp điều phối lộ trình

**Chủ trì:** Người soạn lộ trình  
**Kỹ năng:** `$learning-path-composition`

Tạo hoặc cập nhật đúng các tệp được phép trong `ai-native-builder/runs/<run-slug>/`. Chỉ viết sự điều phối đặc thù của lộ trình và trỏ tới bài học, mẫu dùng chung hoặc tài nguyên chuẩn khi cần dùng lại nội dung. Không sao chép lời giải thích, bài thực hành, chính sách, mẫu hay bảng tiêu chí từ thư mục mục tiêu.

**Điều kiện kết thúc:** bộ tệp có nguồn sở hữu rõ ràng, không lặp nội dung chuẩn và phản ánh chính xác phương án đã khóa.

### Cổng kiểm tra xác định trước kiểm định độc lập

Trước H, các phép kiểm tra xác định được thực hiện theo đúng quyền sở hữu sau:

- Người thiết kế lộ trình chạy cổng cục bộ cho `README.md`, `schedule.md` và `coverage.md`.
- Người kiểm tra mức sẵn sàng chạy cổng cục bộ cho `readiness.md`.
- Người soạn lộ trình chạy cổng cục bộ cho từng `<session>.md` nếu tệp đó tồn tại.
- Điều phối viên chạy kiểm tra tích hợp xuyên tệp sau G: liên kết, quan hệ phụ thuộc, tổng thời lượng, trùng nguồn chuẩn, độ đầy đủ của điểm kiểm tra và ranh giới quyền sở hữu.

Mỗi bên phải ghi vị trí lỗi hoặc kết quả kiểm tra vào hồ sơ điều phối trước khi chuyển H. Người kiểm định độc lập chỉ kiểm tra hồ sơ này có đủ, có thể tái lập và phù hợp với tệp đã đọc; không chịu trách nhiệm bắt lỗi cơ học lần đầu.

### Giai đoạn H — Kiểm tra, kiểm định độc lập và sửa

**Chủ trì:** Người kiểm định độc lập  
**Kỹ năng:** `$curriculum-quality-review`

1. Xác nhận các phép kiểm tra xác định ở mục 8 đã được đúng chủ sở hữu chạy trước H, có vị trí lỗi/kết quả và vẫn áp dụng cho phiên bản tệp hiện tại.
2. Kiểm định trực tiếp nguồn chuẩn, bộ tệp lộ trình và bằng chứng; không nhận kết luận tự đánh giá làm bằng chứng đủ.
3. Ghi cổng, điểm số, bằng chứng, giới hạn truy cập và kết luận vào `review.md`.
4. Nếu thất bại, trả đúng phát hiện về đơn vị sở hữu. Điểm kiểm tra thiếu ánh xạ đánh giá cấp lộ trình trả về E để gọi `$assessment-design`; nếu chỉ thiếu chỉ dẫn điều phối cho một điểm kiểm tra đã có tiêu chí, trả về G; nếu thiếu đánh giá của chính một `gNN`, trả về `complete-goal-lessons`. Người kiểm định không dùng `$assessment-design` để tự sửa. Một chu kỳ sửa chỉ được đổi các tệp và vấn đề đã nêu; thay đổi lời hứa hoặc kiến trúc phải quay lại quy trình sở hữu.
5. Sau hai chu kỳ sửa vẫn kẹt cùng một vấn đề, chuyển `Awaiting decision` cùng phương án và bằng chứng; không tự hạ chuẩn để đóng lượt.

**Điều kiện kết thúc:** kiểm định độc lập `Pass`, hoặc có bản ghi chặn rõ ràng.

### Giai đoạn I — Ghi trạng thái và bàn giao

**Chủ trì:** Điều phối viên

- Chế độ phác thảo sớm: ghi `Needs revision`, các khoảng trống, giả định và điều kiện tái nhập; bàn giao sang chủ sở hữu bài học.
- Chế độ đóng gói để dạy: chỉ ghi `Pilot-ready` khi toàn bộ cổng bắt buộc đạt `Pass`, không có tiêu chí bằng `0`, tổng điểm đạt tối thiểu `11/16` và có kiểm định độc lập. Ghi `Release-ready` khi thêm điều kiện `13/16` và không còn sửa bắt buộc đã biết.
- Bàn giao sang `pilot-and-validate` kèm phiên bản nguồn, lộ trình, kết quả kiểm định, giới hạn, giả định, câu hỏi chưa giải quyết, mọi `Not verified` còn lại cùng nguyên nhân/bên cung cấp/phạm vi kiểm tra lại, bằng chứng bị mất hiệu lực nếu thay đổi và điều kiện bắt đầu dạy thử.

**Điều kiện kết thúc:** trạng thái không vượt quá bằng chứng hiện có và bên tiếp nhận có đủ tệp để bắt đầu.

## 7. Cấu trúc tệp lộ trình và quyền sở hữu

```text
runs/<run-slug>/
├── README.md        # Path contract, audience, promise, and exclusions
├── schedule.md      # Session order, timing, goal links, and handoffs
├── coverage.md      # Goal selection, handoff graph, checkpoints, and recovery
├── readiness.md     # Lesson maturity, blockers, and required handoffs
├── review.md        # Delivery-packaging mode only: independent quality review
└── <session>.md     # Delivery-packaging mode only when separate facilitation is needed
```

`run-slug` là định danh bền vững của lộ trình và thư mục chuẩn trong `ai-native-builder/runs/`. `run-id` là định danh của một lượt thực thi workflow và chỉ tồn tại trong `.agents/workflow-runs/`. Một lộ trình có thể có nhiều `run-id`; không dùng hai định danh thay thế cho nhau.

| Tệp | Chủ sở hữu duy nhất | Nội dung được phép |
|---|---|---|
| `README.md` | Người thiết kế lộ trình | Hợp đồng, đối tượng, lời hứa, giả định và phần loại trừ. |
| `schedule.md` | Người thiết kế lộ trình | Nguồn duy nhất về thứ tự và thời lượng các buổi. |
| `coverage.md` | Người thiết kế lộ trình | Nguồn duy nhất về lựa chọn mục tiêu, đường truy vết, đồ thị bàn giao, sản phẩm, điểm kiểm tra và phục hồi. |
| `readiness.md` | Người kiểm tra mức sẵn sàng | Trạng thái bài học, khoảng trống và bàn giao cần thiết. |
| `<session>.md` | Người soạn lộ trình | Chỉ ở chế độ đóng gói để dạy khi một buổi phức tạp cần điều phối riêng; không chứa bài học chuẩn sao chép. |
| `review.md` | Người kiểm định độc lập | Chỉ ở chế độ đóng gói để dạy: kết quả kiểm định; Người soạn không được điền sẵn. |

Chỉ tạo `<session>.md` khi `schedule.md` không đủ để điều phối an toàn một buổi vì có ít nhất một trong các yếu tố: nhiều điểm kiểm tra cần can thiệp khác nhau; ghép hoặc đối chiếu nhiều sản phẩm trung gian; thiết lập, phục hồi hoặc phương án dự phòng riêng; hoặc điều phối nhiều người, công cụ hay ranh giới an toàn cần hướng dẫn chi tiết. Không tạo tệp chỉ để lặp lại lịch hoặc kéo dài diễn giải. Không để hai tệp cùng sở hữu lịch, ma trận bao phủ hoặc trạng thái mức sẵn sàng.

## 8. Kiểm chứng

### 8.1. Phép kiểm tra xác định

Đây là danh sách cổng cục bộ và kiểm tra tích hợp được phân công ở phần ngay trước H. Không chuyển trách nhiệm chạy lần đầu sang Người kiểm định độc lập:

1. Mọi liên kết tới mục tiêu, bài học, tài nguyên dùng chung và tệp lộ trình đều tồn tại.
2. Thứ tự trong lịch giữ mọi điều kiện tiên quyết; không có mục tiêu, buổi, sản phẩm hoặc điểm kiểm tra mồ côi.
3. Tổng thời lượng bằng hợp đồng sau khi cộng chuyển tiếp và khoảng phục hồi; phần việc giữa buổi được tách riêng.
4. Không có nội dung bài học chuẩn bị sao chép sang `runs/`.
5. Mỗi điểm kiểm tra có sản phẩm hoặc hành vi quan sát được, tiêu chí quyết định, phương pháp xem xét, hỗ trợ được phép và cách phục hồi. Không dùng mức tự tin tự báo cáo làm bằng chứng chính.
6. Không có hai tệp cùng công bố một nguồn chuẩn cho thứ tự, thời lượng, ma trận bao phủ hoặc mức sẵn sàng.

Kết quả kiểm tra phải ghi được vị trí lỗi, không chỉ ghi “đã kiểm tra”. Nếu chưa có công cụ tự động cho một phép kiểm tra, ghi rõ đó là kiểm tra thủ công, phạm vi đã đọc và giới hạn còn lại.

### 8.2. Kiểm định ngữ nghĩa độc lập

Dùng `$curriculum-quality-review` để đánh giá đủ tám cổng bắt buộc trong `.agents/rules/quality-gates.md`: `Alignment`, `Observable outcome`, `Prerequisite`, `Learner ownership`, `Evidence`, `Verification`, `Safety` và `Consistency`. Sau đó chấm riêng đủ tám tiêu chí chất lượng 0–2, trong đó có `Time feasibility` và `Progression`; không chấm hai tiêu chí này bằng `Pass`/`Fail`/`Not verified`.

```text
Program promise
  → Required goal
  → Session outcome
  → Incoming artifact
  → Learning activity
  → Produced artifact
  → Checkpoint evidence
  → Recovery path
  → Next session
```

Người kiểm định lần theo từng đường của sơ đồ. Thiếu nội dung là `Fail`; thiếu quyền truy cập hoặc bằng chứng quan sát trong dạy thử là `Not verified`, kèm phạm vi kiểm tra lại và bên sở hữu.

### 8.3. Điều kiện chất lượng trước dạy thử

- Một lộ trình ở chế độ phác thảo sớm luôn giữ `Needs revision`.
- Lộ trình có thể đạt `Pilot-ready` hoặc `Release-ready` trước dạy thử theo các ngưỡng của quy tắc chất lượng, nhưng không được ghi `Validated`.
- Trước dạy thử, tổng điểm tối đa là `14/16` vì `Beginner clarity` và `Time feasibility` đều bị trần `1`. Vì vậy `Pilot-ready` là đích thực dụng; `Release-ready` từ `13/16` chỉ là trường hợp hẹp, không là bằng chứng rằng lộ trình đã được dạy thử hoặc phát hành.
- Mức tự tin của học viên sau buổi học, nếu được thu thập khi dạy thử, chỉ là bằng chứng bổ trợ. Kết quả thực hiện, sản phẩm, thời lượng thực tế và quan sát ở điểm kiểm tra mới là bằng chứng chính để kiểm chứng lộ trình.

## 9. Hợp đồng giao việc cho tác nhân AI nhẹ

Mỗi đơn vị công việc chỉ có một vai trò chính, một giai đoạn và danh sách tệp tường minh:

```text
Role: <Orchestrator | Path designer | Readiness reviewer | Run author | Independent reviewer>
Mode: <Early composition | Delivery packaging>
Current phase: <A | B | C | D | E | F | G | H | I>
Allowed files: <explicit file list>
Canonical inputs: <required source files>
Required skills: <skill names or None>
Required outputs: <artifacts and exact locations>
Decision status: <Not required | Awaiting decision | Confirmed>
Stop conditions: <missing input, scope expansion, time conflict, failed gate>
Do not: <change goal boundaries, duplicate lesson content, self-approve, exceed maturity ceiling>
```

| Giai đoạn | Vai trò | Kỹ năng |
|---|---|---|
| A | Điều phối viên | `$learning-path-composition` |
| B–D | Người thiết kế lộ trình | `$learning-path-composition`; `$learner-artifact-design` khi cần ở D |
| E | Người thiết kế lộ trình | `$learning-path-composition`; `$assessment-design` khi thiết kế hoặc sửa đánh giá điểm kiểm tra cấp lộ trình |
| F | Người kiểm tra mức sẵn sàng | Không; đối chiếu chỉ đọc theo `review.md` và quy tắc chất lượng |
| G | Người soạn lộ trình | `$learning-path-composition` |
| H | Người kiểm định độc lập | `$curriculum-quality-review` |
| I | Điều phối viên | Không; chỉ ghi trạng thái và bàn giao |

Tác nhân không tự chuyển giai đoạn. Nó trả về đầu ra, phép kiểm tra, điểm chưa xác minh và lý do dừng để Điều phối viên quyết định bước tiếp theo.

## 10. Điều kiện đóng quy trình

### 10.1. Đóng chế độ phác thảo sớm

1. Có hợp đồng, lịch dự kiến, ma trận bao phủ gồm đồ thị bàn giao và ngân sách thời lượng.
2. Mọi khoảng trống bài học hoặc rủi ro đã được ghi trong `readiness.md` cùng chủ sở hữu.
3. Đã bàn giao đúng quy trình chịu trách nhiệm; không tuyên bố sẵn sàng dạy thử.
4. Trạng thái chất lượng là `Needs revision`.
5. Không tạo `review.md` hoặc `<session>.md`; hai tệp này chỉ thuộc chế độ đóng gói để dạy.

### 10.2. Đóng chế độ đóng gói để dạy

1. Mọi bài học bắt buộc có trạng thái tối thiểu `Pilot-ready`.
2. Bộ tệp điều phối có chủ sở hữu rõ ràng, không trùng nội dung chuẩn và không có tham chiếu hỏng.
3. Quan hệ phụ thuộc, đường sản phẩm trung gian, điểm kiểm tra, phục hồi và ngân sách thời lượng đều đạt kiểm tra.
4. Kiểm định độc lập ghi `Pass` cho phạm vi lộ trình.
5. Trạng thái là `Pilot-ready` hoặc `Release-ready` đúng với bằng chứng; không có trạng thái `Validated` trước dạy thử.
6. Bản bàn giao sang `pilot-and-validate` đầy đủ và, nếu có phân công tác nhân con, sổ thực thi đạt điều kiện của `agent-dispatch-protocol.md`.

### 10.3. Điều kiện chuyển quy trình sang `Active`

Trước khi đổi trạng thái quy trình này từ `Proposed` sang `Active`, Điều phối viên phải kiểm kê mọi thư mục hiện có trong `ai-native-builder/runs/`. Mỗi lộ trình hiện có phải được đưa qua quy trình này, hoặc được đánh dấu rõ là lộ trình cũ chưa kiểm định theo chuẩn mới cùng điều kiện và bên chịu trách nhiệm kiểm định lại. Không suy diễn rằng các tệp cũ đạt `Pilot-ready` chỉ vì chúng đã tồn tại.

Quy trình này chứng minh lộ trình được ghép nhất quán và có thể đưa đi dạy thử. Nó không chứng minh học viên thực sự đạt kết quả cho tới khi quy trình dạy thử và kiểm chứng hoàn tất.
