# Quy trình làm mới nội dung dễ lỗi thời

- **Trạng thái:** `Proposed` — chờ duyệt
- **Mục tiêu:** kiểm tra lại các khẳng định phụ thuộc công cụ, phiên bản, giá, quyền hạn, chính sách hoặc nguồn bên ngoài; cập nhật bằng chứng gần nội dung sử dụng và định tuyến đúng mọi thay đổi có ảnh hưởng tới giáo trình.
- **Phạm vi:** phát hiện khẳng định đến hạn, tạo hàng đợi dẫn xuất, nghiên cứu có giới hạn, cập nhật sổ khẳng định và sổ bằng chứng, phân tích ảnh hưởng, chặn rủi ro an toàn khi cần, kiểm định độc lập và bàn giao.
- **Ngoài phạm vi:** khảo sát công cụ không phục vụ quyết định, tự thay công cụ vì mới hơn, tự sửa nội dung bài học hoặc lộ trình phụ thuộc, tự thay đổi mục tiêu và tự quyết định đánh đổi sản phẩm.

Quy trình này làm mới bằng chứng và trạng thái của khẳng định. Nó không tạo một nguồn chuẩn trung tâm thứ hai, không sao chép tài liệu bên ngoài và không biến “mới hơn” thành “phù hợp hơn”.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Dùng quy trình này khi ít nhất một điều kiện sau đúng:

1. Đã đến ngày kiểm tra tiếp theo của một khẳng định.
2. Phiên bản công cụ, mô hình, giao diện lập trình, thư viện, chính sách hoặc tài liệu nguồn không còn khớp phạm vi đã ghi.
3. Có thông báo thay đổi, ngừng hỗ trợ, sự cố an toàn, thay đổi giá/quyền hạn hoặc phản ánh từ dạy thử.
4. Chuẩn bị phát hành, dạy thử hoặc sử dụng hướng dẫn phụ thuộc mạnh vào công cụ thay đổi nhanh.
5. Người dùng hoặc người kiểm định tranh chấp một khẳng định có thể kiểm chứng.

Không dùng quy trình này để tìm “công cụ tốt nhất”, thay đổi sở thích công nghệ, hoặc nghiên cứu lại nguyên lý sư phạm ổn định khi không có bằng chứng mới ảnh hưởng quyết định.

### 1.2. Các loại điều kiện kiểm tra lại

Mỗi khẳng định dễ lỗi thời phải có ít nhất một điều kiện kiểm tra lại, chọn từ:

| Loại điều kiện | Khi kích hoạt |
|---|---|
| Theo ngày | Đến `Ngày kiểm tra tiếp theo`. |
| Theo phiên bản | Phiên bản nguồn hoặc công cụ khác `Phiên bản/phạm vi` đã ghi. |
| Theo sự kiện | Có thông báo thay đổi, ngừng hỗ trợ, cảnh báo an toàn hoặc thay đổi chính sách. |
| Trước khi sử dụng | Trước phát hành, dạy thử hoặc buổi học phụ thuộc trực tiếp vào khẳng định. |
| Theo phát hiện | Có hành vi, bằng chứng hoặc phản biện mới làm yếu khẳng định. |

Không áp một chu kỳ ngày cố định cho mọi khẳng định. `Rapidly changing` phải có điều kiện trước khi sử dụng hoặc ngày kiểm tra tiếp theo; `Version-bound` phải nêu phiên bản; `Stable` vẫn cần điều kiện nếu nguồn của nó có thể thay đổi cách diễn giải.

### 1.3. Định tuyến khi không thuộc phạm vi

| Nguyên nhân gốc | Quy trình chịu trách nhiệm |
|---|---|
| Câu chữ, chỉ dẫn, thực hành, đánh giá hoặc hướng dẫn giảng viên cần đổi | `complete-goal-lessons` |
| Lịch, nhịp độ, cấu hình tổ chức hoặc điểm kiểm tra của lộ trình cần đổi | `compose-learning-run` |
| Mục tiêu, quan hệ phụ thuộc hoặc cam kết chương trình cần đổi | `change-curriculum-architecture` |
| Bằng chứng dạy thử hoặc trạng thái `Validated` bị ảnh hưởng | `pilot-and-validate` |

Khẳng định có bằng chứng mới nhưng dẫn đến đánh đổi sản phẩm vẫn cần cổng quyết định của con người; nghiên cứu không chọn ưu tiên thay chủ sở hữu giáo trình.

## 2. Nguồn sở hữu và cấu trúc sổ khẳng định

Mỗi nội dung sử dụng khẳng định bên ngoài sở hữu `references.md` gần nó nhất. Trong trường hợp thông thường, đó là `ai-native-builder/goals/gNN-*/references.md`; tài nguyên dùng chung hoặc lộ trình chỉ có `references.md` riêng khi chính chúng chứa khẳng định bên ngoài độc lập.

Không tạo danh mục khẳng định trung tâm. Mỗi lượt chạy chỉ tạo hàng đợi dẫn xuất trong thư mục vận hành:

```text
.agents/workflow-runs/<run-id>/
├── orchestration-log.md
├── trigger-input.md
├── volatile-claim-queue.md
├── impact-map.md
├── review.md
└── handoff.md
```

Hàng đợi dẫn xuất không thay `references.md` và không được dùng làm nguồn cho bài học.

- `trigger-input.md` ghi ngày tham chiếu, chế độ, tín hiệu theo ngày/phiên bản/sự kiện/trước sử dụng và nguồn của tín hiệu. Với lượt chỉ dựa trên ngày, tệp vẫn ghi rõ không có tín hiệu ngoài lịch.
- `impact-map.md` là bản phân tích dẫn xuất từ claim tới nội dung phụ thuộc; nó không tự đổi trạng thái chất lượng.
- `review.md` chỉ do Người kiểm định độc lập ghi cho phạm vi bắt buộc kiểm định.
- `handoff.md` ghi từng đơn vị nhận, trạng thái tiếp nhận và điều kiện tái nhập. Hồ sơ quyết định của con người được liên kết từ tệp này hoặc lưu cùng thư mục lượt chạy khi có cổng F.

### 2.1. Mã khẳng định

Mã phải ổn định trong phạm vi sở hữu và có tiền tố phạm vi, ví dụ `g07-c01`, `shared-verification-c02` hoặc `run-workshop-c01`. Không tái sử dụng mã cho một mệnh đề khác.

### 2.2. Bảng khẳng định bắt buộc

`references.md` dùng ít nhất hai bảng chuẩn tách biệt. Bảng khẳng định ghi mệnh đề và trạng thái; bảng bằng chứng ghi từng nguồn. Tệp của một `gNN` có thể có thêm bảng `Đối chiếu tiền lệ giáo trình`; lượt bảo trì chỉ cập nhật bảng này khi nguồn tiền lệ hoặc hệ quả thiết kế của nó thực sự thay đổi.

```md
## Sổ khẳng định

| Mã khẳng định | Khẳng định | Loại khẳng định | Độ cập nhật cần thiết | Tác động quyết định | Mức rủi ro | Phán quyết | Ngày kiểm tra | Phiên bản/phạm vi | Vị trí sử dụng | Điều kiện kiểm tra lại | Ngày kiểm tra tiếp theo |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Sổ bằng chứng

| Mã khẳng định | Mã nguồn | Nguồn | Thẩm quyền | Ngày công bố/cập nhật | Ngày kiểm tra | Phiên bản/phạm vi | Chiều bằng chứng | Phần được hỗ trợ | Giới hạn |
|---|---|---|---|---|---|---|---|---|---|
```

Giá trị chuẩn trong bảng kỹ thuật:

```text
Required currency: Stable | Version-bound | Rapidly changing
Risk level: Low | Medium | High | Critical
Verdict: Supported | Partially supported | Not supported | Contradicted | Inconclusive
Evidence direction: Supporting | Falsifying | Limiting
```

`Ngày kiểm tra tiếp theo` dùng `YYYY-MM-DD` hoặc `—` khi điều kiện kiểm tra lại không dựa trên ngày. `Điều kiện kiểm tra lại` vẫn bắt buộc trong cả hai trường hợp.

## 3. Hai chế độ thực hiện

| Chế độ | Khi dùng | Phạm vi | Điều kiện đóng |
|---|---|---|---|
| Làm mới có mục tiêu | Một hay một nhóm khẳng định cụ thể được kích hoạt. | Chỉ các khẳng định, nguồn và tệp phụ thuộc đã nêu. | Có phán quyết, phân tích ảnh hưởng và điều kiện kiểm tra lại mới. |
| Rà soát trước phát hành | Cần kiểm tra mức sẵn sàng của kho trước phát hành hoặc chu kỳ bảo trì. | Quét toàn kho để lập hàng đợi, rồi chỉ nghiên cứu sâu khẳng định quá hạn, thiếu dữ liệu, rủi ro cao hoặc có phiên bản lệch. | Hàng đợi được xử lý, trì hoãn có lý do hoặc bàn giao rõ ràng. |

Rà soát trước phát hành không có nghĩa là nghiên cứu lại mọi khẳng định từ đầu.

## 4. Sơ đồ tổng thể và trạng thái

```text
TRIGGER
  ↓
SCAN LOCAL CLAIM LEDGERS
  ↓
BUILD DERIVED DUE QUEUE
  ↓
PRIORITIZE BY RISK AND DECISION IMPACT
  ↓
DEFINE BOUNDED CLAIM UNIT
  ↓
RESEARCH SUPPORTING AND FALSIFYING EVIDENCE
  ↓
ASSIGN VERDICT AND ANALYZE IMPACT
  ├── Supported
  │      → UPDATE METADATA → INDEPENDENT REVIEW → CLOSE
  ├── Partially supported
  │      → ROUTE NARROWING TO OWNER → CLOSE
  ├── Not supported or Contradicted
  │      → MARK DEPENDENT CONTENT AT RISK
  │      → ROUTE TO OWNER → CLOSE
  └── Inconclusive
         ├── Safety or critical claim → BLOCK USE → ROUTE → CLOSE
         └── Non-critical claim → RECORD LIMITATION → REVIEW → CLOSE
```

```text
Queued → Scanned → Prioritized → Researching → Verdict assigned → Impact mapped
                                                                      ├── Routed → Closed
                                                                      ├── Blocked → Closed
                                                                      └── Reviewed → Closed

Any state ──→ Awaiting decision ──→ return to the affected state
```

`Blocked` là trạng thái của lượt bảo trì hoặc phạm vi sử dụng, không tự thay trạng thái chất lượng của toàn giáo trình. Tệp phụ thuộc chỉ đổi trạng thái chất lượng sau kiểm định của quy trình sở hữu.

Khi kết thúc, Điều phối viên phải ghi đúng một kết quả lượt chạy, tách khỏi trạng thái chất lượng của nội dung:

```text
Refreshed             = bằng chứng và siêu dữ liệu đã cập nhật, không còn thay đổi phụ thuộc bắt buộc.
Closed with handoff   = phần thuộc workflow này đã xong, nhưng nội dung phụ thuộc còn phải được workflow sở hữu xử lý.
Blocked from use      = phạm vi phụ thuộc đã được bảo vệ khỏi sử dụng và có điều kiện gỡ chặn.
Awaiting decision     = chưa thể đóng vì thiếu quyết định của chủ sở hữu.
```

Không dùng `Closed` đơn lẻ và không diễn giải `Closed with handoff` là “nội dung đã được sửa”.

## 5. Đầu vào, đầu ra và quyền sở hữu

### 5.1. Đầu vào tối thiểu

| Đầu vào | Bên cung cấp | Điều phối viên phải làm |
|---|---|---|
| Điều kiện kích hoạt hoặc yêu cầu bảo trì | Người dùng, lịch bảo trì, nguồn chính thức, dạy thử hoặc người kiểm định | Ghi khẳng định, phạm vi và lý do; không biến tín hiệu thành kết luận. |
| `references.md` chịu ảnh hưởng | Kho dự án hiện hành | Đọc sổ khẳng định, sổ bằng chứng và nơi khẳng định được dùng. |
| Nội dung phụ thuộc | Kho dự án hiện hành | Đọc phần bài học, lộ trình hoặc tài nguyên sử dụng khẳng định. |
| Tín hiệu ngoài lịch | Thông báo chính thức, yêu cầu trước sử dụng, dạy thử, người dùng hoặc người kiểm định | Ghi tín hiệu và nguồn trong `trigger-input.md`; không yêu cầu bộ quét cục bộ tự suy ra thay đổi bên ngoài. |
| Ràng buộc an toàn và quyết định | Quy tắc hiện hành, người dùng hoặc chủ sở hữu giáo trình | Xác định điều gì có thể cập nhật theo dữ kiện và điều gì cần cổng quyết định. |

### 5.2. Đầu ra và chủ sở hữu

| Đầu ra | Bên tạo hoặc cập nhật | Bên nghiệm thu |
|---|---|---|
| Hàng đợi dẫn xuất `volatile-claim-queue.md` | Điều phối viên | Điều phối viên kiểm tra cấu trúc và phạm vi |
| Phán quyết, nguồn và siêu dữ liệu trong `references.md` | Người nghiên cứu | Người kiểm định độc lập cho khẳng định trọng yếu |
| `impact-map.md` | Người phân tích ảnh hưởng | Người kiểm định độc lập cho ảnh hưởng trọng yếu |
| `review.md` | Người kiểm định độc lập | Điều phối viên kiểm tra tính đầy đủ, không đổi phán quyết |
| `handoff.md` | Điều phối viên | Quy trình nhận xác nhận đủ điều kiện bắt đầu hoặc ghi trì hoãn/chặn rõ ràng |
| Cờ chặn sử dụng an toàn | Điều phối viên dựa trên bằng chứng đã kiểm tra | Người kiểm định độc lập hoặc Chủ sở hữu giáo trình |
| Hồ sơ quyết định | Chủ sở hữu giáo trình khi có đánh đổi | Chủ sở hữu giáo trình |

Quy trình này chỉ được sửa trực tiếp `references.md`, hàng đợi dẫn xuất và hồ sơ quyết định phù hợp. Phần giải thích, hướng dẫn, bài thực hành, lịch hoặc mục tiêu phải được bàn giao về tệp và quy trình sở hữu.

## 6. Vai trò và mô hình điều phối tác nhân

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Phân loại kích hoạt, tạo hàng đợi, khóa phạm vi và bàn giao | Tự chọn công cụ hoặc ưu tiên sản phẩm |
| Người nghiên cứu | Kiểm chứng thuận/nghịch và cập nhật sổ khẳng định | Sửa nội dung phụ thuộc hoặc tự chọn đánh đổi |
| Người phân tích ảnh hưởng | Lần từ khẳng định sang các tệp và trạng thái bị ảnh hưởng | Nâng trạng thái chất lượng bằng suy đoán |
| Người kiểm định độc lập | Đọc nguồn, phán quyết và ảnh hưởng trực tiếp | Tự nghiệm thu phần mình đã nghiên cứu hoặc sửa |
| Chủ sở hữu giáo trình | Chọn khi thay đổi liên quan ưu tiên, chi phí, quyền hạn hoặc phạm vi | — |

Vai trò không mặc nhiên tương ứng một tác nhân AI mới. Khi chạy quy trình, gọi `$workflow-orchestration` và áp dụng [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md) trước mỗi đơn vị công việc.

```text
ROOT ORCHESTRATOR: A, B, and H
  ├── Research agent: C → D
  ├── Impact analysis agent: E
  ├── Human curriculum owner: F, only when required
  └── Independent review agent: G
      └── Evidence adjudicator: only for material disputed findings
```

- Một tác nhân nghiên cứu nên giữ C và D để bằng chứng và phán quyết dùng cùng mô hình mệnh đề.
- E có thể tách khi số tệp phụ thuộc đủ lớn hoặc khi cần cô lập ngữ cảnh nghiên cứu khỏi phân tích ảnh hưởng.
- G là lượt tác nhân mới, không tham gia nghiên cứu, cập nhật `references.md` hoặc phân tích ảnh hưởng cho phạm vi được kiểm định.
- H không được ghi `Pass` thay G nếu quy trình có thay đổi trọng yếu.

```text
Required isolation: G for high, critical, changed, or routed claims
Preferred continuity: C → D
Conditional specialist: E
Human-only gate: F
Parallel-safe units: non-overlapping claim units with no shared references.md
Shared-file exclusion: one writer per references.md
Spawn verification: required only when the runtime lacks compatible recorded evidence
```

## 7. Các giai đoạn thực hiện

### Giai đoạn A — Tiếp nhận, quét và tạo hàng đợi

**Chủ trì:** Điều phối viên  
**Kỹ năng:** `$curriculum-reference-research`

1. Xác định chế độ, điều kiện kích hoạt, phạm vi kho và ngày tham chiếu.
2. Ghi `trigger-input.md`. Bộ quét cục bộ chỉ phát hiện điều kiện theo ngày, verdict cần xử lý và lỗi ledger; tín hiệu theo phiên bản, sự kiện hoặc trước sử dụng phải được đưa vào tường minh từ đầu vào này.
3. Chạy [`scan_volatile_claims.py`](scripts/scan_volatile_claims.py) theo chế độ chỉ đọc để tìm `references.md`, kiểm tra cả sổ khẳng định lẫn sổ bằng chứng và lập hàng đợi. Dùng `--release-sweep` cho rà soát trước phát hành để kiểm tra thêm độ bao phủ của các gói bài học đã được soạn.
4. Lưu hàng đợi tại `.agents/workflow-runs/<run-id>/volatile-claim-queue.md` cùng mã lượt chạy.
5. Hợp nhất tín hiệu ngoài lịch vào hàng đợi mà không thay dữ liệu gốc. Một claim có thể giữ nhiều lý do kích hoạt.
6. Đưa các khẳng định thiếu cấu trúc, thiếu nguồn, ngày kiểm tra, vị trí sử dụng hoặc điều kiện kiểm tra lại vào hàng đợi sửa dữ liệu; không coi là đã kiểm chứng.
7. Trong lượt trước phát hành, nếu có gói bài học đã soạn nhưng không có `references.md`, hoặc phạm vi dùng chung/lộ trình chứa claim ngoài độc lập nhưng chưa khai báo ledger, ghi `Coverage not verified`; không được kết luận toàn kho không có claim đến hạn.

Lệnh chuẩn, thêm `--release-sweep` ở chế độ rà soát trước phát hành:

```text
python .agents/workflows/scripts/scan_volatile_claims.py --root ai-native-builder --as-of YYYY-MM-DD --output .agents/workflow-runs/<run-id>/volatile-claim-queue.md --strict [--release-sweep]
```

**Điều kiện kết thúc:** có hàng đợi giới hạn hoặc kết luận không có khẳng định nào thuộc phạm vi.

### Giai đoạn B — Ưu tiên và khóa đơn vị khẳng định

**Chủ trì:** Điều phối viên  
**Kỹ năng:** `$curriculum-reference-research`

Ưu tiên theo thứ tự: `Critical` về an toàn, quyền hạn hoặc dữ liệu; `High` ảnh hưởng trực tiếp lời hứa với học viên; khẳng định `Rapidly changing` quá hạn; khẳng định thiếu nguồn hoặc có phiên bản lệch; rồi tới các khẳng định còn lại.

Mỗi đơn vị chỉ chứa một khẳng định hoặc một nhóm mệnh đề không tách được, cùng danh sách tệp sử dụng, phiên bản/phạm vi, điều gì sẽ hỗ trợ hoặc làm yếu nó và ngân sách nghiên cứu. Không nhóm các công cụ khác nhau chỉ vì cùng thuộc một bài học.

**Điều kiện kết thúc:** mỗi đơn vị có mệnh đề có thể bác bỏ, phạm vi, tiêu chí bằng chứng và chủ sở hữu rõ ràng.

### Giai đoạn C — Nghiên cứu có giới hạn

**Chủ trì:** Người nghiên cứu  
**Kỹ năng:** `$curriculum-reference-research`

1. Ưu tiên tài liệu, đặc tả, chính sách và ghi chú phát hành chính thức; dùng nghiên cứu gốc hoặc tổ chức có trách nhiệm khi khẳng định không thuộc hành vi sản phẩm.
2. Tìm bằng chứng ủng hộ, bằng chứng bác bỏ hoặc làm hẹp, rồi đối chiếu ngày, phiên bản, đối tượng và điều kiện áp dụng.
3. Phân biệt dữ kiện với lựa chọn sư phạm hoặc ưu tiên sản phẩm.
4. Dùng tối đa ba lượt tìm kiếm có mục tiêu cho mỗi khẳng định. Có thể tăng ngân sách cho `Critical` khi Điều phối viên ghi lý do.
5. Khi hết ngân sách mà chưa kết luận được, ghi `Inconclusive`, điều còn thiếu và điều kiện kiểm tra lại; không tìm vô hạn.

**Điều kiện kết thúc:** có bằng chứng đủ để ra phán quyết trung thực hoặc có giới hạn được ghi rõ.

### Giai đoạn D — Cập nhật phán quyết và sổ bằng chứng

**Chủ trì:** Người nghiên cứu  
**Kỹ năng:** `$curriculum-reference-research`

Trong `references.md`, cập nhật phán quyết, nguồn thuận/nghịch, ngày kiểm tra, phiên bản/phạm vi, giới hạn và điều kiện kiểm tra lại. Không sao chép hướng dẫn bên ngoài; chỉ ghi kết luận cần cho quyết định giáo trình.

Không xóa bằng chứng cũ chỉ vì có nguồn mới. Giữ hàng nguồn cũ khi nó còn giúp giải thích lịch sử và ghi rõ giới hạn hoặc việc đã bị thay thế. Mỗi lần verdict, phiên bản/phạm vi hoặc tập nguồn trọng yếu thay đổi, thêm một hàng vào phần `Nhật ký làm mới` trong `references.md`:

```md
## Nhật ký làm mới

| Run ID | Mã khẳng định | Thời điểm | Giá trị trước | Giá trị sau | Nguồn thêm/thay thế | Lý do |
|---|---|---|---|---|---|---|
```

Git history là bằng chứng bổ trợ, không thay nhật ký này.

| Phán quyết | Xử lý dữ liệu tham khảo |
|---|---|
| `Supported` | Cập nhật ngày, phạm vi và điều kiện kiểm tra lại. |
| `Partially supported` | Ghi phiên bản hoặc điều kiện hẹp được hỗ trợ; tạo ảnh hưởng yêu cầu thu hẹp nội dung. |
| `Not supported` | Ghi rõ nguồn không xác lập mệnh đề; đánh dấu vị trí sử dụng cần sửa hoặc loại bỏ. |
| `Contradicted` | Ghi bằng chứng đối lập và ưu tiên phân tích ảnh hưởng; không giữ nguyên nội dung phụ thuộc. |
| `Inconclusive` | Ghi điều thiếu, giới hạn và điều kiện kiểm tra lại; không biến thành `Supported` vì thuận tiện. |

**Điều kiện kết thúc:** sổ khẳng định và sổ bằng chứng phản ánh đúng bằng chứng hiện có, không có kết luận vượt nguồn.

### Giai đoạn E — Phân tích ảnh hưởng và chặn rủi ro

**Chủ trì:** Người phân tích ảnh hưởng  
**Kỹ năng:** `$curriculum-quality-review`

Lần từ từng mã khẳng định qua vị trí sử dụng tới bài học, lộ trình, tài nguyên dùng chung, bằng chứng dạy thử và trạng thái chất lượng. Với mỗi tệp, ghi trong `impact-map.md` một trong các giá trị `No change`, `Metadata updated`, `Update required`, `Reverify`, `Invalidate`, `Block use` hoặc `Not verified`, cùng lý do, phiên bản tệp đã đọc và quy trình sở hữu.

Nếu khẳng định `High` hoặc `Critical` bị `Contradicted`, `Not supported` hoặc `Inconclusive` và liên quan an toàn, dữ liệu, quyền hạn, chi phí hoặc hành động bên ngoài, Điều phối viên phải đặt cờ `Block use` cho phạm vi phụ thuộc và bàn giao ngay. Cờ này là biện pháp phòng ngừa, không phải kết luận rằng toàn bộ giáo trình thất bại.

**Điều kiện kết thúc:** có bản đồ ảnh hưởng, lộ trình bàn giao và phạm vi bị chặn hoặc cần kiểm định lại rõ ràng.

### Giai đoạn F — Cổng quyết định của con người

**Chủ trì:** Chủ sở hữu giáo trình

Cổng này chỉ bắt buộc khi dữ kiện yêu cầu một lựa chọn: đổi công cụ hay mô hình; tăng chi phí hoặc quyền hạn; thu hẹp lời hứa; thay đổi hỗ trợ cho học viên; chọn giữa phương án tương thích; hoặc thay đổi mục tiêu, quan hệ phụ thuộc và phạm vi.

Chủ sở hữu ghi `Accept`, `Reject`, `Defer` hoặc `Escalate` trong hồ sơ quyết định. Cập nhật ngày kiểm tra, thêm nguồn tương đương hoặc điều chỉnh phạm vi bằng chứng mà không đổi nội dung phụ thuộc không cần cổng này.

**Điều kiện kết thúc:** mọi thay đổi phụ thuộc vào ưu tiên có quyết định, hoặc lượt dừng ở `Awaiting decision`.

### Giai đoạn G — Kiểm định độc lập

**Chủ trì:** Người kiểm định độc lập  
**Kỹ năng:** `$curriculum-quality-review`

Kiểm định bắt buộc với khẳng định `High` hoặc `Critical`, phán quyết đổi, nguồn thay thế làm đổi phạm vi, cờ `Block use` hoặc mọi lượt có bàn giao sửa nội dung. Người kiểm định phải đọc trực tiếp mệnh đề, nguồn, phạm vi, bằng chứng nghịch, bảng ảnh hưởng và điều kiện kiểm tra lại, rồi ghi kết quả theo từng claim vào `review.md`.

Với khẳng định `Low` hoặc `Medium` chỉ cập nhật siêu dữ liệu mà không đổi phán quyết hay ảnh hưởng, có thể kiểm tra cục bộ có ghi bằng chứng. Tuy nhiên, lượt rà soát trước phát hành phải có kiểm định độc lập cho toàn bộ hàng đợi được đóng.

Với finding trọng yếu của G, áp dụng mục 6.4 của [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). Người nghiên cứu phản hồi finding về claim/evidence; Người phân tích ảnh hưởng phản hồi finding về impact map; bên còn lại là phía thứ ba của đánh giá `Out of scope` nếu độc lập với người phản hồi và reviewer. Nếu finding đồng thời chạm cả hai, Điều phối viên phải gọi một Người đánh giá ảnh hưởng mới. Chỉ finding `Accept` cục bộ mới quay về D hoặc E để sửa rồi kiểm định lại; finding từng tranh chấp, bị thu hẹp trọng yếu hoặc đổi phạm vi cần reviewer mới xác nhận.

`Not verified` chỉ được ghi sau khi cạn đường kiểm tra theo mục 6.4. Nó thông báo Chủ sở hữu, tạo `Awaiting decision`, giữ cờ `Block use` khi có rủi ro và không cho phép kết quả `Refreshed`; công việc không phụ thuộc có thể tiếp tục.

**Điều kiện kết thúc:** phán quyết và ảnh hưởng trọng yếu đạt `Pass`, hoặc đã có `Awaiting decision`/hồ sơ Chủ sở hữu cho `Not verified` theo giao thức; trường hợp sau chỉ có thể đi tới `Closed with handoff` hoặc `Blocked from use`.

### Giai đoạn H — Bàn giao và đóng lượt

**Chủ trì:** Điều phối viên

1. Bàn giao phần cần sửa sang đúng quy trình sở hữu, kèm mã khẳng định, phán quyết, nguồn, tệp ảnh hưởng, cờ chặn, thay đổi nhỏ nhất và điều kiện kiểm định lại.
2. Nếu thay đổi được áp dụng, đánh dấu bằng chứng dạy thử hoặc kiểm định cũ bị ảnh hưởng; không xóa lịch sử.
3. Ghi điều kiện kiểm tra lại tiếp theo cho mọi khẳng định đã xử lý.
4. Trong `handoff.md`, mỗi đơn vị phải có trạng thái `Accepted`, `Deferred` kèm chủ sở hữu và ngày/điều kiện quay lại, hoặc `Blocked` kèm biện pháp bảo vệ và điều kiện gỡ chặn.
5. Ghi một kết quả lượt chạy trong bốn giá trị ở mục 4. Chỉ đóng lượt khi tất cả đơn vị được cập nhật hoặc có trạng thái bàn giao hợp lệ; `Awaiting decision` không phải kết quả đóng.

**Điều kiện kết thúc:** không còn khẳng định trọng yếu không có phán quyết, chủ sở hữu hoặc điều kiện kiểm tra lại.

## 8. Kiểm chứng

### 8.1. Kiểm tra xác định

1. Mọi `references.md` có ít nhất hai bảng chuẩn, mã khẳng định không trùng trong phạm vi quét và không có hàng bắt buộc bị thiếu; bảng đối chiếu tiền lệ, nếu có, không thay hai bảng này.
2. Mọi khẳng định có ít nhất một hàng bằng chứng liên kết bằng mã; cặp claim–source không trùng, cùng một mã nguồn không ánh xạ tới nhiều nguồn khác nhau trong một `references.md`, và không có bằng chứng trỏ tới claim không tồn tại; các trường ngày, chiều bằng chứng và giá trị chuẩn đều hợp lệ.
3. Mọi khẳng định `Version-bound` có phiên bản/phạm vi; mọi khẳng định `Rapidly changing` có ngày kiểm tra tiếp theo hoặc điều kiện trước khi sử dụng.
4. Hàng đợi dẫn xuất chỉ có tệp tham chiếu và siêu dữ liệu cần thiết, không sao chép khẳng định thành nguồn chuẩn.
5. Phép quét tự động không truy cập mạng và không sửa `references.md`.
6. Lượt trước phát hành có kết quả kiểm tra độ bao phủ ledger; `Coverage not verified` ngăn kết luận “không có claim đến hạn”.

### 8.2. Kiểm định ngữ nghĩa

```text
Dependent instruction
  → Claim ID
  → Claim scope
  → Supporting and falsifying evidence
  → Verdict
  → Impact map
  → Owning workflow
  → Recheck trigger
```

Người kiểm định lần theo từng đường. Một nguồn mới không đủ nếu nó không hỗ trợ đúng mệnh đề, phiên bản và phạm vi đang được dạy. Một thông báo công cụ mới cũng không tự chứng minh việc chuyển công cụ là phù hợp với người học.

### 8.3. Giới hạn và mất hiệu lực

- Nguồn không truy cập được không đồng nghĩa khẳng định sai; phải tìm nguồn thay thế hoặc ghi `Inconclusive`.
- `Inconclusive` chặn sử dụng khi khẳng định liên quan an toàn, dữ liệu, quyền hạn, chi phí hoặc kết quả bắt buộc; với phạm vi khác, ghi giới hạn rõ ràng và điều kiện kiểm tra lại.
- Khi nội dung phụ thuộc thay đổi, ngày kiểm tra cũ vẫn giữ giá trị lịch sử nhưng không được suy ra cho mệnh đề hoặc phiên bản mới.
- Không được nâng `Currency` hoặc trạng thái chất lượng chỉ vì ngày kiểm tra vừa được cập nhật; kết luận phải dựa trên nguồn và ảnh hưởng đã được kiểm định.

## 9. Hợp đồng giao việc cho tác nhân AI nhẹ

Mỗi đơn vị công việc chỉ có một vai trò chính, một nhóm khẳng định không chồng tệp và một danh sách đầu ra tường minh:

```text
Role: <Orchestrator | Researcher | Impact analyst | Independent reviewer | Evidence adjudicator>
Mode: <Targeted refresh | Release sweep>
Run directory: <.agents/workflow-runs/run-id>
Claim IDs: <explicit IDs>
Trigger inputs: <dated, version, event, pre-use, or discovery signals>
Allowed files: <explicit file list>
Canonical inputs: <references.md, dependent files, relevant rules>
Research budget: <maximum targeted searches>
Required skills: <skill names or None>
Required outputs: <verdict, evidence rows, impact map, handoff, and finding disposition/adjudication when applicable>
Local gate: <machine checks and semantic pass conditions>
Decision status: <Not required | Awaiting decision | Recorded>
Stop conditions: <missing source access, unresolved material conflict, scope expansion, budget exhausted>
Do not: <survey tools, change dependent content, select product preference, self-approve material verdict>
```

| Giai đoạn | Vai trò | Kỹ năng |
|---|---|---|
| A–B | Điều phối viên | `$curriculum-reference-research` |
| C–D | Người nghiên cứu | `$curriculum-reference-research` |
| E | Người phân tích ảnh hưởng | `$curriculum-quality-review` |
| F | Chủ sở hữu giáo trình | Không giao cho AI quyết định |
| G | Người kiểm định độc lập | `$curriculum-quality-review` |
| G khi có tranh chấp dữ kiện | Người phân xử bằng chứng độc lập | Đọc dossier theo `agent-dispatch-protocol.md` 6.4–6.5 |
| H | Điều phối viên | Chỉ bàn giao và đóng lượt |

Tác nhân không tự chuyển giai đoạn. Nó trả về bằng chứng đã đọc, phán quyết, giới hạn, kiểm tra đã chạy và lý do dừng cho Điều phối viên.

## 10. Điều kiện đóng quy trình

1. Hàng đợi dẫn xuất có nguồn, phạm vi và lý do kích hoạt rõ ràng.
2. Mọi khẳng định đã xử lý có phán quyết, nguồn thuận/nghịch, phiên bản/phạm vi, ngày và điều kiện kiểm tra lại.
3. Mọi ảnh hưởng tới bài học, lộ trình, kiến trúc, dạy thử hoặc an toàn có chủ sở hữu và bàn giao phù hợp.
4. Cờ `Block use` còn lại có lý do, phạm vi, người chịu trách nhiệm và điều kiện gỡ chặn.
5. Khẳng định trọng yếu, phán quyết đã đổi và lượt trước phát hành đã qua kiểm định độc lập. `Not verified` chỉ cho phép kết thúc bằng `Closed with handoff` hoặc `Blocked from use` khi giới hạn, chủ sở hữu, phạm vi kiểm tra lại và biện pháp bảo vệ đã rõ; nó không đủ cho `Refreshed`.
6. Không có nội dung phụ thuộc nào bị sửa trực tiếp ngoài `references.md` và hồ sơ quyết định mà quy trình này sở hữu.
7. Nếu có tác nhân con, sổ thực thi đạt điều kiện của `agent-dispatch-protocol.md`.
8. `handoff.md` có xác nhận `Accepted`, hoặc trạng thái `Deferred`/`Blocked` đủ điều kiện; không còn bàn giao chỉ tồn tại trong hội thoại.
9. Điều phối viên đã ghi đúng một kết quả lượt chạy: `Refreshed`, `Closed with handoff` hoặc `Blocked from use`. `Awaiting decision` giữ lượt mở.

Quy trình này xác nhận bằng chứng và tuyến xử lý của thông tin dễ lỗi thời. Nó không tự chứng minh hiệu quả học tập, không thay kiểm định dạy thử và không thay quyết định sản phẩm của con người.

## 11. Điều kiện chuyển quy trình sang `Active`

Quy trình chỉ chuyển từ `Proposed` sang `Active` khi người dùng chấp nhận kết quả của một lượt chạy thử có kiểm soát và các điều kiện sau đều đạt:

1. Bộ quét xác minh được cả sổ khẳng định, sổ bằng chứng, liên kết claim–source và độ bao phủ của gói bài học trong chế độ trước phát hành.
2. Thử ít nhất ba đường: claim đến hạn vẫn `Supported`; claim đổi phạm vi thành `Partially supported`; claim `High` hoặc `Critical` bị làm yếu và dẫn tới `Block use` hoặc bàn giao bắt buộc.
3. Mọi đầu ra của lượt thử nằm ở đường dẫn chuẩn, có thể tái lập từ nguồn và không biến hàng đợi dẫn xuất thành nguồn chuẩn thứ hai.
4. Một verdict hoặc phạm vi thay đổi để lại lịch sử trước/sau và không xóa bằng chứng cũ cần cho truy vết.
5. Người kiểm định độc lập có thể lần từ nội dung phụ thuộc tới claim, nguồn, verdict, ảnh hưởng, bàn giao và điều kiện kiểm tra lại.
6. Kết quả đóng phân biệt được `Refreshed`, `Closed with handoff`, `Blocked from use` và `Awaiting decision`; không có nội dung chưa được bảo vệ bị trình bày như đã làm mới xong.
7. Thử nghiệm xác nhận workflow không sửa trực tiếp bài học, lộ trình, kiến trúc hoặc trạng thái dạy thử ngoài phạm vi sở hữu.
