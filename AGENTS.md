# Hướng dẫn cho tác nhân AI

## Mục đích và phạm vi

Kho dự án này xây dựng giáo trình AI-native Builder cho người mới bắt đầu xây dựng sản phẩm cùng AI. Hãy giữ ranh giới giữa kế hoạch, kiến trúc giáo trình, bài học, lộ trình học, hồ sơ dạy thử và hồ sơ vận hành.

`AGENTS.md` là hợp đồng vận hành tóm tắt, không thay thế các quy tắc chuyên môn trong `.agents/rules/`.

## Thứ tự đọc bắt buộc

Trước khi tạo, sửa, kiểm định hoặc sắp xếp nội dung:

1. Đọc `README.md` để hiểu bản đồ kho dự án.
2. Đọc [đầu mối quy tắc](.agents/rules/README.md), sau đó đọc các quy tắc mà loại công việc yêu cầu.
3. Đọc nguồn chuẩn liên quan và tệp `README.md` của phạm vi đang thay đổi.
4. Đọc kỹ năng hoặc quy trình được chọn trước khi thực hiện.

## Nguồn chuẩn và quyền sở hữu

- Phân cấp nguồn chuẩn, ranh giới giữa kiến trúc và bản đồ giáo trình, cùng quy ước ngôn ngữ nằm trong [`curriculum-contract.md`](.agents/rules/curriculum-contract.md).
- Bản định hướng `README.md` trong `ai-native-builder/goals/gNN-*` là nguồn thiết kế của mục tiêu đó; các tệp còn lại là phần triển khai.
- `runs/` chỉ ghép và điều phối bài học chuẩn, không sao chép nội dung bài học.
- `.agents/workflow-runs/` là hồ sơ vận hành workflow; `.agent-execution-runs/` là raw trace local của skill; `.agents/decisions/` là hồ sơ quyết định. Các hồ sơ này không thay thế nguồn chuẩn.
- Không tạo nguồn thứ hai cho cùng một quyết định, không bàn giao bằng trí nhớ hội thoại, và tôn trọng quyền sở hữu tệp do quy trình quy định.

## Chọn đường thực hiện

- Với công việc chuyên biệt, phạm vi hẹp: chọn kỹ năng phù hợp trong `.agents/skills/`.
- Với công việc nhiều giai đoạn, vai trò, nhánh quyết định hoặc bàn giao: đọc [danh mục quy trình](.agents/workflows/README.md), rồi dùng `$workflow-orchestration` để thực thi quy trình được chọn.
- Chỉ thực thi quy trình `Active`, trừ khi người dùng đã cho phép chạy thử có kiểm soát quy trình `Proposed`. Không thực thi quy trình `Placeholder`.
- Vai trò trong quy trình không mặc định tương đương một tác nhân riêng. Khi điều phối, tuân theo [`agent-dispatch-protocol.md`](.agents/workflows/agent-dispatch-protocol.md) và lưu bằng chứng phân công trong lượt chạy.
- Lời gọi tường minh `$skill-name` là chỉ dẫn ưu tiên để chọn kỹ năng, nhưng không mở rộng phạm vi hay bỏ qua quy tắc. Khi không có lời gọi tường minh, chọn kỹ năng theo `description` nếu phù hợp.

## Ghi vết thực thi kỹ năng

Khi dùng một repository-local skill trong `.agents/skills/`:

1. Trước hành động chuyên môn đầu tiên, chạy `python .agents/execution-tracing/skill_trace.py start` với tên skill, tóm tắt đã khử nhạy cảm và các input ref cần thiết.
2. Giữ `execution_id` và `trace_path` do lệnh trả về. Trong workflow, đưa chúng vào task contract và `orchestration-log.md`.
3. Chỉ ghi các event có giá trị kiểm định như `artifact`, `check`, `correction`, `retry` hoặc `limitation`; không biến trace thành nhật ký hội thoại.
4. Trước bàn giao cuối, chạy `finish` với outcome và output refs. Không để trace mở chỉ vì công việc thất bại; dùng `failed`, `cancelled` hoặc `not-verified` phù hợp.
5. Không ghi raw prompt, chain-of-thought, secret, dữ liệu cá nhân, environment dump hoặc toàn bộ tool response. Raw trace ở `.agent-execution-runs/` là local/ignored và mặc định giữ 30 ngày.
6. Nếu recorder không khả dụng hoặc không ghi được, không tạo bằng chứng giả. Ghi `Skill trace: Not verified` trong bàn giao; workflow phải phản ánh giới hạn này trong hồ sơ lượt chạy.

Lệnh, schema, validator và cách xuất aggregate counts-only nằm trong [`.agents/execution-tracing/README.md`](.agents/execution-tracing/README.md). Đây là hợp đồng do tác nhân thực thi, không phải platform hook; audit phải coi invocation không có trace là khoảng trống bằng chứng.

## Bất biến khi làm việc

- Khi bất đồng có thể đổi kết quả, dừng phần phụ thuộc, trình bày các mệnh đề xung đột, kiểm chứng cả bằng chứng ủng hộ lẫn phản bác, rồi mới tiếp tục sau khi đã có kết luận hoặc quyết định của người dùng. Xem `.agents/rules/README.md`.
- Không tự nâng trạng thái chất lượng. Mọi cổng, điểm và trạng thái phải có bằng chứng theo [`quality-gates.md`](.agents/rules/quality-gates.md); người tạo không được là bên duy nhất chấp nhận phần mình tạo.
- Chỉ sửa tầng kiến trúc khi phát hiện thực sự ảnh hưởng ranh giới mục tiêu, quan hệ phụ thuộc hoặc cam kết chương trình; thay đổi cục bộ ở bài học phải ở đúng tầng sở hữu.
- Với dữ liệu, công cụ, API, quyền hạn hoặc thông tin biến động theo thời gian, áp dụng [`safety-and-currency.md`](.agents/rules/safety-and-currency.md) và kiểm chứng nguồn phù hợp.
- Viết văn xuôi tiếng Việt tự nhiên. Giữ tiếng Anh cho tên tệp, đường dẫn, mã định danh, lệnh, tên kỹ năng/quy trình và nội dung bên trong khối kỹ thuật; không trộn hai ngôn ngữ trong cùng một khối kỹ thuật.

## Thay đổi và kiểm chứng

- Dùng bản vá có phạm vi hẹp; bảo toàn các thay đổi ngoài phạm vi yêu cầu.
- Sau thay đổi, chạy phép kiểm tra phù hợp với rủi ro và ghi rõ bằng chứng hay giới hạn còn lại.
- Thay đổi `.agents/rules/` là thay đổi quản trị: ghi hồ sơ trong `.agents/decisions/`, xác định phạm vi ảnh hưởng và có kiểm định quản trị độc lập trước khi coi là chuẩn.
- Chỉ tạo `AGENTS.md` lồng nhau khi thư mục có chỉ dẫn vận hành khác biệt thực sự; đặt nó sát phạm vi áp dụng và không lặp lại luật toàn cục.

## Tài liệu chi tiết

- Quy tắc và thuật ngữ: [`.agents/rules/README.md`](.agents/rules/README.md)
- Danh mục và vòng đời quy trình: [`.agents/workflows/README.md`](.agents/workflows/README.md)
- Kỹ năng cục bộ: [`.agents/skills/`](.agents/skills/)
- Bản đồ giáo trình: [`ai-native-builder/curriculum-map.md`](ai-native-builder/curriculum-map.md)
