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
