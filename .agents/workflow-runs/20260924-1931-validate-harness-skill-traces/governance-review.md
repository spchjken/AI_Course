# Kiểm định quản trị độc lập

- **Reviewer:** `/root/skill_execution_traces_governance_review`
- **Baseline:** `a65e86caff89feb4e7c065fa5a22443a83d4d23e`
- **Candidate evidence commit:** `cd811a4d8ff8fb6d0374d16985d6f13f60758f63`
- **Phán quyết:** `Fail`
- **Lý do:** còn bốn finding `Major` chưa được disposition và sửa: `STE-001` đến `STE-004`. Theo cổng giai đoạn H, candidate chưa đủ điều kiện `Pass` hoặc `Ratify`.

## Phạm vi và tính độc lập

Reviewer đọc trực tiếp nguồn chuẩn, workflow/giao thức, ba `SKILL.md` bị sửa, toàn bộ implementation/schema/tests, decision record, hồ sơ lượt chạy, Git diff/log/status, raw trace local và tài liệu portable hiện có. Kết luận không dựa vào phán quyết tự đánh giá trong `validation-report.md`; reviewer chỉ ghi `governance-review.md` và `review-findings.md`, không sửa implementation.

## Kết quả theo tiêu chí

| Tiêu chí | Kết quả | Bằng chứng chính |
|---|---|---|
| An toàn đường dẫn và Windows | `Fail` | `skill_trace.py:53-57` chỉ chặn symlink, không chặn Windows junction. Fixture trên Python 3.14 báo `is_symlink=False`, `is_junction=True`; `start` đã tạo execution directory trong target ngoài repository root rồi lỗi `ValueError` tại `skill_trace.py:247`. Xem `STE-001`. |
| Schema, validator và lifecycle | `Fail` | Schema yêu cầu kiểu chuỗi và `additionalProperties: false` tại `skill-trace.schema.json:18-46`; validator ép kiểu bằng `str(...)` tại `skill_trace.py:318,327`, chỉ kiểm tra skill keys bằng `issubset` tại `331-335`, không kiểm tra kiểu `parent_workflow_run`/`agent_id`, và không cấm nhiều event `started`. Fixture schema-invalid vẫn được validator trả `valid: true`, exit `0`. Xem `STE-002`. |
| Riêng tư của aggregate | `Fail` | `skill_trace.py:466-475` nhóm cả trace invalid theo raw `skill`/`sha256`. Fixture invalid với marker `PRIVATE_MARKER_DO_NOT_EXPORT` xuất marker hai lần trong aggregate dù payload tự ghi `counts-only; no summaries or refs`. Xem `STE-003`. |
| Sáu kịch bản cố định và comparison | `Fail` | Test hiện có xanh nhưng không chạy concurrency thật, không chứng minh append không viết lại lịch sử, không thử absolute Windows path/junction, không kiểm schema JSON đã commit và không kiểm aggregate trước trace invalid. Do đó claim `6/6` tại `validation-report.md:5-17` lớn hơn bằng chứng. Xem `STE-004`. |
| Append/concurrency assumptions | `Minor concern` | Lock `O_EXCL` bảo vệ một writer nhưng `.append.lock` không có metadata, timeout hay stale-lock recovery (`skill_trace.py:176-198`); crash có thể khóa trace vĩnh viễn. Xem `STE-005`. |
| Raw trace ignore và derived-index exclusion | `Pass` | `git check-ignore -v` xác nhận raw `manifest.json`/`events.jsonl` bị nested `.gitignore` chặn; chỉ `README.md` và `.gitignore` được track. `index-config.json:25-26` loại cả `temp/**` và `.agent-execution-runs/**`; generated index không chứa raw trace entry. |
| Aggregate không chứa summary/ref trong trace hợp lệ | `Pass có giới hạn` | Aggregate từ hai raw trace thật không chứa request/event summary hoặc refs; unit test hiện có cũng đạt. Kết quả không bao phủ trace invalid, là nguyên nhân `STE-003`. |
| Skill hash và Git evidence | `Pass có giới hạn` | Hai raw manifest ghi full baseline HEAD, dirty state và SHA-256; hash hiện tại của `repo-skill-creator` và `workflow-orchestration` khớp manifest. Baseline/candidate branch/implementation commit kiểm chứng được. `implementation-log.md:7` vẫn ghi evidence commit là pending dù commit review là `cd811a4`; cần đồng bộ trước ratification. |
| Giới hạn không có platform hook | `Pass` | Giới hạn được nêu rõ trong `execution-tracing/README.md:3`, decision record, implementation log và central contract; không có claim capture tự động tuyệt đối trong nguồn được commit. |
| Central contract và độ phình skill | `Pass` | Hợp đồng chung nằm trong `AGENTS.md`; chỉ ba skill chịu ảnh hưởng được thêm chỉ dẫn hẹp, không nhân bản schema/CLI trong mọi skill. Cả ba validator skill đạt. |
| `.gitignore` và quyền sở hữu | `Pass` | Diff baseline..candidate không chạm root `.gitignore`; dirty change `temp/*` tồn tại ngoài hai candidate commit và được ghi là pre-existing. Candidate chỉ thêm nested `.agent-execution-runs/.gitignore`. |
| Migration và rollback | `Pass` | `migration-and-rollback.md` không backfill lịch sử, giữ raw evidence tới expiry, rollback bằng revert commit mới và không đụng root `.gitignore`. |
| Tài liệu portable | `Minor concern` | `temp/generalizable-agent-harness-patterns.md:484` nói validator phải báo invocation thiếu, nhưng code chỉ liệt kê trace directory hiện có (`skill_trace.py:438-448`) và không thể suy ra invocation bị bỏ qua. Tệp cũng bị ignore nên thay đổi portable không tái dựng được từ candidate commit. Xem `STE-006`. |
| Hồ sơ orchestration tự tuân thủ hợp đồng mới | `Minor concern` | `orchestration-log.md` liệt kê execution ID trong cột output nhưng thiếu cột `Skill trace` và thiếu `trace_path` theo `agent-dispatch-protocol.md`; workflow trace đang mở dưới 24 giờ là hợp lệ trong lúc lượt chạy còn tiếp tục. Xem `STE-007`. |

## Phép kiểm tra đã chạy

```text
python -X utf8 -m unittest discover -s .agents/execution-tracing/tests -v
=> 7/7 pass

python -X utf8 .agents/skills/repo-skill-creator/scripts/quick_validate.py <affected-skill>
=> 3/3 pass

python -X utf8 -m unittest discover -s .agents/indexing/tests -v
=> 8/8 pass

python -X utf8 .agents/execution-tracing/skill_trace.py validate --all
=> 2 traces valid; 1 closed, 1 open dưới 24 giờ; exit 0

python -X utf8 .agents/execution-tracing/skill_trace.py aggregate --output temp/governance-review-skill-trace-aggregate.json --force
=> counts-only cho hai trace thật; file tạm đã xóa

python -X utf8 .agents/indexing/validate_index.py --index .agents/generated/context-index.json
=> schema valid nhưng stale orchestration-log; exit 1

python -X utf8 .agents/indexing/sync_index.py --check
=> exit 1

git diff --check a65e86caff89feb4e7c065fa5a22443a83d4d23e..cd811a4d8ff8fb6d0374d16985d6f13f60758f63
=> pass
```

Index failure hiện tại đến từ `orchestration-log.md` đã được Điều phối viên cập nhật sau evidence commit để mở work unit review; thêm chính hai tệp review cũng sẽ làm index stale. Đây không phải finding implementation riêng, nhưng index phải được tái sinh và cả `validate_index.py` lẫn `sync_index.py --check` phải đạt sau khi review/disposition ổn định và trước ratification.

Quét candidate/hồ sơ/raw trace theo các mẫu private key, OpenAI/GitHub/AWS token và credential phổ biến không thấy dữ liệu nhạy cảm thật; chuỗi duy nhất khớp là token giả trong negative unit test. Fixture review và aggregate tạm đã được xóa.

## Điều kiện để re-review

1. Disposition đầy đủ cho mọi finding; sửa `STE-001` đến `STE-004` trước khi xin `Pass`.
2. Bổ sung test Windows junction/symlink, schema/lifecycle tamper, invalid-trace aggregate, concurrency/append và toàn bộ mệnh đề của sáu kịch bản đã khóa.
3. Đồng bộ hồ sơ Git/skill trace, đóng trace workflow khi lượt kết thúc, sửa claim portable và tái sinh index sau khi hồ sơ ổn định.
4. Re-review phải chạy trên commit mới, giữ nguyên baseline và chỉ chấp nhận khi không còn `Blocker`/`Major`.

---

## Re-review commit `956e742`

- **Ngày re-review:** 2026-09-25
- **Corrective commit:** `956e742` (`Harden skill trace validation after review`)
- **Phán quyết:** `Fail`
- **Lý do:** `STE-001`, `STE-002` và `STE-004` vẫn còn `Major`; `STE-005` và `STE-007` còn `Minor`. `STE-003` và `STE-006` đã đóng bằng bằng chứng trực tiếp.

Reviewer đọc lại corrective diff, implementation/docs/tests/disposition, raw traces và portable export; không tin kết luận sửa của bên thực hiện. Implementation không bị reviewer sửa.

### Kết quả đóng finding

| Finding | Re-review | Bằng chứng |
|---|---|---|
| `STE-001` | `Reopened — Major` | Junction/reparse root và nested directory nay bị từ chối, nhưng Windows hardlink của `events.jsonl` vẫn vượt bảo vệ. Fixture thay `events.jsonl` bằng hardlink tới file ngoài fixture repo; lệnh `event` exit `0` và file ngoài tăng từ 111 lên 209 byte. `reject_link_or_reparse` tại `skill_trace.py:63-70` không kiểm `st_nlink`; append tại `223-233` mở hardlink bằng `ab`. |
| `STE-002` | `Reopened — Major` | Exact nested manifest types và nhiều lifecycle invariant đã được thêm, nhưng `seq` không được kiểm kiểu. Fixture đổi event đầu thành `"seq": true`; `validate` trả `valid: true`, exit `0`, vì `True == 1` tại `skill_trace.py:503-504`. JSON schema vẫn cho phép nhiều giá trị mà validator từ chối (`repository.head`, `started_at`, skill name/path và slug chỉ có type, thiếu pattern/format), nên schema/validator chưa tương đương hai chiều. |
| `STE-003` | `Resolved` | `aggregate_command` bỏ mọi item invalid trước khi dùng dimension (`skill_trace.py:590-601`). Fixture marker invalid trả `invalid_count: 1`, `valid_count: 2` và marker không xuất hiện trong file aggregate. |
| `STE-004` | `Reopened — Major` | Suite tăng lên 13 test và đã bao phủ process start concurrency, junction, UNC, invalid aggregate, prefix sau terminal rejection và một số mutation. Tuy nhiên nó không bắt hardlink escape hay non-integer `seq`, không chạy official schema, không thử concurrent writers, và prefix assertion không kiểm một successful append. Vì candidate vẫn có hai lỗi Major trong chính scenario path/lifecycle, claim corrected `6/6` chưa trung thực. |
| `STE-005` | `Unresolved — Minor` | Lock hợp lệ stale/dead được thu hồi, nhưng lock rỗng/malformed do crash trong lúc ghi metadata không bao giờ được thu hồi: fixture lock rỗng cũ một giờ vẫn trả exit `2` và tồn tại. 12 concurrent `event` processes chỉ ghi được 3 note; trace không hỏng nhưng phần còn lại bị từ chối ngay, chưa có test hay tài liệu hóa single-writer/nonblocking assumption. |
| `STE-006` | `Resolved` | Portable export dòng 484 nay nói invocation thiếu chỉ phát hiện được khi có expected roster độc lập; nếu không coverage là `Not verified`. Trạng thái local/ignored được disposition ghi rõ. |
| `STE-007` | `Partially resolved — Minor` | Orchestration log đã có cột `Skill trace` và đủ ID/path cho ST-1/ST-2. Tuy nhiên chưa có work-unit row cho corrective implementation/re-review, `implementation-log.md` vẫn ghi corrective commit `pending`, và workflow trace vẫn open. Các mục này phải hoàn tất trước final handoff/ratification. |

### Phép kiểm tra re-review

```text
python -X utf8 -m unittest discover -s .agents/execution-tracing/tests -v
=> 13/13 pass, gồm 2 Windows junction fixtures

python -X utf8 <skill-validator> <each affected skill>
=> 3/3 pass

python -X utf8 -m unittest discover -s .agents/indexing/tests -v
=> 8/8 pass

python -X utf8 .agents/execution-tracing/skill_trace.py validate --all
=> 2/2 valid; 1 closed, 1 open dưới 24 giờ; exit 0

Adversarial Windows hardlink events.jsonl fixture
=> event exit 0; outside file 111 -> 209 bytes: Fail

Adversarial lifecycle fixture with first event seq=true
=> validator valid=true, exit 0: Fail

Adversarial invalid-trace aggregate marker fixture
=> marker absent; invalid_count=1: Pass

Adversarial empty stale lock fixture
=> event exit 2; stale lock remains: Minor concern

12 concurrent event processes on one trace
=> final trace valid, only 3 note events persisted; nonblocking writer failures observed

python -X utf8 .agents/indexing/validate_index.py --index .agents/generated/context-index.json
=> schema valid; 6 stale sources; exit 1

python -X utf8 .agents/indexing/sync_index.py --check
=> exit 1
```

Index chưa được tái sinh sau corrective commit và sẽ tiếp tục stale khi hai tệp reviewer thay đổi. Đây là cổng pre-ratification còn pending, không phải nguyên nhân chính của verdict hiện tại.

### Điều kiện re-review tiếp theo

1. Chặn hardlink/multi-link write target hoặc mở append theo cơ chế không-follow/identity-safe; thêm fixture chứng minh file ngoài không đổi.
2. Kiểm exact type cho event `seq` (`int`, không phải `bool`) và đồng bộ JSON schema với mọi constraint mà validator coi là contract; thêm schema con cho events hoặc tài liệu/schema máy đọc tương đương.
3. Mở rộng scenario tests cho successful append prefix, concurrent-writer contract và malformed stale-lock recovery; sửa `6/6` chỉ sau khi toàn bộ biến thể đã khóa đạt.
4. Hoàn tất lifecycle evidence, đóng workflow trace, đồng bộ corrective commit/work units và tái sinh index trước ratification.

---

## Final re-review commit `f416cc0`

- **Ngày:** 2026-09-25
- **Candidate:** `f416cc0` (`Close skill trace safety gaps`)
- **Phán quyết:** `Fail`
- **Finding chặn:** `STE-002`, `STE-004` và `STE-005` còn `Major`. `STE-001`, `STE-003` và `STE-006` đã đóng. `STE-007` chỉ còn các bước final handoff, không được tính là lỗi implementation.

### Đối chiếu từng finding

| Finding | Final re-review | Bằng chứng |
|---|---|---|
| `STE-001` | `Resolved` | Fixture hardlink độc lập: `event` exit `2`, file ngoài không đổi; junction tests cũng đạt. Code kiểm multi-link cả trước open và trên file handle (`skill_trace.py:65-74, 232-245`). |
| `STE-002` | `Unresolved — Major` | Bool/float `seq` nay bị từ chối. Tuy nhiên schema parity vẫn sai trên input an toàn/riêng tư quan trọng: chính helper schema của candidate trả `true` cho manifest ref `ftp://example.com/x`, `..\outside.md`, URL có credentials/query; validator trả `false`. `skill-event.schema.json` chỉ yêu cầu ref là non-empty string nên cũng nhận `../outside.md`. Manifest slug `../run` được schema nhận nhưng `validate_slug` từ chối. Xem finding chi tiết bên dưới. |
| `STE-003` | `Resolved` | Invalid aggregate marker không xuất hiện; `invalid_count=1`. Summary/ref của trace hợp lệ vẫn không xuất ra aggregate. |
| `STE-004` | `Unresolved — Major` | Successful append-prefix, hardlink, seq typing và nhiều regression đã có test. Tuy nhiên schema parity matrix và cross-process writer behavior chưa được test đúng; suite dùng threads cho writer serialization. Hai lỗi Major còn tái hiện nên báo cáo `16/16` và `6/6` vẫn vượt bằng chứng. |
| `STE-005` | `Unresolved — Major` | Malformed stale lock cũ đã phục hồi đúng. Nhưng fixture 4 process trên Windows tạo race giữa waiter đọc lock và owner `unlink`: hai command thành công, một command ghi event rồi exit với `WinError 32`, một command còn chờ sau 10 giây; 3 notes đã tồn tại và `.append.lock` mồ côi giữ PID của process đã lỗi. Đây là outcome mơ hồ, có thể gây duplicate khi retry và trái claim “concurrent writers without event loss”. |
| `STE-006` | `Resolved` | Portable guidance tiếp tục giữ expected-roster/no-platform-hook limitation đúng. |
| `STE-007` | `Pending final handoff — không phải lỗi implementation` | ST-4 đến ST-6 đã được ghi và trace column/path tồn tại. Việc ghi SHA `f416cc0`, thêm final-review work unit, đóng workflow trace và tái sinh index chỉ có thể hoàn tất sau kết luận này; chúng là cổng handoff/ratification, không làm thay đổi verdict code. |

### Phép kiểm tra final

```text
python -X utf8 -m unittest discover -s .agents/execution-tracing/tests -v
=> 16/16 pass

python -X utf8 <skill-validator> <each affected skill>
=> 3/3 pass

python -X utf8 -m unittest discover -s .agents/indexing/tests -v
=> 8/8 pass

python -X utf8 .agents/execution-tracing/skill_trace.py validate --all
=> 2/2 valid; workflow trace còn open dưới 24 giờ; exit 0

Hardlink adversarial fixture
=> event exit 2; outside bytes unchanged: Pass

seq=true và seq=1.0 fixtures
=> cả hai invalid, exit 2: Pass

Malformed stale lock cũ một giờ
=> event exit 0; lock removed: Pass

Invalid aggregate marker
=> marker absent; invalid_count=1: Pass

Schema parity adversarial matrix
=> Fail: manifest/event schemas nhận unsafe refs/slug mà validator từ chối

4 cross-process concurrent event writers on Windows
=> Fail: 2 clean success; 1 WinError 32 after event write; 1 still waiting; orphan lock; 3 notes present

python -X utf8 .agents/indexing/validate_index.py --index .agents/generated/context-index.json
=> schema valid; 7 stale sources; exit 1

python -X utf8 .agents/indexing/sync_index.py --check
=> exit 1
```

Root `.gitignore` vẫn không thuộc candidate diff; raw traces vẫn bị nested ignore và excluded khỏi derived index. Quét credential pattern không phát hiện secret thật ngoài token giả trong negative test.

### Điều kiện cho lần re-review kế tiếp

1. Làm cho manifest/event schema từ chối cùng ref/slug/timestamp mà validator từ chối; thêm adversarial parity matrix hai chiều, không chỉ generated-data/type smoke test.
2. Sửa Windows cross-process lock để waiter không giữ file handle chặn owner unlink; command không được báo lỗi sau khi event đã commit. Thêm subprocess fixture lặp lại đủ để bắt race và xác nhận mọi command outcome khớp đúng một event.
3. Chỉ khôi phục claim `6/6` khi hai finding trên đóng. Sau reviewer `Pass`, Điều phối viên mới hoàn tất `STE-007`, tái sinh index và mở ratification gate.

---

## Re-review candidate `20ab1c9`

- **Ngày:** 2026-09-25
- **Candidate:** `20ab1c9` (`Make skill trace locking process safe`)
- **Phán quyết:** `Fail`
- **Finding chặn:** `STE-002` và `STE-004` còn `Major`. Race đa tiến trình của `STE-005` đã đóng; còn một hạn chế migration `Minor` với lock-file do candidate trước để lại. `STE-007` vẫn là công việc vòng đời final handoff, không phải lỗi implementation.

### Kết quả theo finding

| Finding | Re-review `20ab1c9` | Bằng chứng |
|---|---|---|
| `STE-001` | `Resolved` | 17/17 tests tiếp tục đạt, gồm junction và hardlink; hardlink target ngoài không bị ghi. Không có hồi quy path-containment đã đóng. |
| `STE-002` | `Unresolved — Major` | Các case yêu cầu `ftp`, `..\\outside.md`, URL credentials/query, `../outside.md` trong event và slug `../run` nay đều bị schema lẫn validator từ chối. Tuy nhiên parity hai chiều vẫn sai: recorder chấp nhận và lưu nguyên `https://example.com/a b` trong manifest/event; validator trả `valid: true`, còn cả schema trả `false`. Manifest đã chỉnh thành `docs\\file.md` và timestamp `+00:00` cũng được validator nhận nhưng schema từ chối. Một trace do chính CLI tạo có thể vì vậy “valid” theo validator nhưng invalid theo machine-readable contract. |
| `STE-003` | `Resolved` | Invalid dimensions/privacy test tiếp tục đạt; aggregate không xuất summary/ref hay marker từ trace invalid. Raw runtime vẫn ignored và excluded khỏi index. |
| `STE-004` | `Unresolved — Major` | Test mới đã thêm subprocess writer thật và matrix các unsafe ref đã nêu, nhưng schema test vẫn một chiều: chỉ assert schema từ chối bốn input, không chứng minh mọi trace validator nhận cũng khớp schema. Fixture URL có khoảng trắng tái hiện trace CLI-generated mà report `6/6` gọi hợp lệ dù schema không nhận. Vì primary metric yêu cầu schema/lifecycle validity, claim `6/6` vẫn vượt bằng chứng. |
| `STE-005` | `Resolved` cho lock-directory hiện tại; `Minor` migration | 8 vòng độc lập × 24 Windows subprocess đều đạt: 192/192 command success, mỗi vòng đúng 24 note duy nhất, sequence liên tục, trace valid và không orphan lock. Empty/malformed/dead-owner/extra-regular stale lock-directory đều phục hồi; hai fixture 12-process tranh phục hồi cũng đạt exactly-once. Tuy nhiên stale `.append.lock` **file** từ `f416cc0` gây `NotADirectoryError [WinError 267]` và không được thu hồi sau đổi format; đây là khoảng trống migration của trial, không tái hiện race hiện hành. |
| `STE-006` | `Resolved` | No-platform-hook/expected-roster limitation và portable guidance không hồi quy. |
| `STE-007` | `Pending final handoff — không phải lỗi implementation` | Workflow trace đang mở, SHA corrective/final review và derived index refresh chỉ nên hoàn tất sau review. `validate_index.py` hiện chỉ báo 7 stale sources, đúng với trạng thái candidate/reviewer chưa bàn giao. |

### Phép kiểm tra độc lập

```text
python -X utf8 -m unittest discover -s .agents/execution-tracing/tests -v
=> 17/17 pass, gồm Windows junction, hardlink và subprocess writers

python -X utf8 .agents/skills/repo-skill-creator/scripts/quick_validate.py <affected-skill>
=> 3/3 pass

python -X utf8 -m unittest discover -s .agents/indexing/tests -v
=> 8/8 pass

python -X utf8 .agents/execution-tracing/skill_trace.py validate --all
=> 2/2 valid; 1 closed, workflow trace open dưới 24 giờ; exit 0

Required ref/slug matrix
=> ftp, backslash traversal, credentials, query, ../ event ref và ../ slug: schema=false, validator=false

Extended two-way schema matrix
=> FAIL: URL có khoảng trắng do CLI tạo, stored backslash ref và +00:00 timestamps đều validator=true/schema=false

8 rounds × 24 real Windows subprocess writers
=> 192/192 success; exactly 192 unique notes; contiguous seq; 0 orphan locks; 8/8 valid traces

Stale/partial lock-directory fixtures
=> empty, empty owner, malformed owner, dead owner, extra regular file: recovered; prefix retained; trace valid
=> 12-process simultaneous recovery from empty/malformed stale directories: all success, exactly-once, no orphan lock

Legacy stale lock-file fixture from previous candidate
=> NotADirectoryError [WinError 267]; lock file remains; events unchanged

python -X utf8 .agents/indexing/validate_index.py
=> schema valid; 7 stale sources; exit 1 (final-handoff state)

python -X utf8 .agents/indexing/sync_index.py --check
=> exit 1 (final-handoff state)
```

Root `.gitignore` vẫn là thay đổi có sẵn của người dùng và không thuộc candidate diff. Quét pattern chỉ thấy token giả trong negative test. Không có file implementation nào bị reviewer sửa.

### Điều kiện đóng còn lại

1. Đồng bộ grammar mà validator và hai schema chấp nhận, ít nhất với URL whitespace, stored backslash ref và timestamp syntax; test phải kiểm **hai chiều**, gồm trace thực do CLI tạo từ mọi input được chấp nhận.
2. Chỉ giữ claim `6/6` sau khi fixture trên chứng minh mọi completed trace được validator nhận cũng được schemas nhận.
3. Xử lý hoặc tài liệu hóa migration cho stale lock-file từ candidate trước; đây là `Minor`, không phải finding chặn độc lập.
4. Sau reviewer `Pass`, mới thực hiện các bước `STE-007`: ghi SHA/review row, đóng workflow trace, tái sinh và kiểm index, rồi trình ratification.
