# Skill execution tracing

`skill_trace.py` tạo bằng chứng local, máy đọc được cho mỗi repository-local skill invocation. Cơ chế này dựa trên hợp đồng trong `AGENTS.md`; nó không phải platform hook và không quan sát được invocation nếu tác nhân bỏ qua hợp đồng.

## Vòng đời

```powershell
python .agents/execution-tracing/skill_trace.py start `
  --skill lesson-authoring `
  --summary "Revise one approved lesson" `
  --input-ref ai-native-builder/goals/g01-example/README.md

python .agents/execution-tracing/skill_trace.py event `
  --trace .agent-execution-runs/<execution-id> `
  --type check `
  --summary "Required source files were read"

python .agents/execution-tracing/skill_trace.py finish `
  --trace .agent-execution-runs/<execution-id> `
  --outcome completed `
  --summary "Lesson revision and scoped checks completed" `
  --output-ref ai-native-builder/goals/g01-example/lesson.md
```

Lệnh `start` in JSON ra `execution_id` và `trace_path`; giữ giá trị này trong ngữ cảnh làm việc hoặc task contract. Dùng `event` chỉ cho `artifact`, `check`, `correction`, `retry`, `limitation` hoặc `note`. `finish` chỉ chạy một lần với `completed`, `failed`, `cancelled` hoặc `not-verified`.

## Kiểm định và aggregate

```powershell
python .agents/execution-tracing/skill_trace.py validate --all
python .agents/execution-tracing/skill_trace.py aggregate `
  --output .agents/workflow-runs/<run-id>/skill-trace-aggregate.json
```

`validate --all` cho phép trace đang mở dưới 24 giờ nhưng trả lỗi với trace hỏng hoặc mở quá hạn. `aggregate` không xuất summary hay refs; output chỉ gồm counts theo skill, outcome, correction/retry và số trace invalid/open/expired.

Recorder từ chối symlink, junction, reparse point và multi-link write target ở runtime root, trace directory và file được ghi. Append chờ tối đa 30 giây khi cạnh tranh và dùng atomic lock-directory có PID/thời điểm; contender không mở metadata của lock đang hoạt động. Lock quá 5 phút chỉ được thu hồi khi tiến trình sở hữu không còn tồn tại, hoặc khi metadata hỏng và chính lock-directory đã quá 5 phút. `skill-trace.schema.json` và `skill-event.schema.json` công bố hai shape máy đọc; validator còn thực thi các bất biến quan hệ và lifecycle. Trace invalid chỉ đóng góp vào `invalid_count`, không cung cấp dimension cho aggregate.

## Giới hạn dữ liệu

- Summary tối đa 500 ký tự, được chuẩn hóa thành một dòng và bị chặn khi giống secret phổ biến.
- Ref chỉ là path tương đối dùng dấu `/` hoặc URL HTTP(S) không có credentials, query, fragment hay khoảng trắng; recorder và validator chỉ chấp nhận dạng canonical mà schema công bố.
- Recorder không đọc nội dung của ref, không thu environment và không có field cho raw prompt hoặc reasoning.
- `skill_sha256` ghi đúng phiên bản instruction đã dùng; thay đổi skill sau đó không viết lại trace cũ.
