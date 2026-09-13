# Quy trình dạy thử và kiểm chứng

- **Trạng thái:** `Proposed` — chờ duyệt
- **Mục tiêu:** điều phối một đợt dạy thử có kiểm soát cho một bài học hoặc một lộ trình, biến hành vi thực tế của học viên thành bằng chứng, phân tích và quyết định có phạm vi; không suy diễn chất lượng từ cảm nhận, ý kiến giảng viên hoặc việc đã tổ chức buổi dạy.
- **Phạm vi:** kiểm tra điều kiện dạy thử, khóa phiên bản, lập kế hoạch và thu dữ liệu, chuẩn hóa quan sát, phân tích nguyên nhân, đề xuất thay đổi, kiểm định độc lập trạng thái chất lượng và bàn giao sang tầng sở hữu thay đổi.
- **Ngoài phạm vi:** soạn hoặc sửa nội dung bài học, đổi mục tiêu hay quan hệ phụ thuộc, tự tổ chức thay hoạt động của giảng viên, lưu dữ liệu nhận dạng hoặc tự áp dụng giả thuyết thay đổi chưa được chấp thuận.

Dạy thử là hoạt động do con người tổ chức. Quy trình này chuẩn bị, ghi nhận, phân tích và kiểm chứng hoạt động đó; nó không thay giảng viên, học viên hoặc người có thẩm quyền quyết định thay đổi.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Dùng quy trình này khi cần ít nhất một trong các việc sau:

1. Kiểm tra một bài học hoặc lộ trình với học viên thuộc đúng đối tượng mục tiêu.
2. Thu bằng chứng thực tế cho kết quả học tập, độ rõ ràng hoặc tính khả thi về thời lượng.
3. Phân tích một phát hiện, phản hồi hoặc sự cố đã xuất hiện trong buổi dạy thử.
4. Xác định liệu một phiên bản có đủ căn cứ để giữ trạng thái hiện có, giảm trạng thái, cần sửa hay đạt `Validated`.
5. Lập kế hoạch dạy thử lại sau một thay đổi đã được áp dụng bởi quy trình khác.

Một đợt dạy thử chỉ có một đối tượng chính: một bài học hoặc một lộ trình. Dạy thử lộ trình có thể tạo bằng chứng cho các bài học thành phần, nhưng không tự động nâng trạng thái của mọi bài học nếu đường bằng chứng chưa truy được tới từng khẳng định.

### 1.2. Điều kiện bắt đầu

| Điều kiện | Bằng chứng cần có | Xử lý khi thiếu |
|---|---|---|
| Đối tượng dạy thử tối thiểu `Pilot-ready` | `review.md` hiện hành với kiểm định độc lập | Bàn giao về `complete-goal-lessons` hoặc `compose-learning-run`. |
| Lời hứa và đối tượng học viên rõ ràng | Nguồn chuẩn và hợp đồng bài học hoặc lộ trình | Chuyển `Awaiting decision`; không tự suy đoán. |
| Đánh giá năng lực và điểm kiểm tra | `assessment.md` hoặc điểm kiểm tra trong lộ trình | Bàn giao về quy trình sở hữu để thiết kế hoặc làm rõ. |
| Công cụ thu phản hồi | `pilot-feedback-form.md` của bài học, hoặc kế hoạch thu thập lộ trình | Chỉ tạo kế hoạch thu thập; không tổ chức dạy thử. |
| Kế hoạch an toàn và xử lý dữ liệu | `collection-plan.md` được xác nhận trước khi thu hoặc lưu dữ liệu | Có thể lập kế hoạch, nhưng không thu hoặc lưu dữ liệu trước khi hoàn tất. |
| Giảng viên, điều kiện tổ chức và bên có thẩm quyền | Xác nhận của bên tổ chức, Giảng viên và Chủ sở hữu giáo trình | Dừng tại cổng sẵn sàng hoặc `Awaiting decision`; tác nhân AI không thay người tổ chức hay người ra quyết định. |

### 1.3. Định tuyến khi không thuộc phạm vi

| Nguyên nhân gốc | Quy trình chịu trách nhiệm |
|---|---|
| Nội dung, thực hành, đánh giá hoặc hướng dẫn giảng viên của một bài học cần sửa | `complete-goal-lessons` |
| Lịch, nhịp độ, điểm bàn giao hoặc phạm vi của lộ trình cần sửa | `compose-learning-run` |
| Mục tiêu, quan hệ phụ thuộc hoặc cam kết chương trình cần sửa | `change-curriculum-architecture` |
| Công cụ, giao diện lập trình, mô hình, giá hoặc chính sách là nguyên nhân có thể lỗi thời | `refresh-volatile-content` |

Quy trình này tạo giả thuyết và bàn giao. Không dùng một phản hồi đơn lẻ để tự đổi kiến trúc hoặc viết lại bài học.

## 2. Phạm vi của khẳng định kiểm chứng

Trước dạy thử, Điều phối viên phải ghi rõ từng khẳng định được phép kiểm chứng và điều không thể suy ra từ buổi dạy. Khẳng định không được rộng hơn bằng chứng.

```text
Validation scope = target audience + delivery format + content version + tool environment + observed outcome
```

- Một học viên hoặc một phiên 1-1 có thể tạo bằng chứng hữu ích, nhưng phạm vi kết luận phải hẹp và nêu rõ giới hạn mẫu.
- Không đặt số học viên tối thiểu cứng vì chương trình có hình thức 1-1. Người kiểm định độc lập đánh giá độ phủ của bằng chứng, tính phù hợp đối tượng và mức độ tái lập trước khi chấp nhận khẳng định rộng hơn.
- Phản hồi tự báo cáo, mức hài lòng hoặc nhận định của giảng viên chỉ là tín hiệu bổ trợ; không một tín hiệu nào trong số đó đủ để cấp `Validated`.

Kết quả phân tích một khẳng định dùng bốn giá trị `Supported`, `Partially supported`, `Contradicted` hoặc `Inconclusive`. Đây không phải kết quả cổng chất lượng `Pass`, `Fail`, `Not verified`.

## 3. Sơ đồ tổng thể và trạng thái

```text
PILOT REQUEST
  ↓
READINESS AND SCOPE CHECK
  ├── Lesson or run not ready ─────────→ owning workflow
  ├── Missing assessment or instrument ─→ owning workflow
  └── Ready
        ↓
    DEFINE VALIDATION CLAIMS
        ↓
    PLAN EVIDENCE AND DATA HANDLING
        ↓
    LOCK CONTENT VERSION
        ↓
    HUMAN GO/NO-GO GATE
        ├── No-go → CLOSE
        └── Go
              ↓
          CONDUCT PILOT
              ↓
          CHECK EVIDENCE INTEGRITY
              ├── Invalid or insufficient → NEXT-PILOT PLAN → CLOSE
              └── Sufficient
                    ↓
                NORMALIZE AND ANALYZE
                    ↓
                HUMAN CHANGE-DECISION GATE
                    ├── Mandatory accepted change → INDEPENDENT INVALIDATION REVIEW → owning workflow → CLOSE
                    ├── Optional accepted change → owning workflow → CLOSE
                    ├── Need more evidence → NEXT-PILOT PLAN → CLOSE
                    └── No change required
                            ↓
                        INDEPENDENT QUALITY REVIEW
                            ├── Material finding → disposition/adjudication → owner, next-pilot, or owning workflow
                            └── Pass → RECORD STATUS AND HANDOFF → CLOSE
```

```text
Queued → Preflight → Planned → Version locked → Awaiting pilot → Piloted
                                                              ↓
                                                        Evidence checked
                                                              ↓
                                                          Analyzed
                                                              ↓
                                                     Awaiting decision
                                               ┌──────────┼───────────┐
                                             Routed  Re-pilot planned  Reviewed → Closed
                                               ↓
                                            Closed
```

Các trạng thái trên mô tả lượt thực thi, không phải trạng thái chất lượng. Một lượt bị hủy hoặc thiếu dữ liệu không mặc nhiên làm nội dung thành `Needs revision`; nó chỉ không tạo đủ bằng chứng để nâng trạng thái.

## 4. Hồ sơ dạy thử, dữ liệu và quyền sở hữu

### 4.1. Vị trí lưu hồ sơ

Mỗi đợt dạy thử tạo một thư mục dưới `ai-native-builder/pilots/` theo tên không chứa danh tính học viên:

```text
ai-native-builder/pilots/
└── pYYYYMMDD-<target-slug>-<sequence>/
    ├── README.md             # Target, scope, context, and version lock
    ├── collection-plan.md    # Claims, measures, consent notice, and data handling
    ├── evidence-register.md  # Anonymized evidence inventory and access limits
    ├── observations.md       # Expected and observed behavior
    ├── analysis.md           # Findings, explanations, and change hypotheses
    ├── decision.md           # Human decisions and routed handoffs
    └── review.md             # Independent pilot-evidence review; not the current target status
```

`ai-native-builder/pilots/` lưu bằng chứng sư phạm đã ẩn danh. `.agents/workflow-runs/` chỉ lưu sổ điều phối tác nhân; hai nơi không thay thế nhau. `review.md` trong hồ sơ pilot là báo cáo kiểm định bằng chứng của phiên đó. `review.md` hiện hành trong thư mục bài học hoặc lộ trình là nguồn duy nhất ghi trạng thái chất lượng hiện hành; nó phải liên kết tới hồ sơ pilot đã dùng và chỉ Người kiểm định độc lập mới được cập nhật phán quyết này.

### 4.2. Dữ liệu được phép và không được phép

- Dùng mã người tham gia không thể truy ngược trong kho, ví dụ `P01`; không lưu bảng đối chiếu danh tính.
- Không lưu tên, liên hệ, bản đồng ý có chữ ký, ảnh chụp chứa dữ liệu riêng, lịch sử trò chuyện đầy đủ, khóa truy cập, dữ liệu khách hàng hoặc sản phẩm thô có thông tin nhạy cảm.
- Nếu bằng chứng thô cần giữ ở nơi được phép ngoài kho, `evidence-register.md` chỉ ghi loại bằng chứng, người giữ, giới hạn truy cập và cách kiểm định lại; không ghi đường dẫn bí mật hoặc thông tin nhận dạng.
- Chỉ lưu trích đoạn hoặc sản phẩm trung gian đã ẩn danh khi cần cho kiểm định và có căn cứ sử dụng phù hợp.
- `collection-plan.md` mô tả thông báo sử dụng dữ liệu, quyền từ chối và thời hạn lưu; không dùng nó để lưu câu trả lời đồng ý của từng cá nhân.

### 4.3. Khóa phiên bản

`README.md` của hồ sơ phải ghi mục tiêu hoặc lộ trình được dạy, danh sách tệp chuẩn đã dùng, phiên bản hoặc mã kiểm tra nội dung, ngày, hình thức dạy, cấu hình công cụ, thời lượng dự kiến và mọi sai lệch đã biết trước buổi dạy. Nếu nội dung thay đổi sau buổi dạy, hồ sơ cũ vẫn là bằng chứng lịch sử của phiên bản đã khóa, không được gắn ngầm cho phiên bản mới.

### 4.4. Chủ sở hữu tệp

| Tệp | Chủ sở hữu duy nhất | Nội dung được phép |
|---|---|---|
| `README.md` | Điều phối viên | Đối tượng, phạm vi, bối cảnh và khóa phiên bản. |
| `collection-plan.md` | Điều phối viên | Khẳng định, phép đo, cách thu và ranh giới dữ liệu; Giảng viên xác nhận các điều kiện tổ chức liên quan. |
| `evidence-register.md` | Người quản lý bằng chứng | Danh mục dữ liệu ẩn danh, trạng thái truy cập và giới hạn. |
| `observations.md` | Giảng viên hoặc Người quan sát | Dữ kiện, thời lượng và bối cảnh; không kết luận nguyên nhân. |
| `analysis.md` | Người phân tích | Diễn giải có căn cứ, giả thuyết cạnh tranh và phạm vi tác động. |
| `decision.md` | Chủ sở hữu giáo trình | Quyết định chấp nhận, từ chối, hoãn hoặc yêu cầu thêm bằng chứng. |
| `review.md` | Người kiểm định độc lập | Kiểm định bằng chứng pilot, phạm vi và đề xuất trạng thái; không thay thế `review.md` hiện hành của đối tượng. |

## 5. Vai trò và mô hình điều phối tác nhân

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Khóa phạm vi, quản lý trạng thái, tập hợp đầu vào và bàn giao | Tự thay Giảng viên hoặc Chủ sở hữu giáo trình |
| Giảng viên | Tổ chức buổi dạy, hỗ trợ trong giới hạn đã công bố và ghi quan sát | Sửa âm thầm nội dung đang dạy hoặc kết luận chất lượng một mình |
| Người quản lý bằng chứng | Kiểm tra giảm thiểu dữ liệu, ẩn danh hóa và đăng ký bằng chứng | Suy diễn dữ liệu thiếu thành kết luận |
| Người phân tích | Chuẩn hóa quan sát, phân tích nguyên nhân và lập giả thuyết thay đổi | Tự áp dụng thay đổi hoặc chọn thay người dùng |
| Chủ sở hữu giáo trình | Quyết định với từng giả thuyết và đánh đổi | — |
| Người kiểm định độc lập | Kiểm định bằng chứng, trạng thái và tính nhất quán xuyên tầng | Tự nghiệm thu nội dung mình đã tạo hoặc sửa |

Vai trò không mặc nhiên tương ứng một tác nhân AI mới. Khi chạy quy trình, gọi `$workflow-orchestration` và áp dụng [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md) trước mỗi đơn vị công việc.

```text
ROOT ORCHESTRATOR: A, B, C, and J
  ├── Evidence steward: E
  ├── Human facilitator: D
  ├── Analysis agent: F
  ├── Human curriculum owner: G
  └── Independent review agent: H
      └── Evidence adjudicator: only for material disputed findings
```

- D là cổng do con người thực hiện; tác nhân AI không được tự tuyên bố đã dạy thử.
- E và F có thể dùng cùng một tác nhân nếu dữ liệu nhỏ và không yêu cầu độc lập; H luôn là lượt mới, không tham gia tạo hoặc sửa đầu ra được kiểm định.
- Tác nhân chỉ được đọc dữ liệu đã được phép chia sẻ và ẩn danh. Không giao dữ liệu thô không cần thiết để “tăng ngữ cảnh”.
- Nếu có tác nhân con, Điều phối viên phải lưu định danh do công cụ trả về, hợp đồng giao việc, trạng thái và đầu ra trong `.agents/workflow-runs/<run-id>/orchestration-log.md`.

```text
Required isolation: H
Human-only gate: D and G
Preferred continuity: E → F
Parallel-safe units: independent evidence normalization after version lock
Shared-file exclusion: one writer per pilot-record file
Spawn verification: required only when the runtime lacks compatible recorded evidence
```

## 6. Các giai đoạn thực hiện

### Giai đoạn A — Tiếp nhận và kiểm tra điều kiện

**Chủ trì:** Điều phối viên  
**Kỹ năng:** `$curriculum-quality-review`

1. Xác định đối tượng chính là bài học hay lộ trình, phiên bản hiện tại và trạng thái đang được yêu cầu kiểm chứng.
2. Đọc nguồn chuẩn, `review.md` trước dạy thử, phần đánh giá năng lực, phiếu phản hồi phù hợp, lộ trình liên quan và bằng chứng dạy thử cũ nếu có.
3. Kiểm tra các điều kiện ở mục 1.2 và định tuyến đúng phần thiếu.
4. Ghi điều gì buổi dạy có thể và không thể kiểm chứng.

**Điều kiện kết thúc:** đối tượng đủ điều kiện, hoặc đã có bản bàn giao với chủ sở hữu phần thiếu.

### Giai đoạn B — Lập kế hoạch bằng chứng và xử lý dữ liệu

**Chủ trì:** Điều phối viên; Giảng viên xác nhận điều kiện tổ chức  
**Kỹ năng:** `$assessment-design`

Tạo thư mục hồ sơ nháp theo mục 4.1 và ghi `README.md` tối thiểu với đối tượng, phạm vi dự kiến và các bên có thẩm quyền. Sau đó tạo `collection-plan.md` với mỗi khẳng định cần kiểm chứng theo cấu trúc:

```text
Outcome → Learner task → Direct evidence → Criterion → Method → Support allowed → Retry evidence
```

Kế hoạch phải nêu người học mục tiêu, hình thức dạy, thời lượng, số người tham gia dự kiến, điểm quan sát, cách ghi thời gian và mức hỗ trợ, cách dùng phiếu phản hồi, dữ liệu không thu, thông báo sử dụng dữ liệu, quyền từ chối, quyền truy cập và thời hạn lưu. Không dùng bảng tiêu chí chất lượng của giáo trình để chấm trực tiếp học viên.

**Điều kiện kết thúc:** mỗi khẳng định có bằng chứng trực tiếp khả thi và kế hoạch dữ liệu không vượt quyền được phép.

### Giai đoạn C — Khóa phiên bản và cổng sẵn sàng dạy

**Chủ trì:** Điều phối viên  
**Kỹ năng:** `$curriculum-quality-review`

1. Hoàn thiện `README.md` của hồ sơ, ghi phạm vi và khóa phiên bản theo mục 4.3.
2. Xác nhận Giảng viên có tài liệu, thời lượng, phương án phục hồi và giới hạn hỗ trợ cần thiết.
3. Xác nhận Người quản lý bằng chứng biết dữ liệu nào được thu và nơi ghi an toàn.
4. Trình cổng `Go` hoặc `No-go` cho bên tổ chức. `No-go` phải ghi lý do, không coi là bằng chứng chất lượng xấu.

**Điều kiện kết thúc:** có xác nhận `Go` của con người, hoặc hồ sơ đóng với lý do `No-go`.

### Giai đoạn D — Tổ chức buổi dạy thử

**Chủ trì:** Giảng viên  
**Kỹ năng:** Không; đây là hoạt động con người thực hiện

Giảng viên dạy theo phiên bản đã khóa. Chỉ ghi các sai lệch cần thiết: thời lượng thực tế, điểm học viên bị kẹt, mức hỗ trợ, lỗi môi trường, hành vi quan sát được, sản phẩm hoặc kết quả đánh giá, và phản hồi được phép dùng. Quan sát phải tách dữ kiện khỏi diễn giải.

Không thay đổi nội dung đang dạy để “cứu” kết quả mà không ghi lại. Nếu cần can thiệp vì an toàn hoặc để buổi học tiếp tục, ghi can thiệp, lý do và ảnh hưởng tới khả năng diễn giải bằng chứng.

**Điều kiện kết thúc:** buổi dạy hoàn tất, bị hủy hoặc bị mất hiệu lực với lý do và bằng chứng sẵn có.

### Giai đoạn E — Kiểm tra tính toàn vẹn của bằng chứng

**Chủ trì:** Người quản lý bằng chứng  
**Kỹ năng:** `$pilot-feedback-analysis`

1. Lập `evidence-register.md`: loại bằng chứng, mã ẩn danh, nguồn, lớp nội dung, trạng thái truy cập và hạn chế.
2. Kiểm tra dữ liệu nhận dạng, thông tin bí mật hoặc dữ liệu ngoài phạm vi; loại khỏi kho hoặc ẩn danh trước khi phân tích.
3. Đánh dấu bằng chứng thiếu, chọn lọc, không tin cậy hoặc bị ảnh hưởng bởi sai lệch tổ chức.
4. Không suy ra rằng một vấn đề không tồn tại chỉ vì không có quan sát về nó.

**Điều kiện kết thúc:** bộ bằng chứng đủ và được phép phân tích, hoặc có kế hoạch dạy thử lại với lý do dữ liệu không đủ hay không hợp lệ.

### Giai đoạn F — Chuẩn hóa và phân tích

**Chủ trì:** Người phân tích  
**Kỹ năng:** `$pilot-feedback-analysis`, `$assessment-design` khi phát hiện cách đánh giá không đo được năng lực đã hứa

Trong `analysis.md`, chuẩn hóa từng sự kiện quan trọng từ `observations.md` theo cấu trúc:

```text
Expected behavior → Observed behavior → Evidence type → Context → Deviation
```

Trong `analysis.md`:

1. Tách quan sát, trích dẫn, diễn giải và giả thuyết.
2. Lần theo mỗi sai lệch qua điều kiện tiên quyết, hướng dẫn, hoạt động, tương tác AI, sản phẩm, đánh giá năng lực và thời lượng.
3. Nêu ít nhất hai giải thích đáng tin khi quan hệ nhân quả chưa rõ; tìm bằng chứng thuận và nghịch cho từng giải thích.
4. Phân loại phát hiện `Blocker`, `High-impact friction`, `Minor friction`, `Positive evidence` hoặc `Unknown`.
5. Với phát hiện cần xử lý, nêu tầng sở hữu, thay đổi nhỏ nhất, cải thiện hành vi dự kiến, rủi ro hồi quy, độ tin cậy và bằng chứng cần có ở lần dạy tiếp theo.

**Điều kiện kết thúc:** có phân tích truy vết được, bao gồm bằng chứng tích cực, giới hạn và những điều chưa thể kết luận.

### Giai đoạn G — Cổng quyết định thay đổi của con người

**Chủ trì:** Chủ sở hữu giáo trình

Chủ sở hữu ghi trong `decision.md` một trong năm quyết định cho từng giả thuyết. Với `Accept`, phải nêu rõ thay đổi là bắt buộc hay tùy chọn đối với trạng thái chất lượng hiện hành:

1. `Accept` — chấp nhận thay đổi và chỉ rõ quy trình sở hữu.
2. `Reject` — không chấp nhận, cùng lý do và điều kiện xem xét lại.
3. `Defer` — giữ nguyên vì bằng chứng chưa đủ, kèm kế hoạch thu thêm bằng chứng.
4. `Repeat` — dạy thử lại vì lỗi môi trường hoặc điều kiện tổ chức làm mất hiệu lực phiên.
5. `Escalate` — chuyển sang quyết định kiến trúc hoặc quản trị lớn hơn.

Tác nhân AI có thể đề xuất giả thuyết nhưng không được chọn `Accept`, `Reject` hay `Escalate` thay Chủ sở hữu giáo trình.

**Điều kiện kết thúc:** mọi phát hiện `Blocker` hoặc `High-impact friction` có quyết định, chủ sở hữu và bước tiếp theo rõ ràng.

### Giai đoạn H — Kiểm định độc lập và trạng thái chất lượng

**Chủ trì:** Người kiểm định độc lập  
**Kỹ năng:** `$curriculum-quality-review`

Người kiểm định đọc trực tiếp nguồn chuẩn, phiên bản đã khóa, hồ sơ dạy thử và các giới hạn dữ liệu. Giai đoạn này có hai nhánh:

- **H1 — Xác nhận mất hiệu lực:** chạy khi G đã chấp nhận một sửa đổi bắt buộc. Người kiểm định ghi báo cáo H1 trong `review.md` của hồ sơ pilot, xác nhận việc hạ trạng thái xuống `Needs revision` trong `review.md` hiện hành của bài học hoặc lộ trình, liên kết hai tệp và ghi phạm vi cần kiểm định lại. H1 không đề xuất `Validated`.
- **H2 — Kiểm định duy trì hoặc nâng trạng thái:** chỉ chạy khi không có thay đổi đang chờ áp dụng cho phạm vi được kiểm định. Người kiểm định thực hiện các bước sau:

  1. Chấm lại tám cổng bắt buộc `Pass`, `Fail` hoặc `Not verified`.
  2. Chấm tám tiêu chí chất lượng, cho phép `2` ở `Beginner clarity` và `Time feasibility` chỉ khi bằng chứng dạy thử phù hợp hỗ trợ.
  3. Lần theo chuỗi `claim → learner → observed behavior → artifact → assessment → timing → gate → status`.
  4. Ghi phạm vi kiểm chứng, giới hạn mẫu, phiên bản và môi trường trong `review.md` của hồ sơ pilot; cập nhật phán quyết trạng thái và liên kết bằng chứng trong `review.md` hiện hành của bài học hoặc lộ trình.
  5. Đề xuất trạng thái đúng với bằng chứng, không điều chỉnh điểm để đạt trạng thái mong muốn.

Nếu H nêu finding trọng yếu về diễn giải dữ liệu, hard gate, phạm vi bằng chứng hoặc phán quyết trạng thái, áp dụng mục 6.4 của [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). `review.md` của hồ sơ pilot giữ finding; `finding-disposition.md` trong hồ sơ lượt chạy giữ phản hồi và dossier phân xử. Trong workflow này, Người quản lý bằng chứng là phía thứ ba của đánh giá `Out of scope`, nhưng phải độc lập với Người phân tích và Reviewer; nếu không chứng minh được điều đó, không dùng `Out of scope` để đóng finding.

`Validated` chỉ được đề xuất khi phiên bản đã đáp ứng `Release-ready`, có học viên đúng đối tượng, có bằng chứng thực tế về kết quả, độ rõ ràng và thời lượng, không còn cổng chặn, và lượt kiểm định độc lập có bằng chứng thực thi theo `agent-dispatch-protocol.md` nếu dùng tác nhân AI.

**Điều kiện kết thúc:** có báo cáo kiểm định độc lập. Nếu một hard gate là `Not verified`, chỉ ghi sau khi đã cạn đường kiểm tra theo mục 6.4; phải tạo `Awaiting adjudication`, thông báo lại Chủ sở hữu ở G và khóa mọi nâng trạng thái. Khi Chủ sở hữu chưa có mặt, giữ trạng thái hiện hành và chỉ tiếp tục công việc thật sự độc lập. Báo cáo phải ghi phạm vi cần kiểm tra lại và trạng thái trong `review.md` hiện hành phải tuân theo `.agents/rules/quality-gates.md`.

### Giai đoạn I — Bàn giao, mất hiệu lực và kế hoạch dạy thử lại

**Chủ trì:** Điều phối viên

- Nếu G chấp nhận sửa đổi bắt buộc: chỉ bàn giao sau khi H1 đã ghi `Needs revision` vào `review.md` hiện hành của đối tượng. Ghi tệp chịu ảnh hưởng, giả thuyết, bằng chứng nguồn và thước đo cho lần dạy thử lại. Không sửa nội dung trong quy trình này.
- Nếu G chấp nhận sửa đổi tùy chọn: bàn giao sang quy trình sở hữu mà không suy diễn thay đổi trạng thái của phiên bản đã khóa; phiên bản mới phải được kiểm định theo quy trình sở hữu trước khi kế thừa bất kỳ trạng thái nào.
- Nếu phiên bản thay đổi sau dạy thử: giữ hồ sơ cũ làm lịch sử, nhưng ghi rõ bằng chứng nào không còn áp dụng cho phiên bản mới. Lượt dạy thử lại dùng một thư mục hồ sơ mới.
- Nếu bằng chứng chưa đủ hoặc điều kiện tổ chức gây nhiễu: giữ trạng thái hiện có, ghi khẳng định bị ảnh hưởng là `Inconclusive`, nêu giới hạn và tạo kế hoạch thu bằng chứng tiếp theo. Chỉ dùng `Not verified` khi H đã chấm một hard gate và đã thỏa điều kiện “đã cạn đường kiểm tra” của `agent-dispatch-protocol.md`; Chủ sở hữu quyết định thu thêm bằng chứng, thu hẹp phạm vi, trì hoãn hoặc từ chối.
- Nếu H2 đạt: Người kiểm định ghi trạng thái vào `review.md` hiện hành của đúng bài học hoặc lộ trình, kèm liên kết tới `review.md` của hồ sơ pilot; Điều phối viên chỉ xác nhận bàn giao. Không nâng các phạm vi không được bằng chứng bao phủ.

**Điều kiện kết thúc:** quy trình sở hữu tiếp theo, phạm vi kiểm định lại, bằng chứng cũ bị ảnh hưởng và trạng thái hiện hành đều được ghi rõ.

## 7. Kiểm chứng

### 7.1. Kiểm tra xác định trước phân tích

1. Tên thư mục hồ sơ không chứa dữ liệu nhận dạng và có một đối tượng chính.
2. Mọi tệp nguồn trong khóa phiên bản tồn tại và trạng thái trước dạy thử tối thiểu `Pilot-ready`.
3. Với lượt đã đi qua phân tích và quyết định, có `collection-plan.md`, `evidence-register.md`, `observations.md`, `analysis.md`, `decision.md` và `review.md` trước khi đóng. Lượt `No-go` chỉ cần `README.md` và `collection-plan.md`; lượt dừng ở E vì bằng chứng không hợp lệ cần thêm `evidence-register.md` và `observations.md` nếu có dữ liệu đã được phép thu.
4. Dữ liệu trong kho không chứa thông tin cấm; bằng chứng ngoài kho có người giữ và phạm vi truy cập được ghi.
5. Mỗi kết luận trong `analysis.md` trỏ tới một quan sát, sản phẩm, kết quả đánh giá, thời lượng hoặc trích dẫn đã ẩn danh.
6. Mọi quyết định `Accept`, `Reject`, `Defer`, `Repeat` hoặc `Escalate` có chủ sở hữu, lý do và bước tiếp theo.

### 7.2. Kiểm định ngữ nghĩa và giới hạn kết luận

Người kiểm định phải tìm bằng chứng thuận lẫn bằng chứng làm yếu mỗi khẳng định quan trọng. Dùng mô hình dưới đây để không nhầm tín hiệu với kết luận:

```text
Pilot evidence
  → Observation or artifact
  → Competing explanations
  → Change hypothesis or retained assumption
  → Human decision
  → Independent quality review
  → Scoped maturity status
```

- `Fail` nghĩa là bằng chứng đã kiểm tra cho thấy cổng không đạt.
- `Not verified` chỉ dùng cho một hard gate khi cần dữ liệu, quyền truy cập hoặc một đợt dạy thử khác; nó không đồng nghĩa với nội dung kém nhưng vẫn có hệ quả trạng thái theo `.agents/rules/quality-gates.md`. Với một khẳng định kiểm chứng chưa đủ bằng chứng, dùng `Inconclusive`.
- Một sự cố công cụ, một giảng viên can thiệp quá mức hoặc học viên sai đối tượng có thể làm bằng chứng không đủ để kết luận, thay vì tự động bác bỏ bài học.
- Dữ liệu tích cực phải được giữ trong phân tích; quy trình không chỉ thu danh sách lỗi.

### 7.3. Cập nhật trạng thái trung thực

| Tình huống | Trạng thái hoặc bước tiếp theo |
|---|---|
| Cổng bắt buộc thất bại, có tiêu chí `0`, hoặc sửa đổi bắt buộc đã được chấp nhận | `Needs revision` và bàn giao về tầng sở hữu. |
| Không có lỗi chặn nhưng bằng chứng dạy thử chưa đủ phạm vi | Giữ `Pilot-ready` hoặc `Release-ready` hiện có; ghi giới hạn và kế hoạch dạy thử lại. |
| Bằng chứng đủ điều kiện `Pilot-ready` nhưng chưa đạt `Release-ready` | Ghi `Pilot-ready`; không mô tả như sẵn sàng phát hành. |
| Đạt `Release-ready` nhưng chưa có bằng chứng dạy thử đủ | Ghi `Release-ready`; không ghi `Validated`. |
| Đạt điều kiện `Validated` trong H | Ghi `Validated` với phạm vi người học, phiên bản, hình thức và môi trường đã kiểm chứng. |

## 8. Hợp đồng giao việc cho tác nhân AI nhẹ

Mỗi đơn vị công việc chỉ có một vai trò chính, một giai đoạn và danh sách tệp tường minh:

```text
Role: <Orchestrator | Evidence steward | Analyst | Independent reviewer | Evidence adjudicator>
Pilot target: <lesson | learning run>
Current phase: <A | B | C | E | F | H | I>
Allowed files: <explicit file list>
Canonical inputs: <required source files>
Evidence access: <anonymized files and limitations>
Required skills: <skill names or None>
Required outputs: <artifacts and exact locations; finding disposition/adjudication when applicable>
Decision status: <Not required | Awaiting human decision | Recorded>
Stop conditions: <missing consent plan, sensitive data, unlocked version, insufficient evidence, scope expansion>
Do not: <conduct the pilot, identify participants, apply content changes, self-approve status>
```

| Giai đoạn | Vai trò | Kỹ năng |
|---|---|---|
| A | Điều phối viên | `$curriculum-quality-review` |
| B | Điều phối viên; Giảng viên xác nhận điều kiện tổ chức | `$assessment-design` |
| C | Điều phối viên | `$curriculum-quality-review` |
| D | Giảng viên | Không giao cho AI |
| E | Người quản lý bằng chứng | `$pilot-feedback-analysis` |
| F | Người phân tích | `$pilot-feedback-analysis`; `$assessment-design` khi cần |
| G | Chủ sở hữu giáo trình | Không giao cho AI quyết định |
| H | Người kiểm định độc lập | `$curriculum-quality-review`; H1 xác nhận mất hiệu lực, H2 kiểm định duy trì hoặc nâng trạng thái |
| H khi có tranh chấp dữ kiện | Người phân xử bằng chứng độc lập | Đọc dossier theo `agent-dispatch-protocol.md` 6.4–6.5 |
| I | Điều phối viên | Chỉ bàn giao và xác nhận tham chiếu trạng thái |

Tác nhân không tự chuyển giai đoạn. Nó trả về đầu ra, bằng chứng đã đọc, giới hạn, kết quả kiểm tra và lý do dừng cho Điều phối viên.

## 9. Điều kiện đóng quy trình

1. Đối tượng dạy thử, phiên bản, đối tượng học viên, hình thức, môi trường và giới hạn kết luận đã được ghi.
2. Dữ liệu trong kho đã được giảm thiểu và ẩn danh; không có dữ liệu cấm trong hồ sơ hoặc sổ điều phối.
3. Phân tích tách quan sát khỏi diễn giải, có giải thích cạnh tranh khi cần và giữ cả bằng chứng tích cực lẫn tiêu cực.
4. Mọi giả thuyết thay đổi trọng yếu có quyết định của Chủ sở hữu giáo trình hoặc được ghi rõ là chưa thể quyết định.
5. Mọi thay đổi được chấp nhận đã bàn giao đúng quy trình sở hữu; bằng chứng cũ bị ảnh hưởng được xác định mà không xóa lịch sử.
6. Trạng thái chất lượng không vượt quá phạm vi bằng chứng, do Người kiểm định độc lập xác nhận và được ghi trong `review.md` hiện hành của đối tượng; `review.md` của hồ sơ pilot chỉ là bằng chứng liên kết.
7. Nếu có tác nhân con, sổ thực thi đạt điều kiện của `agent-dispatch-protocol.md`, gồm bằng chứng kiểm định độc lập khi H được sử dụng.

Quy trình này không chứng minh tính phổ quát vượt khỏi phạm vi đã ghi. Mỗi khẳng định `Validated` luôn gắn với phiên bản, người học, hình thức dạy và môi trường đã được kiểm chứng.
