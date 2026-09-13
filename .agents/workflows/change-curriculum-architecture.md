# Quy trình thay đổi kiến trúc giáo trình

- **Trạng thái:** `Proposed` — đã chạy thử có kiểm soát; hồ sơ `20260912-2149-change-curriculum-context-rebalance` còn `Awaiting decision`
- **Mục tiêu:** thay đổi hoặc đồng bộ kiến trúc giáo trình mà không làm mất dấu lý do, quan hệ phụ thuộc, bằng chứng hay trách nhiệm của các quy trình phía sau.
- **Phạm vi:** cam kết cấp chương trình, ranh giới mục tiêu, điều kiện tiên quyết, quan hệ phụ thuộc, sản phẩm trung gian được chuyển giao và cách các mục tiêu được sắp vào chương trình.
- **Ngoài phạm vi:** viết nội dung bài học, sửa lịch dạy thuần túy, phân tích buổi dạy thử, cập nhật riêng một khẳng định dễ lỗi thời hoặc cấp trạng thái `Validated`.

Đây là cơ chế quản trị thay đổi, không phải đường khởi đầu bắt buộc của việc xây dựng giáo trình.

## 1. Khi nào cần dùng

### 1.1. Phép thử kích hoạt

Dùng quy trình này nếu thay đổi dự kiến làm đổi ít nhất một yếu tố:

1. Kết quả quan sát được mà một mục tiêu hứa hẹn.
2. Ranh giới trách nhiệm giữa các mục tiêu.
3. Điều kiện tiên quyết hoặc thứ tự phụ thuộc.
4. Sản phẩm trung gian đầu vào, đầu ra hoặc nơi tiếp nhận nó.
5. Cam kết cấp chương trình về đối tượng học viên, phạm vi, thời lượng hoặc kết quả cuối.
6. Cách một năng lực được phân bổ giữa các mục tiêu, kể cả năng lực xuyên suốt và mục tiêu riêng.

Nếu vấn đề có thể được sửa mà giữ nguyên cả sáu yếu tố, không dùng quy trình này.

### 1.2. Trường hợp điển hình

- Thêm, tách, gộp, đổi thứ tự, đổi tên, loại bỏ hoặc làm rõ một mục tiêu `gNN`.
- Thay đổi điều kiện tiên quyết hoặc quan hệ phụ thuộc.
- Chuyển năng lực hay sản phẩm trung gian giữa các mục tiêu.
- Thay đổi cam kết, đối tượng học viên, phạm vi hoặc thời lượng chương trình.
- Bằng chứng dạy thử cho thấy nguyên nhân gốc nằm ở cấu trúc.
- Các nguồn chuẩn mâu thuẫn về mục tiêu hoặc quan hệ phụ thuộc.
- Một thay đổi làm mất hiệu lực nhiều bài học hoặc chương trình dạy.

### 1.3. Định tuyến khi không thuộc phạm vi

| Nguyên nhân gốc | Quy trình chịu trách nhiệm |
|---|---|
| Nội dung hoặc bài thực hành của một mục tiêu đã chốt | `complete-goal-lessons` |
| Lịch, nhịp độ hoặc cách ghép bài mà không đổi mục tiêu | `compose-learning-run` |
| Thu thập và phân tích bằng chứng sau dạy thử | `pilot-and-validate` |
| Khẳng định về công cụ, giao diện lập trình, mô hình, giá hoặc chính sách có thể lỗi thời | `refresh-volatile-content` |

Nếu chưa rõ nguyên nhân gốc, chỉ thực hiện giai đoạn A; không mặc định nâng lỗi liên mục tiêu thành thay đổi kiến trúc.

## 2. Hai chế độ thực thi

### 2.1. Đồng bộ nguồn chuẩn

Dùng khi một quyết định có thẩm quyền đã tồn tại nhưng nguồn cấp thấp hơn bị lệch. Chế độ này không được tạo ý nghĩa mới và chỉ được thực hiện không cần xin lại quyết định thiết kế khi:

- hồ sơ quyết định hoặc nguồn cấp cao hơn nói rõ kết quả cần đồng bộ;
- yêu cầu hiện tại cho phép áp dụng;
- phân tích ảnh hưởng xác nhận không có hệ quả ngữ nghĩa mới.

Nếu có điểm mơ hồ hoặc hệ quả mới, chuyển sang chế độ thay đổi kiến trúc và dừng tại cổng quyết định.

### 2.2. Thay đổi kiến trúc

Dùng khi thay đổi làm đổi ý nghĩa, ranh giới hoặc quan hệ của chương trình. Phải có đề xuất, phân tích phương án và sự chấp thuận tường minh của con người trước khi sửa nguồn chuẩn.

## 3. Sơ đồ tổng thể

```text
TRIGGER
  ↓
CAPTURE GIT BASELINE → CREATE DEDICATED RUN BRANCH/WORKTREE
  ↓
INTAKE AND CLASSIFICATION
  ├── Local lesson issue ─────────────→ complete-goal-lessons
  ├── Learning-run issue ─────────────→ compose-learning-run
  ├── Volatile-content issue ─────────→ refresh-volatile-content
  ├── Pilot-analysis issue ───────────→ pilot-and-validate
  ├── Canonical synchronization ──────→ IMPACT ANALYSIS
  └── Architecture-change candidate
          ↓
      PROBLEM DIAGNOSIS → EVIDENCE REVIEW → DESIGN ALTERNATIVES
          ↓
      BEFORE/AFTER DEPENDENCY GRAPH → IMPACT AND MIGRATION ANALYSIS
          ↓
      HUMAN DECISION GATE
          ├── Reject → Record no-change decision → CLOSE
          ├── Revise → DESIGN ALTERNATIVES
          └── Approve
                  ↓
              APPLY PROVISIONAL CHANGES ON RUN BRANCH → MIGRATE DEPENDENT REFERENCES
                  ↓
              INDEPENDENT VERIFICATION
                  ├── Finding → DISPOSITION AND ADJUDICATION
                  │                  ├── Accept → bounded repair → re-review
                  │                  ├── Dispute → evidence response → independent adjudication
                  │                  ├── Out of scope → two-of-three confirmation → handoff
                  │                  └── Semantic/Not verified → HUMAN DECISION GATE
                  ├── Failed accepted repair → repair, escalate or rollback
                  └── Pass → HUMAN RATIFICATION
                          ↓
                      INTEGRATE APPROVED COMMITS
                          ↓
                      INVALIDATE STALE EVIDENCE
                          ↓
                      ROUTE TO OWNING WORKFLOWS → CLOSE
```

```text
Queued → Baseline captured → Triaged → Diagnosed → Designed → Awaiting decision
                                             ├── Rejected → Closed
                                             ├── Revision requested → Designed
                                             └── Approved → Provisionally applied → Under review
                                                                                  ├── Finding disputed → Awaiting adjudication
                                                                                   ├── Finding not verified → Awaiting adjudication
                                                                                   ├── Failed → Repair or Rolled back
                                                                                   └── Verified → Awaiting ratification
                                                                                                             ├── Rejected → Rolled back
                                                                                                             └── Ratified → Integrated → Closed
```

## 4. Đầu vào, trách nhiệm chuẩn bị và đầu ra

Điều phối viên chịu trách nhiệm bảo đảm bộ đầu vào đủ cho từng giai đoạn, nhưng không được tự tạo bằng chứng còn thiếu, tự xác lập tiền đề thực tế hoặc tự quyết định thay chủ sở hữu giáo trình.

### 4.1. Đầu vào tối thiểu để khởi động

| Đầu vào | Bên cung cấp | Điều phối viên phải làm |
|---|---|---|
| Yêu cầu hoặc phát hiện ban đầu | Người dùng hoặc quy trình phát hiện vấn đề | Ghi nguyên văn vấn đề, nguồn phát hiện và kết quả mong muốn; không tự diễn giải thành quyết định kiến trúc |
| Bằng chứng hiện có | Bên đưa ra phát hiện | Gắn bằng chứng với mệnh đề nó hỗ trợ; ghi rõ phần chưa có bằng chứng |
| Nguồn chuẩn nền | Kho dự án hiện hành | Định vị và đọc kế hoạch chương trình, kiến trúc nội dung và bản đồ chương trình |
| Bên có thẩm quyền quyết định | Người dùng hoặc chủ sở hữu giáo trình | Xác nhận ai có quyền chấp thuận nếu lượt thực thi có thể đổi ngữ nghĩa |
| Căn Git và nhánh đích | Kho Git hiện hành | Ghi commit nền, nhánh đích, trạng thái worktree và tạo nhánh hoặc worktree riêng cho lượt chạy trước khi sửa nguồn chuẩn |

Chỉ năm nhóm trên là điều kiện tiếp nhận. Chưa cần biết đầy đủ mọi tệp chịu ảnh hưởng để bắt đầu giai đoạn A.

### 4.2. Đầu vào do Điều phối viên tập hợp

Trước khi kết thúc giai đoạn A, Điều phối viên phải tập hợp hoặc ghi lý do chưa thể tiếp cận:

1. `AI-native-builder-curriculum-plan.md`.
2. `curriculum-content-architecture.md`.
3. `ai-native-builder/curriculum-map.md`.
4. Bản định hướng của các mục tiêu được cho là liên quan ở thời điểm tiếp nhận.
5. Quy tắc hiện hành và hồ sơ quyết định liên quan trong `.agents/decisions/`.
6. Bản bàn giao từ quy trình phát hiện vấn đề, nếu lượt này bắt nguồn từ một quy trình khác.

Điều phối viên chỉ tập hợp và kiểm tra phiên bản, không được sửa các nguồn này trong bước chuẩn bị đầu vào.

### 4.3. Đầu vào được phát hiện trong quá trình thực hiện

Các đầu vào sau không phải điều kiện để mở quy trình vì phạm vi của chúng chỉ rõ dần sau chẩn đoán và phân tích ảnh hưởng:

| Đầu vào được phát hiện | Giai đoạn xác định | Bên chịu trách nhiệm |
|---|---|---|
| Bản định hướng mục tiêu chịu ảnh hưởng đầy đủ | B và E | Người phân tích |
| Bài học, chương trình dạy và tài nguyên dùng chung chịu ảnh hưởng | E | Người phân tích ảnh hưởng |
| Bằng chứng nghiên cứu cần bổ sung | B và C | Người phân tích nêu nhu cầu; Người nghiên cứu thu thập |
| Bằng chứng kiểm định hoặc dạy thử liên quan | B, C và E | Quy trình nguồn cung cấp; Điều phối viên tập hợp |
| Danh sách tệp cần sửa, kiểm định lại hoặc làm mất hiệu lực | E | Người phân tích ảnh hưởng |
| Lựa chọn ưu tiên và quyết định cuối | F | Chủ sở hữu giáo trình |

Không được dùng việc “chưa biết toàn bộ phạm vi ảnh hưởng” làm lý do bỏ qua giai đoạn E.

### 4.4. Xử lý đầu vào còn thiếu

- Nếu đầu vào chưa cần cho giai đoạn hiện tại, ghi vào hồ sơ thực thi cùng thời điểm phải có rồi tiếp tục.
- Nếu đầu vào cần để chẩn đoán hoặc so sánh phương án, giao đúng bên bổ sung và dừng đơn vị công việc phụ thuộc.
- Nếu đầu vào cần cho cổng quyết định hoặc cổng kiểm định, ghi `Not verified`, nêu nguyên nhân, phạm vi kiểm tra lại và dừng tại cổng đó.
- Nếu thiếu quyền truy cập, không được coi đó là bằng chứng rằng nội dung không tồn tại.
- Nếu không xác định được người có thẩm quyền quyết định, không được chuyển sang giai đoạn G.
- Không suy đoán nội dung của nguồn bị thiếu và không để tác nhân AI tự chế tạo bằng chứng thay thế.

### 4.5. Đầu ra bắt buộc và bên chịu trách nhiệm

| Đầu ra | Bên tạo hoặc cập nhật | Bên nghiệm thu |
|---|---|---|
| Hồ sơ quyết định trong `.agents/decisions/YYYY-MM-DD-<slug>.md` | Điều phối viên tổng hợp; Chủ sở hữu giáo trình xác nhận quyết định | Chủ sở hữu giáo trình |
| `git-baseline.md` trong hồ sơ lượt chạy | Điều phối viên | Người thực hiện đối chiếu trước G; Người kiểm định đối chiếu tại H |
| Đồ thị phụ thuộc trước/sau | Người thiết kế và Người phân tích ảnh hưởng | Người kiểm định độc lập |
| Bản đồ ảnh hưởng, kế hoạch chuyển đổi và hoàn tác | Người phân tích ảnh hưởng | Chủ sở hữu giáo trình tại giai đoạn F |
| Nguồn chuẩn đã cập nhật sau chấp thuận | Người thực hiện | Người kiểm định độc lập |
| `review-findings.md` | Người kiểm định độc lập | Điều phối viên kiểm tra tính đầy đủ; không sửa phán quyết của reviewer |
| `finding-disposition.md` | Người thực hiện phản hồi; Điều phối viên ghi đường xử lý; Người phân xử bằng chứng ghi kết quả dữ kiện khi cần; Chủ sở hữu quyết định tranh chấp ngữ nghĩa hoặc `Not verified` | Reviewer hoặc Người phân xử xác nhận finding đã được hiểu đúng |
| Báo cáo kiểm định | Người kiểm định độc lập | Theo cổng chất lượng hiện hành |
| Danh sách bằng chứng hoặc trạng thái bị mất hiệu lực | Điều phối viên dựa trên bản đồ ảnh hưởng đã kiểm định | Người kiểm định độc lập |
| Bản bàn giao tới các quy trình tiếp theo | Điều phối viên | Bên tiếp nhận xác nhận đủ điều kiện bắt đầu |

Hồ sơ quyết định lưu lý do và thẩm quyền, không thay nguồn chuẩn. Quyết định giữ nguyên cũng phải được ghi nếu đã qua phân tích đáng kể.

### 4.6. Cổng căn Git và cô lập lượt chạy

Cổng này chạy trước giai đoạn A và phải đạt trước khi tạo hoặc sửa bất kỳ nguồn chuẩn nào. Hồ sơ vận hành có thể được tạo để ghi lý do dừng, nhưng không được dùng việc đã tạo hồ sơ làm lý do bỏ qua cổng.

1. Xác định kho Git, nhánh đích dự kiến, commit `HEAD` và trạng thái worktree. Ghi thông tin cần thiết vào `.agents/workflow-runs/<run-id>/git-baseline.md`; không lưu bí mật hoặc dữ liệu không liên quan.
2. Tạo nhánh hoặc worktree riêng từ đúng commit nền, mặc định dùng tên `codex/<run-id>`. Không áp dụng thay đổi kiến trúc trực tiếp lên nhánh mặc định hoặc nhánh đích.
3. Nếu worktree hiện tại có thay đổi chưa commit, không tự stash, commit, di chuyển hay hoàn tác chúng. Ưu tiên tạo worktree riêng từ commit nền. Nếu không thể cô lập an toàn, ghi `Baseline not verified` và dừng trước khi sửa nguồn chuẩn.
4. Sau giai đoạn E và ngay trước G, xác nhận mọi tệp mang nhãn `Update` vẫn khớp commit nền hoặc trạng thái đã được Chủ sở hữu chấp thuận. Nếu có drift, dừng, cập nhật phân tích ảnh hưởng và xin lại quyết định; không tự rebase hoặc ghi đè.
5. Mỗi lần áp dụng ở G và mỗi vòng sửa sau H phải nằm trong một commit có phạm vi tường minh trên nhánh lượt chạy. Ghi mã commit, danh sách tệp và finding liên quan vào manifest; không gộp thay đổi ngoài phạm vi.
6. Chỉ tích hợp các commit của lượt chạy vào nhánh đích sau khi H đạt `Pass` cho phạm vi bắt buộc và Chủ sở hữu đã phê chuẩn cuối cùng. Trước thời điểm đó, nội dung trên nhánh lượt chạy là `Provisionally applied`, không phải nguồn chuẩn hiện hành.
7. Khi từ chối trước tích hợp, giữ nhánh và hồ sơ đủ lâu để kiểm toán; không cần sửa nhánh đích. Khi lỗi được phát hiện sau tích hợp, hoàn tác bằng commit mới đảo đúng các commit của lượt chạy. Không dùng `reset --hard`, hoàn tác rộng hoặc xóa lịch sử.

`git-baseline.md` tối thiểu phải có:

```text
Repository: <absolute repository path>
Target branch: <branch>
Baseline commit: <full SHA>
Run branch/worktree: <name and path>
Worktree state: <clean | isolated from listed unrelated changes>
Potentially affected files: <preliminary list or pending until E>
Baseline status: <Verified | Not verified>
Recorded by and time: <identity and timestamp>
```

Thiếu Git, không xác định được commit nền, không tạo được vùng làm việc riêng hoặc không chứng minh được tệp cần sửa chưa bị ghi đè đều là điều kiện dừng. Kế hoạch inverse hunk chỉ là lớp dự phòng kiểm toán, không thay thế căn Git.

## 5. Vai trò và quyền hạn

| Vai trò | Trách nhiệm | Không được làm |
|---|---|---|
| Điều phối viên | Phân loại, khóa phạm vi, quản lý trạng thái, phân xử thủ tục và bàn giao | Tự phê duyệt thay đổi ngữ nghĩa hoặc mặc định reviewer đúng khi finding bị tranh chấp |
| Người phân tích | Chẩn đoán và kiểm tra phương án nhỏ hơn | Biến sở thích thành dữ kiện |
| Người nghiên cứu | Kiểm chứng tiền đề thực tế khi cần | Quyết định thay người dùng |
| Người thiết kế | Tạo phương án, hợp đồng mục tiêu và đồ thị | Sửa bài học chi tiết |
| Người thực hiện | Áp dụng đúng phương án; phản hồi từng finding bằng bằng chứng trước khi sửa | Mở rộng phạm vi khi đang sửa hoặc sửa chỉ vì reviewer đề xuất |
| Người kiểm định | Kiểm tra độc lập cấu trúc, ý nghĩa và ảnh hưởng; trả lời phản biện đối với finding của mình | Tự nghiệm thu phần mình vừa viết hoặc quyết định thay Chủ sở hữu về đánh đổi sản phẩm |
| Chủ sở hữu giáo trình | Chấp thuận, từ chối, yêu cầu sửa, phân xử tranh chấp ngữ nghĩa và phê chuẩn cuối trước tích hợp | — |

### 5.1. Mô hình điều phối tác nhân

Vai trò là ranh giới trách nhiệm, không mặc nhiên tương ứng một tác nhân AI mới. Tên vai trò trong quy trình không phải lệnh tự động sinh tác nhân con. Điều phối viên phải chọn cách thực thi tường minh dựa trên nhu cầu giữ mạch suy luận, chuyên môn, cô lập ngữ cảnh và kiểm định độc lập.

Khi chạy quy trình, gọi `$workflow-orchestration` và áp dụng `.agents/workflows/agent-dispatch-protocol.md` trước mỗi đơn vị công việc. Cấu trúc dưới đây chỉ là gợi ý để Điều phối viên đánh giá sau khi đã có ngữ cảnh:

```text
ROOT ORCHESTRATOR
  ├── Architecture agent: B → D → E
  ├── Research agent: C, only when required
  ├── Human owner: F
  ├── Implementation agent: G
  ├── Independent review agent: H
  ├── Evidence adjudicator: H.2 only when required
  └── ROOT ORCHESTRATOR: A and I
```

- Điều phối viên chính giữ trạng thái toàn lượt, thực hiện A và I, tạo lời nhắc giao việc và không tự thay con người ở F.
- Một tác nhân kiến trúc nên giữ xuyên suốt B, D và E để chẩn đoán, phương án và bản đồ ảnh hưởng dùng cùng một mô hình vấn đề.
- Chỉ sinh tác nhân nghiên cứu ở C khi có tiền đề thực tế cần kiểm chứng. Tác nhân này trả bằng chứng, không chọn phương án sản phẩm.
- G nên do một tác nhân thực hiện nhận gói quyết định đã khóa. Với đồng bộ nhỏ, Điều phối viên có thể thực hiện nếu phạm vi tệp tường minh và H vẫn độc lập.
- H bắt buộc dùng một tác nhân hoặc một lượt thực thi mới không tham gia thiết kế hay áp dụng thay đổi. Nó phải đọc đầu ra từ tệp và bằng chứng, không dựa vào trí nhớ hay lời tự thuật của người thực hiện.

Không sinh tác nhân chỉ vì xuất hiện một tên vai trò. Chỉ tách tác nhân khi ít nhất một điều kiện đúng:

1. Công việc cần chuyên môn hoặc kỹ năng khác biệt.
2. Công việc có thể chạy độc lập mà không phụ thuộc kết quả chưa hoàn thành.
3. Ngữ cảnh hiện tại chứa thiên kiến hoặc chi tiết không cần thiết cho nhiệm vụ mới.
4. Quy tắc yêu cầu kiểm định độc lập.

Nếu môi trường không hỗ trợ tác nhân con, có thể dùng các lượt gọi tuần tự với bản bàn giao qua tệp. Tuy nhiên, một tác nhân chỉ “đổi vai” từ Người thiết kế hoặc Người thực hiện sang Người kiểm định không đáp ứng tính độc lập. Khi chưa có lượt kiểm định độc lập, giai đoạn H phải giữ `Not verified` và quy trình chưa được đóng với kết quả `Pass`.

Ràng buộc phân công riêng của quy trình này:

```text
Required isolation: H
Preferred continuity: B → D → E
Conditional specialist: C
Human-only gate: F
Parallel-safe units: non-overlapping claim groups within C after B is stable
Shared-file exclusion: one writer per canonical file
Spawn verification: required before the first delegated work unit in an unverified runtime
```

## 6. Các giai đoạn thực hiện

### Giai đoạn A — Tiếp nhận và phân loại

**Chủ trì:** Điều phối viên

0. Xác nhận cổng căn Git ở mục 4.6 đạt `Verified`; nếu không, chỉ ghi hồ sơ dừng và không sửa nguồn chuẩn.
1. Viết phát hiện thành mệnh đề có thể kiểm tra: hiện trạng, kết quả mong muốn và chênh lệch.
2. Gắn thao tác `add`, `split`, `merge`, `reorder`, `rename`, `retire` hoặc `clarify`.
3. Áp dụng phép thử kích hoạt; phân loại chế độ thực thi.
4. Liệt kê sơ bộ các tệp và mục tiêu có thể bị ảnh hưởng.
5. Nếu nguyên nhân thuộc quy trình khác, tạo bản bàn giao rồi kết thúc.

**Điều kiện kết thúc:** có lý do kiểm tra được để tiếp tục, hoặc đã định tuyến đúng.

### Giai đoạn B — Chẩn đoán vấn đề

**Chủ trì:** Người phân tích  
**Kỹ năng:** `$curriculum-goal-design`

1. Xác định thất bại của học viên hoặc ràng buộc cấp chương trình.
2. Kiểm tra nguyên nhân là thiếu mục tiêu hay chỉ thiếu giải thích, thực hành, giàn giáo, bằng chứng hoặc thời gian.
3. Mô tả năng lực trước và sau điểm thay đổi bằng hành vi quan sát được.
4. Xác định nơi tiêu thụ năng lực, quyết định hoặc sản phẩm trung gian.
5. Ghi giả định, điều chưa biết và bằng chứng phản đối chẩn đoán.

**Điều kiện kết thúc:** lỗi cấu trúc đã được phân biệt với lỗi triển khai; phương án không đổi kiến trúc đã được cân nhắc.

### Giai đoạn C — Kiểm chứng tiền đề thực tế

**Chủ trì:** Người nghiên cứu  
**Kỹ năng có điều kiện:** `$curriculum-reference-research`

Chỉ chạy khi đề xuất dựa trên khẳng định thực tế có thể kiểm chứng. Tách khẳng định, tìm bằng chứng thuận/nghịch, ghi độ mới và giới hạn, rồi phân biệt dữ kiện với lựa chọn ưu tiên.

**Điều kiện kết thúc:** tiền đề quan trọng được hỗ trợ, bác bỏ, thu hẹp hoặc ghi rõ chưa thể kết luận. Bằng chứng không thay cổng quyết định.

### Giai đoạn D — Thiết kế phương án

**Chủ trì:** Người thiết kế  
**Kỹ năng:** `$curriculum-goal-design`

Nếu có lựa chọn thực tế, tạo: phương án giữ nguyên kiến trúc; thay đổi nhỏ nhất; và một phương án khác có đánh đổi đáng cân nhắc. Với mỗi phương án, ghi:

- vấn đề được và không được giải quyết;
- hợp đồng mục tiêu: đầu vào, hành vi quan sát được, quyết định, sản phẩm trung gian, bằng chứng hoàn thành và nơi sử dụng tiếp;
- lợi ích, chi phí, rủi ro, giả định và khả năng hoàn tác;
- ảnh hưởng tới cam kết, thời lượng và tải nhận thức.

**Điều kiện kết thúc:** có phương án nhỏ nhất khả thi và đủ dữ liệu so sánh, không chỉ một kết luận viết sẵn.

### Giai đoạn E — Đồ thị trước/sau và bản đồ ảnh hưởng

**Chủ trì:** Người phân tích ảnh hưởng  
**Kỹ năng:** `$curriculum-goal-design`

Mỗi cạnh của đồ thị phải nói rõ năng lực hoặc sản phẩm được truyền đi:

```text
BEFORE
gNN [observable outcome]
  └── capability/artifact ──→ gMM [downstream use]

AFTER
gNN [revised observable outcome]
  └── revised capability/artifact ──→ gXX [new or revised downstream use]
```

Bản đồ ảnh hưởng phải bao phủ kế hoạch chương trình, kiến trúc nội dung, bản đồ chương trình, bản định hướng mục tiêu, bài học, bằng chứng kiểm định, chương trình dạy, tài nguyên dùng chung và lớp quản trị nếu liên quan. Mỗi tệp nhận một nhãn `Update`, `Reverify`, `Invalidate`, `No change` hoặc `Not verified`, kèm lý do và chủ sở hữu.

**Điều kiện kết thúc:** có đồ thị, danh sách tệp chính xác, kế hoạch chuyển đổi và hoàn tác. Thay đổi quy tắc chỉ được ghi là ảnh hưởng cần xử lý theo cơ chế quản trị quy tắc, không sửa âm thầm ở đây.

### Giai đoạn F — Cổng quyết định của con người

**Chủ trì:** Chủ sở hữu giáo trình

Gói đề xuất gồm vấn đề và nguyên nhân; bằng chứng thuận/nghịch; các phương án; đồ thị trước/sau; hợp đồng mục tiêu; bản đồ ảnh hưởng; kế hoạch chuyển đổi, hoàn tác; và khuyến nghị có lập luận.

- **Từ chối:** ghi quyết định giữ nguyên và kết thúc.
- **Yêu cầu sửa:** quay lại giai đoạn D, không sửa nguồn chuẩn.
- **Chấp thuận:** khóa phạm vi, phương án và danh sách tệp rồi sang giai đoạn G.

Không sửa nguồn chuẩn trước cổng này, trừ đồng bộ nguồn chuẩn đáp ứng đầy đủ mục 2.1.

### Giai đoạn G — Áp dụng và chuyển đổi

**Chủ trì:** Người thực hiện  
**Kỹ năng:** `$curriculum-goal-design`

Trước khi sửa, đối chiếu commit nền, nhánh/worktree lượt chạy, danh sách tệp và trạng thái có thể khôi phục. Mọi thay đổi ở giai đoạn này là tạm áp dụng trên nhánh lượt chạy; không sửa trực tiếp nhánh đích. Áp dụng theo thứ tự quyền lực:

1. `AI-native-builder-curriculum-plan.md` nếu cam kết chương trình đổi.
2. `curriculum-content-architecture.md`.
3. `ai-native-builder/curriculum-map.md`.
4. Bản định hướng của mục tiêu chịu ảnh hưởng.
5. Tham chiếu trong chương trình dạy.
6. Tài nguyên dùng chung, kỹ năng hoặc quy trình nếu nằm trong phạm vi đã duyệt.

Không viết bài học; không đánh lại số hàng loạt; giữ mã `gNN` nếu danh tính không đổi; mục tiêu mới dùng mã chưa sử dụng tiếp theo; không sửa ngoài danh sách đã duyệt; không mở rộng ý nghĩa khi đồng bộ câu chữ. Sau khi kiểm tra cục bộ, tạo commit triển khai có phạm vi tường minh và ghi mã commit vào manifest trước khi mở H.

**Điều kiện kết thúc:** phương án được áp dụng trọn vẹn và phần chênh lệch chỉ nằm trong phạm vi cho phép.

### Giai đoạn H — Kiểm định độc lập

**Chủ trì:** Người kiểm định không phải người thực hiện duy nhất  
**Kỹ năng:** `$curriculum-quality-review`

#### H.1 — Lập finding

Người kiểm định chạy ba lớp kiểm tra ở mục 7 và ghi từng finding vào `review-findings.md`. Mỗi finding phải có mã ổn định, mức độ, mệnh đề có thể kiểm tra, bằng chứng tệp/phần, hệ quả, phân loại sơ bộ `implementation`, `semantic`, `scope` hoặc `evidence`, cùng phép kiểm tra sẽ chứng minh nó đã được giải quyết. Khuyến nghị sửa của reviewer không tự động trở thành lệnh sửa.

#### H.2 — Phản hồi và phân xử

Áp dụng đầy đủ mục 6.4 của [`agent-dispatch-protocol.md`](agent-dispatch-protocol.md). Trong workflow này, Người phân tích ảnh hưởng là phía thứ ba của biểu quyết `Out of scope`; `High`/`Critical`, hoặc finding bị reviewer phản đối việc coi là ngoài phạm vi, luôn chuyển sang `Awaiting adjudication` thay vì bị đa số bỏ qua.

Người thực hiện phản hồi từng finding trong `finding-disposition.md`; reviewer chỉ được giữ, thu hẹp hoặc rút finding một lần trước khi một Người phân xử bằng chứng độc lập nhận dossier. `Not verified` chỉ được ghi sau khi thỏa toàn bộ điều kiện “đã cạn đường kiểm tra” của giao thức. Nó tạo `Awaiting adjudication`, thông báo Chủ sở hữu, khóa tích hợp và mọi thay đổi phụ thuộc; các đơn vị thực sự độc lập vẫn có thể tiếp tục trên nhánh lượt chạy.

Finding làm đổi ý nghĩa, phạm vi, danh sách tệp hoặc đánh đổi sản phẩm phải dùng `Requires human decision` và quay về F. Điều phối viên chỉ quyết định đường xử lý, không quyết định nội dung thay Chủ sở hữu. Không giao sửa khi finding chưa có disposition; không yêu cầu hai tác nhân tiếp tục tranh luận cho tới khi tự thống nhất.

#### H.3 — Sửa và kiểm định lại

Mỗi vòng sửa phải liên kết `finding ID → commit sửa → expected evidence`. Reviewer đầu chỉ được dùng lại cho finding `Accept` thuộc lỗi triển khai cục bộ. Finding từng `Dispute`, `Need evidence`, bị thu hẹp/rút ở mức trọng yếu hoặc ảnh hưởng nguồn chuẩn phải có lượt review mới xác nhận kết quả cuối, theo dossier và ranh giới độc lập ở mục 6.4 của `agent-dispatch-protocol.md`.

Giới hạn tối đa hai vòng sửa cho cùng một bộ finding. Sau hai vòng vẫn còn cùng lỗi chặn, tranh chấp hoặc `Not verified` trọng yếu, chuyển `Awaiting adjudication` cho Chủ sở hữu với các mệnh đề đối lập và bằng chứng hai phía; không tiếp tục sửa tự động.

#### H.4 — Phê chuẩn cuối

Sau khi các cổng bắt buộc đạt `Pass`, Chủ sở hữu chọn `Ratify`, `Revise` hoặc `Reject`. Chỉ `Ratify` mới cho phép tích hợp các commit của nhánh lượt chạy vào nhánh đích. `Revise` quay lại giai đoạn phù hợp; `Reject` giữ nhánh đích nguyên trạng nếu chưa tích hợp, hoặc kích hoạt hoàn tác có phạm vi nếu đã tích hợp do lỗi vận hành.

**Điều kiện kết thúc:** kiểm định đạt `Pass` và đã `Ratify`, hoặc đã hoàn tác/từ chối và ghi lý do. `Not verified` tại cổng bắt buộc không được coi là đạt; thiếu phê chuẩn cuối không được chuyển sang tích hợp.

### Giai đoạn I — Làm mất hiệu lực và bàn giao

**Chủ trì:** Điều phối viên

1. Sau `Ratify`, xác nhận nhánh đích chưa lệch khỏi căn tích hợp đã được kiểm tra. Nếu có drift ảnh hưởng phạm vi, dừng và kiểm định lại phần giao nhau; không tự ghi đè.
2. Tích hợp đúng các commit đã được phê chuẩn từ nhánh lượt chạy vào nhánh đích và ghi mã commit kết quả. Không đưa finding bị từ chối, commit ngoài phạm vi hoặc thay đổi chưa kiểm định vào cùng lượt.
3. Đánh dấu bằng chứng, kết quả kiểm định và trạng thái không còn đúng.
4. Chỉ làm mất hiệu lực phần có đường ảnh hưởng cụ thể, không hạ trạng thái hàng loạt.
5. Ghi công việc tiếp theo, chủ sở hữu, đầu vào và điều kiện kết thúc.
6. Bàn giao bài học cho `complete-goal-lessons`, chương trình dạy cho `compose-learning-run`, và phần khác cho quy trình sở hữu.
7. Đối chiếu sổ đăng ký tác nhân với căn Git, commit triển khai, finding, disposition, phê chuẩn cuối, commit tích hợp và bằng chứng kiểm định độc lập.
8. Đóng hồ sơ quyết định và hồ sơ thực thi. Không tự xóa nhánh/worktree của lượt chạy; việc dọn dẹp là hành động riêng sau khi xác nhận không còn cần cho kiểm toán.

**Điều kiện kết thúc:** không còn tham chiếu mồ côi; phần mất hiệu lực có chủ sở hữu; lượt sau không cần dựa vào hội thoại.

## 7. Cách kiểm chứng

### 7.1. Trước thay đổi

- [ ] Vấn đề thuộc tầng kiến trúc hoặc là đồng bộ quyết định có thẩm quyền.
- [ ] Đã cân nhắc phương án nhỏ hơn hoặc không đổi kiến trúc.
- [ ] Dữ kiện, suy luận và sở thích được phân biệt.
- [ ] Đã xác định người có quyền quyết định.
- [ ] Có danh sách tệp và cách hoàn tác.
- [ ] Căn Git, nhánh đích và nhánh/worktree lượt chạy đã được ghi và xác minh.
- [ ] Các tệp dự kiến sửa không chứa thay đổi chưa được phép hoặc đã được cô lập an toàn.
- [ ] Thay đổi ngữ nghĩa đã được chấp thuận tường minh.

### 7.2. Cấu trúc và tính nhất quán

- [ ] Không trùng mã mục tiêu, chu trình phụ thuộc hay mục tiêu mồ côi không được giải thích.
- [ ] Điều kiện tiên quyết truy ngược được tới mục tiêu trước hoặc giàn giáo tường minh.
- [ ] Sản phẩm trung gian truy xuôi được tới nơi sử dụng.
- [ ] Không trùng quyền sở hữu kết quả quan sát được và không có bước nhảy độ khó thiếu cầu nối.
- [ ] Kiến trúc nội dung và bản đồ chương trình nhất quán.
- [ ] Chương trình dạy chỉ tham chiếu mục tiêu còn tồn tại; liên kết nội bộ hợp lệ.
- [ ] Phần chênh lệch không vượt danh sách tệp đã duyệt.
- [ ] Chương trình ba buổi vẫn kết thúc bằng nguyên mẫu nội bộ đã được kiểm chứng.
- [ ] Lộ trình đầy đủ vẫn dẫn tới sản phẩm cuối đúng cam kết.

Khi có công cụ tự động, lưu lệnh và kết quả. Nếu kiểm tra thủ công, ghi từng phép kiểm tra, bằng chứng và phần chưa thể xác minh; không chỉ ghi “đã kiểm tra”.

### 7.3. Ngữ nghĩa độc lập

Dùng `$curriculum-quality-review` và các cổng liên quan trong `.agents/rules/quality-gates.md`, đặc biệt là tính tiến triển, khả năng tái sử dụng, khả năng kiểm chứng và tính khả thi về thời gian.

```text
Program promise
  → Goal outcome
  → Prerequisite edge
  → Learner decision
  → Artifact
  → Completion evidence
  → Downstream consumer
  → Learning-run checkpoint
```

Mỗi mắt xích phải có vị trí nguồn. Thiếu nội dung là lỗi cần sửa; thiếu quyền truy cập phải ghi `Not verified`, phạm vi kiểm tra lại và người có thể cung cấp dữ liệu.

Kết quả kiểm định kiến trúc phải tách khỏi trạng thái trưởng thành của bài học hoặc lộ trình. Thiếu bằng chứng dạy thử được ghi `Out of scope` hoặc giới hạn bằng chứng, trừ khi chính thay đổi kiến trúc đưa ra một khẳng định hiệu quả thực nghiệm cần dạy thử để chấp nhận. Không hạ kết quả kiến trúc thành `Needs revision` chỉ vì chưa có pilot; cũng không suy diễn `Pass` kiến trúc thành `Pilot-ready`, `Release-ready` hoặc `Validated`.

## 8. Hoàn tác và xử lý thất bại

- Trước tích hợp, nhánh đích phải còn nguyên; từ chối hoặc lỗi hệ thống không yêu cầu hoàn tác nhánh đích. Giữ nhánh lượt chạy và đánh dấu `Rejected` hoặc `Failed` để điều tra.
- Sau tích hợp, chỉ hoàn tác phần chênh lệch do các commit đã ghi của lượt này sở hữu. Tạo commit đảo có phạm vi trên một nhánh sửa chữa; không dùng thao tác phá hủy rộng, `reset --hard` hoặc xóa lịch sử.
- Trước khi hoàn tác, xác nhận commit đích, danh sách tệp và phần giao với thay đổi đến sau. Nếu có xung đột hoặc nguy cơ ghi đè thay đổi khác, dừng và yêu cầu quyết định.
- Lỗi triển khai chỉ được sửa sau disposition `Accept`, trong phương án đã duyệt, rồi chạy lại phép kiểm tra chịu ảnh hưởng.
- Nếu cần thay đổi ngữ nghĩa mới hoặc finding còn tranh chấp, dừng và quay lại cổng quyết định; không dùng rollback như cách né phân xử.
- Nếu căn Git hoặc commit triển khai không kiểm chứng được, ghi sự cố và không tuyên bố đã khôi phục. Inverse hunk chỉ được dùng như bằng chứng hỗ trợ sau khi đối chiếu với Git.
- Sau hoàn tác, trạng thái là `Rolled back`, không phải `Verified`; hồ sơ quyết định, review và Git không bị xóa.

## 9. Hợp đồng giao việc cho tác nhân AI nhẹ

Mỗi đơn vị chỉ có một vai trò chính, một giai đoạn và danh sách tệp tường minh:

```text
Role: <Orchestrator | Analyst | Researcher | Designer | Implementer | Reviewer | Evidence adjudicator>
Mode: <Canonical synchronization | Architecture change>
Operation: <add | split | merge | reorder | rename | retire | clarify>
Current phase: <A | B | C | D | E | G | H | I>
Baseline commit: <full SHA>
Run branch/worktree: <name and path>
Allowed files: <explicit file list>
Canonical inputs: <required source files>
Required skills: <skill names or None>
Required outputs: <artifacts and exact locations; finding disposition/adjudication when applicable>
Decision status: <Not required | Awaiting approval | Approved | Awaiting adjudication | Ratified | Rejected>
Finding IDs and disposition: <IDs and current status or None>
Stop conditions: <missing authority, unverified baseline, target drift, scope expansion, semantic ambiguity, disputed finding, failed gate>
Do not: <author lesson content, renumber stable IDs, mutate before approval, edit target branch before ratification, auto-accept reviewer findings, expand scope>
```

| Giai đoạn | Vai trò | Kỹ năng |
|---|---|---|
| A | Điều phối viên | Không; dùng tiêu chí định tuyến ở đây |
| B | Người phân tích | `$curriculum-goal-design` |
| C | Người nghiên cứu | `$curriculum-reference-research` khi cần |
| D | Người thiết kế | `$curriculum-goal-design` |
| E | Người phân tích ảnh hưởng | `$curriculum-goal-design` |
| F | Chủ sở hữu giáo trình | Không giao cho AI quyết định |
| G | Người thực hiện | `$curriculum-goal-design` |
| H | Người kiểm định độc lập | `$curriculum-quality-review` |
| H.2 khi có tranh chấp dữ kiện | Người phân xử bằng chứng độc lập | Đọc dossier theo `agent-dispatch-protocol.md` 6.4–6.5 |
| I | Điều phối viên | Chỉ tạo bản bàn giao |

Tác nhân không tự chuyển giai đoạn. Nó trả về đầu ra, phép kiểm tra, điều chưa xác minh và lý do dừng cho điều phối viên.

## 10. Điều kiện đóng quy trình

1. Quyết định thay đổi hoặc giữ nguyên đã được ghi.
2. `git-baseline.md` xác minh được commit nền, nhánh đích và vùng làm việc riêng; mọi commit triển khai, sửa và tích hợp đều truy vết được.
3. Mọi finding có disposition, bằng chứng phản hồi và kết quả kiểm định lại; không còn finding bị tranh chấp hoặc `Not verified` trọng yếu chưa được Chủ sở hữu quyết định.
4. Chủ sở hữu đã ghi `Ratify` trước tích hợp, hoặc đã ghi `Reject`/`Rolled back` và không để thay đổi thử nghiệm trên nhánh đích.
5. Nguồn chuẩn trên nhánh đích nhất quán theo đúng thứ tự quyền lực.
6. Không còn lỗi chặn trong đồ thị và đường truy vết sản phẩm trung gian.
7. Tham chiếu đã cập nhật hoặc có bản bàn giao với chủ sở hữu rõ ràng.
8. Bằng chứng và trạng thái cũ bị ảnh hưởng đã được làm mất hiệu lực có chọn lọc.
9. Kiểm định độc lập đạt `Pass` cho phạm vi thay đổi; giới hạn pilot được ghi riêng, không trộn với phán quyết kiến trúc.
10. Công việc nội dung hoặc chương trình dạy đã được chuyển tới quy trình sở hữu.
11. Nếu đã phân công tác nhân con, sổ thực thi đạt mục 8 của `agent-dispatch-protocol.md`; việc sinh tác nhân và tính độc lập không còn `Not verified`.

Quy trình này chỉ xác nhận tính nhất quán và khả năng bàn giao của kiến trúc; nó không chứng minh hiệu quả thực tế và không được cấp `Validated`.
