# Finding của kiểm định quản trị

## STE-001 — `Major` — Windows junction cho phép ghi trace ra ngoài repository root

- **Mệnh đề:** Runtime root phải là thư mục thật nằm trong repo; mọi write của recorder phải bị giới hạn ở đó trên Windows.
- **Bằng chứng:** `skill_trace.py:53-57` chỉ kiểm tra `candidate.is_symlink()`. Trên fixture Windows/Python 3.14, junction trả `is_symlink=False`, `is_junction=True`. Lệnh `start` đi qua junction, tạo đầy đủ execution directory ở target ngoài fixture repo, sau đó ném `ValueError` không được `main` bắt tại `skill_trace.py:247` vì directory đã resolve không còn relative với repo. `ensure_within` tại `60-67` lấy chính target đã resolve làm parent nên không ngăn được trường hợp này.
- **Hệ quả:** Một junction/reparse point tại `.agent-execution-runs` có thể chuyển manifest/event writes ra ngoài repo và để lại orphan trace sau lỗi. Nested trace directory hoặc `events.jsonl` dạng link cũng chưa được từ chối rõ ràng.
- **Điều kiện đóng:** Từ chối symlink, junction và reparse point tại runtime root, trace directory và file được ghi; xác nhận root resolved vẫn là đúng runtime path trong repo; mọi lỗi phải trả JSON có kiểm soát và không để lại directory ngoài phạm vi. Thêm fixture Windows cho junction root, linked trace dir/file và cleanup an toàn.

## STE-002 — `Major` — Validator không thực thi schema và lifecycle đã công bố

- **Mệnh đề:** `validate` phải từ chối mọi manifest trái `skill-trace.schema.json` và mọi lifecycle không hợp lệ trước khi trace được tính là valid.
- **Bằng chứng:** Schema cấm extra properties và yêu cầu `request_summary`, từng `input_refs`, `parent_workflow_run` và `agent_id` đúng kiểu tại `skill-trace.schema.json:18-46`. Validator lại ép `request_summary`/ref qua `str(...)` (`skill_trace.py:318,327`), chỉ yêu cầu skill object chứa một tập con keys (`331-335`), và không validate hai optional field. Fixture có integer summary/ref, object `parent_workflow_run` và extra key trong `skill` vẫn trả `valid: true`, exit `0`. Với events, `371-418` chỉ đòi event đầu là `started`, giới hạn terminal và parse từng timestamp; không yêu cầu đúng một `started`, timestamp đầu khớp manifest hay thời gian đơn điệu.
- **Hệ quả:** Claim `100% completed trace validity` không có nghĩa “schema/lifecycle valid”; trace hỏng có thể đi vào audit và aggregate như hợp lệ.
- **Điều kiện đóng:** Dùng validator Draft 2020-12 thật hoặc manual validation tương đương hoàn toàn; kiểm exact keys/types cho mọi nested object và optional field. Định nghĩa/validate event schema, đúng một start, tối đa một finish cuối, timestamp nhất quán/không lùi và started event khớp manifest. Thêm tamper fixtures cho từng bất biến.

## STE-003 — `Major` — Aggregate xuất nội dung tùy ý từ trace invalid

- **Mệnh đề:** Aggregate có thể đếm trace invalid nhưng không được sao chép trường raw/untrusted từ chúng vào artifact counts-only có thể commit.
- **Bằng chứng:** `validate_trace` trả raw `skill.name`/`sha256` kể cả khi invalid (`skill_trace.py:424-435`); `aggregate_command` dùng trực tiếp chúng làm JSON keys tại `466-490`. Fixture invalid đặt skill name `PRIVATE_MARKER_DO_NOT_EXPORT`; aggregate exit `0` và xuất marker hai lần trong `skills`/`skill_versions`, đồng thời tự ghi `privacy: counts-only; no summaries or refs`.
- **Hệ quả:** Trace local bị hỏng hoặc bị chỉnh có thể đưa secret, dữ liệu cá nhân hay payload tùy ý vào workflow artifact được commit, vượt ranh giới raw-local/aggregate-safe.
- **Điều kiện đóng:** Không dùng dimension từ trace invalid; gom chúng vào một count cố định như `invalid_count`/`unknown`, hoặc chỉ đưa các dimension đã validate và sanitize. Thêm test với invalid skill/hash/optional fields chứa marker và khẳng định marker không xuất hiện ở output hay stdout.

## STE-004 — `Major` — Báo cáo `6/6` vượt quá coverage của test đã khóa

- **Mệnh đề:** Mỗi scenario tại `trial-contract.md:11-16` phải có phép thử trực tiếp trước khi primary metric được ghi `Pass`.
- **Bằng chứng:** `test_event_types_and_second_terminal_are_rejected` ghi event nhưng không so sánh bytes/prefix trước-sau để chứng minh phần cũ không bị viết lại. `test_same_second_ids_are_unique` tại `test_skill_trace.py:84-89` gọi tuần tự dưới clock mock, không tạo concurrent processes/writers. Negative test tại `91-106` chỉ thử `../` và một outside directory, không thử absolute Windows path, UNC, symlink hoặc junction. Aggregate test tại `120-141` không assert refs và chỉ dùng trace hợp lệ. Không test nào áp dụng JSON schema đã commit. Tuy vậy `validation-report.md:5-26` tuyên bố toàn bộ sáu scenario và schema expansion đều đạt.
- **Hệ quả:** Comparison `0/6 → 6/6` và primary metric không tái hiện đúng contract; nó che các lỗi `STE-001` đến `STE-003`.
- **Điều kiện đóng:** Bổ sung test trực tiếp cho mọi vế của sáu scenario, gồm process concurrency/lock behavior, append prefix integrity, absolute/UNC/junction/symlink, official schema/lifecycle tampering, refs và trace invalid trong aggregate. Chỉ cập nhật report theo kết quả thực; nếu thu hẹp scenario/metric phải quay lại owner gate thay vì sửa sau kết quả.

## STE-005 — `Minor` — Lock append có thể bị stale vĩnh viễn

- **Mệnh đề:** Crash giữa tạo và xóa lock không được làm trace không thể đóng vô thời hạn mà thiếu đường phục hồi có kiểm soát.
- **Bằng chứng:** `skill_trace.py:176-198` tạo `.append.lock` bằng `O_EXCL`, nhưng lock không có owner/time metadata, retry, expiry hoặc documented recovery. Existing lock luôn trả `trace is currently locked by another writer`.
- **Hệ quả:** Process bị kill có thể để một trace mở nhưng không thể event/finish bằng CLI; sau 24 giờ validator chỉ đánh invalid mà không cung cấp phục hồi.
- **Điều kiện đóng:** Chọn OS-level lock hoặc stale-lock protocol có owner/timestamp và kiểm tra an toàn; tài liệu hóa recovery; thêm crash/stale-lock và concurrent writer tests.

## STE-006 — `Minor` — Tài liệu portable hứa phát hiện invocation thiếu mà implementation không thể quan sát

- **Mệnh đề:** Portable guidance phải giữ đúng giới hạn không có platform hook.
- **Bằng chứng:** `temp/generalizable-agent-harness-patterns.md:484` yêu cầu validator báo invocation thiếu; `iter_trace_dirs`/`validate_command` tại `skill_trace.py:438-448` chỉ biết directory đã tồn tại. Nguồn committed khác nói đúng rằng invocation bỏ qua contract không quan sát được. Tệp portable bị `temp/*` ignore dù impact map/implementation log ghi nó là output đã cập nhật.
- **Hệ quả:** Người áp dụng portable pattern có thể tin coverage gap tự được phát hiện; thay đổi portable cũng không tái dựng được từ evidence commit.
- **Điều kiện đóng:** Đổi claim thành audit chỉ phát hiện thiếu khi có expected-invocation roster độc lập; nếu không thì ghi coverage `Not verified`. Ghi rõ portable file là export local/ignored hoặc đưa artifact phiên bản hóa vào phạm vi được duyệt.

## STE-007 — `Minor` — Hồ sơ lượt chạy chưa tuân thủ trường Skill trace mới

- **Mệnh đề:** Trial dùng chính contract mới phải ghi `execution_id` và `trace_path` cho từng repository-local skill, hoặc `Not verified` có lý do.
- **Bằng chứng:** `agent-dispatch-protocol.md` thêm trường `Skill trace`; `AGENTS.md` yêu cầu đưa cả ID/path vào task contract và log. `orchestration-log.md` hiện không có cột này; ST-2 chỉ nhúng hai execution ID vào output và không ghi trace path. Raw workflow trace hiện vẫn open; điều này hợp lệ khi run đang diễn ra nhưng phải được đóng trước bàn giao cuối.
- **Hệ quả:** Evidence tự-host của trial không hoàn toàn tái dựng được theo contract mà candidate muốn ratify.
- **Điều kiện đóng:** Điều phối viên bổ sung trường riêng với ID/path hoặc limitation, đồng bộ candidate/evidence commit, và đóng workflow trace với outcome/output refs trước final handoff.

---

## Re-review disposition — corrective commit `956e742`

### STE-001 — `Reopened / Major`

Junction/reparse protections đạt các fixture mới, nhưng mệnh đề “mọi write bị giới hạn trong trace root” chưa đạt. Trên Windows, reviewer tạo hardlink từ trace `events.jsonl` tới một file ngoài fixture repository. `event` trả exit `0` và tăng file ngoài từ 111 lên 209 byte. `Path.is_symlink()`, `Path.is_junction()` và reparse attribute đều không nhận diện hardlink; code không kiểm `st_nlink` trước `open("ab")`.

**Điều kiện đóng bổ sung:** từ chối multi-link file write target hoặc dùng open/identity protocol bảo đảm handle thuộc file mới, riêng trong trace directory; test phải chứng minh hardlink target ngoài không đổi và recorder trả lỗi có kiểm soát.

### STE-002 — `Reopened / Major`

Validator đã sửa các mismatch từng được nêu, nhưng lifecycle vẫn chấp nhận `seq` sai kiểu. Fixture `"seq": true` được coi là valid vì Python so sánh `True == 1`; float `1.0` có cùng lớp rủi ro. Ngoài ra manifest schema tại `skill-trace.schema.json` vẫn chỉ dùng type cho nhiều trường trong khi validator áp pattern/format/slug/path constraints, nên một consumer dùng schema có thể chấp nhận manifest mà CLI từ chối.

**Điều kiện đóng bổ sung:** yêu cầu `seq` là integer dương và loại `bool`; đồng bộ schema với exact name/path/SHA/HEAD/timestamp/slug/ref constraints, hoặc xác định rõ schema nào là nguồn máy đọc đầy đủ và kiểm thử hai chiều schema ↔ validator.

### STE-003 — `Resolved`

Invalid traces bị loại trước khi aggregate đọc skill/version/event dimensions. Fixture marker không xuất marker ra artifact/stdout payload và vẫn đếm `invalid_count=1`.

### STE-004 — `Reopened / Major`

Coverage 13 test là cải thiện thực, nhưng claim `6/6` vẫn không đạt vì test không phát hiện hai lỗi Major ở `STE-001`/`STE-002`. Test append-prefix chỉ chứng minh terminal thứ hai bị từ chối không sửa file, chưa chứng minh successful append giữ nguyên prefix; không có concurrent-writer test hay official schema conformance test.

**Điều kiện đóng bổ sung:** thêm trực tiếp hardlink, `seq` bool/float, schema two-way, successful append-prefix và concurrent writer fixtures; validation report chỉ được ghi `6/6` sau khi các phép này đạt.

### STE-005 — `Unresolved / Minor`

PID/time metadata và guarded recovery hoạt động với metadata hợp lệ. Tuy nhiên empty/malformed stale lock — trạng thái có thể xuất hiện khi crash giữa `os.open` và `json.dump` — bị khóa vĩnh viễn vì parse failure luôn đặt `stale=False`. Concurrent writers bị từ chối tức thời; fixture 12 process chỉ lưu 3 note nhưng trace còn valid.

**Điều kiện đóng bổ sung:** có recovery an toàn cho malformed lock dựa trên file age/atomic lock metadata, hoặc dùng locking primitive không để lại trạng thái nửa ghi; test concurrent writers và tài liệu hóa rõ retry/single-writer semantics.

### STE-006 — `Resolved`

Portable export nay yêu cầu expected-invocation roster độc lập và dùng `Not verified` khi không có; disposition cũng ghi rõ file là local/ignored export.

### STE-007 — `Partially resolved / Minor`

Cột `Skill trace`, ID và path đã được thêm. Chưa có orchestration row cho corrective implementation/re-review; implementation log chưa ghi SHA `956e742`; raw workflow-orchestration trace còn open. Đây là công việc lifecycle trước final handoff, không phải bằng chứng `Pass` hiện tại.

**Điều kiện đóng bổ sung:** ghi work units/corrective SHA, đóng trace với output refs sau khi workflow thật sự kết thúc, rồi tái sinh/validate derived index.

---

## Final re-review — candidate `f416cc0`

### STE-001 — `Resolved`

Junction/reparse và hardlink/multi-link write targets đều bị từ chối trước write; open-handle link count là lớp kiểm tra thứ hai. Fixture độc lập xác nhận `event` exit `2` và hardlink target ngoài repo giữ nguyên bytes.

### STE-002 — `Unresolved / Major`

Validator và event schema nay loại `seq: true` và `seq: 1.0`. Phần schema parity còn sai:

- manifest schema nhận `ftp://example.com/x` như relative ref dù validator cấm scheme;
- manifest schema nhận `..\outside.md` vì traversal lookahead chỉ hiểu `/`;
- URL có credentials/query vẫn lọt qua nhánh relative-ref của `anyOf`;
- event schema chỉ kiểm ref là non-empty string nên nhận traversal, absolute path và URL bị cấm;
- slug `../run` khớp schema pattern nhưng bị `validate_slug` từ chối.

Các kết quả trên được tái hiện bằng chính `schema_accepts` helper của candidate: schema `true`, validator `false`. Do schema là shape máy đọc được công bố cho consumer, chênh lệch ở path/credentials không chỉ là semantic bổ sung vô hại.

**Điều kiện đóng:** phân biệt URL và repo-relative ref bằng schema không chồng lấp; chuẩn hóa hoặc cấm backslash/traversal/drive/UNC; cấm credentials/query/fragment; áp cùng ref definition cho event schema; cấm `..` slug segments. Test một matrix adversarial hai chiều schema ↔ validator.

### STE-003 — `Resolved`

Aggregate tiếp tục loại toàn bộ dimension từ trace invalid; marker privacy fixture đạt.

### STE-004 — `Unresolved / Major`

16 tests cải thiện coverage thực, nhưng `test_committed_schemas_accept_generated_data_and_reject_type_tampering` chỉ là smoke test generated data/type và bỏ qua adversarial ref/slug parity. `test_concurrent_writers_are_serialized_without_event_loss` chỉ chạy threads trong một process nên `_THREAD_LOCKS` che race file lock giữa processes. Vì `STE-002` và `STE-005` còn lỗi trực tiếp, claim `6/6` chưa đủ căn cứ.

**Điều kiện đóng:** thêm schema parity matrix và subprocess writer fixture trên Windows; report đúng kết quả của các phép này.

### STE-005 — `Unresolved / Major`

Stale malformed lock recovery đã đạt. Cross-process contention chưa an toàn trên Windows: waiter mở lock trong `read_json`; owner đồng thời chạy `lock.unlink()` và có thể nhận `WinError 32`. Fixture 4 process cho kết quả hai success sạch, một process đã ghi note nhưng exit lỗi, một process còn chờ, lock mồ côi còn giữ PID process lỗi và tổng cộng ba note đã commit.

Hậu quả là CLI outcome không còn tương ứng với event commit: retry sau error có thể tạo duplicate, trong khi writer khác timeout cho tới khi lock đủ stale. Đây là lỗi correctness/lifecycle và trái tài liệu chờ 30 giây cùng claim không mất event.

**Điều kiện đóng:** dùng lock protocol không yêu cầu owner xóa file khi waiter đang giữ read handle, hoặc retry unlink an toàn và chứng minh ownership/token trước xóa. Subprocess test phải assert N command success tương ứng đúng N events, không orphan lock và trace valid qua nhiều vòng.

### STE-006 — `Resolved`

Không có hồi quy trong no-platform-hook/expected-roster limitation.

### STE-007 — `Pending final handoff`

Đây không còn là implementation finding: orchestration đã ghi các corrective work unit và trace refs. Sau một reviewer `Pass`, Điều phối viên vẫn phải ghi SHA candidate/final review, đóng workflow trace, tái sinh index, chạy `validate_index.py`/`sync_index.py --check`, rồi mới trình ratification. Trạng thái open/stale hiện tại được kỳ vọng trong khi review chưa kết thúc.

---

## Re-review — candidate `20ab1c9`

### STE-001 — `Resolved`

Không có hồi quy hardlink/junction/reparse/path-containment. Toàn bộ 17 test đạt, bao gồm hardlink ngoài repo không đổi và hai Windows junction fixtures.

### STE-002 — `Unresolved / Major`

Candidate đã sửa đúng các case được nêu gần nhất: manifest/event schemas và validator đều từ chối `ftp://example.com/x`, `..\\outside.md`, URL có credentials/query, `../outside.md` trong event và slug `../run`; `seq` bool/float vẫn bị từ chối.

Nhưng machine-readable schema và validator vẫn không tương đương hai chiều:

- `start --input-ref "https://example.com/a b"` và `event --ref "https://example.com/c d"` được recorder chấp nhận và lưu nguyên. `validate_trace` trả `valid: true`, trong khi chính `schema_accepts` helper của candidate trả `false` cho manifest và event tương ứng vì schema cấm whitespace.
- Manifest tampered với stored ref `docs\\file.md` được validator nhận vì `normalize_ref` chuẩn hóa nhưng validator không so giá trị canonical trở lại; manifest schema từ chối backslash.
- Manifest/started event dùng timezone tương đương `+00:00` được `parse_timestamp` nhận và lifecycle vẫn hợp lệ, trong khi schema chỉ nhận dạng `...Z` chính xác.

Trường hợp đầu tiên không chỉ là tampering: CLI hiện có thể tự sinh trace vi phạm schema được commit nhưng validator gọi hợp lệ. Điều này trái trial metric “schema/lifecycle validation” và README mô tả hai schema là shape máy đọc được.

**Điều kiện đóng:** dùng cùng grammar/canonicalization ở recorder, validator và schemas; hoặc validator phải từ chối artifact không canonical mà schema từ chối. Thêm matrix hai chiều, gồm mọi input CLI chấp nhận và timestamp/ref artifacts mà validator nhận.

### STE-003 — `Resolved`

Không có hồi quy privacy/aggregate. Invalid trace không cung cấp dimension; summary/ref không xuất vào aggregate; raw traces vẫn ignored và excluded khỏi derived index.

### STE-004 — `Unresolved / Major`

Subprocess concurrency coverage nay là process thật và đã tái hiện độc lập ở tải cao. Matrix test mới cũng khóa đúng các unsafe ref/slug đã biết. Tuy nhiên `test_committed_schemas_accept_generated_data_and_reject_type_tampering` vẫn là kiểm tra một chiều đối với ref: nó chỉ khẳng định schema từ chối bốn bad inputs, không khẳng định schema và validator nhận cùng tập artifacts.

Fixture CLI-generated URL có khoảng trắng cho thấy một completed trace có thể được validator tính valid nhưng vi phạm schema. Vì fixed comparison vẫn báo `6/6` và `100% completed fixture trace validity`, coverage chưa đủ để hỗ trợ claim khi `STE-002` còn tái hiện trực tiếp.

**Điều kiện đóng:** thêm two-way/property matrix hoặc một tập parity fixture đầy đủ cho refs/timestamps/canonicalization; report chỉ giữ `6/6` sau khi trace do mọi accepted CLI path sinh ra đạt cả schemas và lifecycle validator.

### STE-005 — `Resolved` cho implementation hiện tại; `Minor` migration follow-up

Lock-directory loại bỏ race Windows cũ. Tám vòng độc lập, mỗi vòng 24 subprocess cùng ghi một trace, đều có 24/24 command success, đúng 24 summary duy nhất, sequence `1..25`, không orphan `.append.lock` và validator hợp lệ. Các stale directory empty, owner empty/malformed, dead owner và extra regular metadata đều được thu hồi. Hai lượt 12 subprocess đồng thời tranh thu hồi empty/malformed stale directory cũng đạt exactly-once và không để lock.

Một hạn chế migration còn lại: nếu candidate `f416cc0` bị crash và để `.append.lock` dạng **file**, `20ab1c9` xem path tồn tại nhưng `release_lock` gọi `iterdir()`, gây `NotADirectoryError [WinError 267]`; lock cũ tồn tại và append không tiến hành. Đây là edge của chuyển đổi giữa hai candidate trial, không phải race/event-loss hiện hành, nên xếp `Minor`.

**Điều kiện follow-up:** nhận diện stale legacy lock-file và thu hồi theo protocol cũ một cách an toàn, hoặc ghi rõ trial migration/cleanup có kiểm soát trước ratification.

### STE-006 — `Resolved`

Không có hồi quy no-platform-hook limitation, expected roster hay trạng thái portable export local/ignored.

### STE-007 — `Pending final handoff`

Không phải implementation finding. Candidate SHA, final reviewer row, workflow trace closure và index regeneration phải thực hiện sau khi không còn Blocker/Major. Index stale và trace open trong lượt review này là trạng thái vòng đời dự kiến, không được dùng để che hay khuếch đại verdict code.

---

## Targeted final re-review — candidate `053df34`

### STE-001 — `Resolved`

Không có hồi quy hardlink, junction, reparse hay containment. Suite 17/17 đạt trên Windows.

### STE-002 — `Unresolved / Major`

Candidate đã đóng các counterexample gần nhất: HTTP/local whitespace, local và traversal backslash, FTP/custom schemes, credentials/query/fragment, parent ref, slug traversal, `+00:00`, fractional/offset/lowercase-z timestamps đều có kết quả schema/validator giống nhau. Một completed trace canonical do recorder sinh đạt manifest schema, mọi event schema và lifecycle validator.

Ma trận hai chiều mở rộng vẫn tìm thấy chênh lệch trực tiếp:

- `https://example.com\\evil`: URL branch của cả hai schemas cho phép backslash trong host character class, trong khi `normalize_ref` cấm mọi backslash. Kết quả schema `true`, validator manifest/event `false`.
- `HTTP://example.com/a` và `HtTpS://example.com/a`: `urlsplit` chuẩn hóa scheme để validator chấp nhận, nhưng schema regex chỉ nhận lowercase. Một completed trace do chính CLI tạo với hai refs này trả validator `valid: true`; manifest và event tương ứng trả schema `false`.
- `parent_workflow_run` có leading/trailing whitespace được `validate_slug` strip rồi chấp nhận, nhưng schema từ chối. Validator không kiểm stored value là canonical.
- Timestamp có hình thức đúng pattern nhưng ngày/giờ bất khả thi (`2026-13-25T...`, `2026-02-30T...`, giờ `25:62:63`) được `schema_accepts` helper dùng trong suite nhận vì helper bỏ qua `format`, trong khi validator từ chối. Với JSON Schema 2020-12, `format` cũng không mặc định là assertion bắt buộc cho mọi consumer, nên pattern hiện tại chưa tự bảo đảm calendar validity.

Do đã có artifact được CLI tạo mà validator gọi valid nhưng committed schema từ chối, đây vẫn là bất đồng machine contract thực, không chỉ semantic lifecycle bổ sung.

**Điều kiện đóng:** dùng chung case/backslash/canonical grammar cho URLs và slugs; dùng schema validation có format assertion hoặc pattern/logic tương đương rồi test cả hai chiều trên artifact hoàn chỉnh.

### STE-003 — `Resolved`

Không có hồi quy privacy. Aggregate tests đạt; raw trace vẫn nested-ignore và excluded khỏi derived index. Secret scan chỉ khớp token giả trong negative fixture.

### STE-004 — `Unresolved / Major`

Test hiện tại đã tốt hơn vì ghi bad ref vào manifest/event rồi assert cả schema lẫn validator từ chối. Tuy nhiên tập test chưa có URL backslash, uppercase/mixed-case HTTP scheme, slug whitespace hoặc calendar-invalid canonical-looking timestamps. Chính các khoảng trống đó tạo counterexample ở `STE-002`, trong đó có completed artifact do CLI sinh.

Vì primary metric yêu cầu mọi completed fixture trace đạt schema/lifecycle validation, `6/6` và `100%` chưa được chứng minh. Đây vẫn là evidence/coverage overclaim, không phải chỉ yêu cầu tăng test tùy chọn.

**Điều kiện đóng:** thêm các counterexample vào matrix hai chiều và assert mọi CLI-accepted input tạo artifact được cả schemas lẫn validator nhận; chỉ sau đó mới giữ comparison `0/6 → 6/6`.

### STE-005 — `Resolved`

Migration lock-file cũ đạt đầy đủ trong fixture độc lập:

- stale legacy file với dead-valid, empty hoặc malformed metadata đều được xóa và thay bằng lock-directory; append giữ prefix, thêm đúng một event, xóa lock và trace valid;
- legacy file cũ nhưng PID còn sống không bị thu hồi;
- hardlinked legacy lock bị từ chối, không xóa/mutate outside target;
- 8 vòng × 24 Windows subprocess cùng append tiếp tục đạt 192/192 command success, 192 summary duy nhất, sequence liên tục, không lock mồ côi và 8/8 trace valid.

Không còn Blocker/Major ở lifecycle/concurrency hiện hành hay migration case được yêu cầu.

### Minor adjunct — malformed URL error path

`normalize_ref("http://[bad", root)` và biến thể IPv6 bracket dở dang làm `urlsplit` ném raw `ValueError`; CLI chỉ bắt `TraceError`, nên người dùng nhận traceback thay vì JSON error có kiểm soát. Không có trace/write được tạo trước lỗi ở `start`, do đó xếp `Minor`.

### STE-006 — `Resolved`

No-platform-hook và expected-roster limitation không hồi quy.

### STE-007 — `Pending final handoff`

Không phải implementation finding. Chỉ sau khi mọi Blocker/Major đóng mới ghi final candidate/reviewer SHA, đóng workflow trace, tái sinh index và chạy hai index gates. Trạng thái stale/open hiện tại không ảnh hưởng phân loại code ở trên.
