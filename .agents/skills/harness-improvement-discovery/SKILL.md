---
name: harness-improvement-discovery
description: Discover evidence-backed weaknesses and improvement opportunities in an agent harness by examining workflow runs, skill traces, decisions, rules, skills, workflows, and related operational evidence. Use for broad or open-ended harness audits when the problem or solution is not yet known; do not edit the harness, validate a chosen intervention, or replace the controlled validation workflow.
---

# Khám phá cải tiến harness

Tìm vấn đề mà metric hoặc người đọc run riêng lẻ có thể bỏ sót, nhưng không ép bằng chứng thành một kết luận giả tạo. Giữ hướng dẫn này ở mức tự do cao để mô hình có thể dùng phán đoán theo ngữ cảnh.

## Khóa phạm vi

1. Ghi câu hỏi rà soát, phạm vi thời gian, loại bằng chứng được phép đọc, giới hạn thời gian/token và dữ liệu cấm.
2. Đọc nguồn chuẩn hiện hành trước khi diễn giải run. Run và decision record là bằng chứng vận hành/lịch sử, không tự là nguồn chuẩn.
3. Khi phạm vi rộng, lấy mẫu có chủ đích gồm run thành công, run thất bại hoặc `Not verified`, run có sửa/re-review và một mẫu ngẫu nhiên. Nêu rõ phần không được quan sát.
4. Đọc raw trace local trong `.agent-execution-runs/` và aggregate đã xuất trong workflow runs khi chúng thuộc phạm vi được phép. Dùng validator trước khi diễn giải; không suy ra hiệu quả từ trace hỏng, mở quá hạn hoặc thiếu invocation.
5. Nếu repo không có trace cho một skill/phạm vi, ghi đây là giới hạn dữ liệu thay vì dùng workflow run làm đại diện. Hợp đồng dựa trên tác nhân không chứng minh coverage tuyệt đối khi host chưa có platform hook.

## Khám phá

- Tìm sai lệch giữa mục tiêu và hành vi, đường vòng, lần sửa lặp lại, finding bị rút hoặc tranh chấp, cổng không tạo giá trị, chi phí điều phối, vùng thiếu bằng chứng và thành công có thể che giấu lỗi thiết kế.
- Với skill traces, so sánh theo `skill_sha256`, outcome, correction/retry/check counts và trace coverage; không đọc request/event summary nếu aggregate counts-only đã đủ cho câu hỏi.
- So sánh các run tương phản thay vì chỉ đếm lỗi. Kiểm tra cả bằng chứng ủng hộ lẫn phản bác cho mỗi diễn giải.
- Phân biệt `Observed`, `Inferred`, `Missing` và `Out of scope`.
- Giữ nhiều giải thích cạnh tranh khi bằng chứng chưa phân biệt được chúng. Không dùng độ tự tin của mô hình thay cho bằng chứng.
- Có thể kết luận không có candidate đủ mạnh; không bắt buộc đề xuất thay đổi.

## Lập báo cáo

Trả một `discovery report` gồm:

1. phạm vi, cách lấy mẫu và bằng chứng đã đọc;
2. giới hạn quan sát và loại dấu vết còn thiếu;
3. các quan sát chưa đủ để hành động;
4. không, một hoặc nhiều `candidate issue` độc lập;
5. vùng đã rà soát nhưng không phát hiện vấn đề đáng kể.

Mỗi candidate dùng nguyên schema sau để có thể bàn giao trực tiếp cho `validate-agent-harness-improvement`:

```text
Candidate ID: <stable local id>
Problem statement: <testable claim; one root issue>
Expected behavior: <observable expectation>
Observed behavior: <observable divergence>
Evidence refs: <run/file/section references>
Counterevidence: <contradicting or limiting evidence>
Trigger: <repeated issue | high/critical incident | environment change | metric threshold | owner-nominated hypothesis>
Suspected scope: <files/components; hypothesis, not verdict>
Initial impact: <Low | Medium | High | Critical, with rationale>
Forbidden data: <data that validation must not collect>
Decision owner: <person/role with trial and ratification authority>
Confidence: <Low | Medium | High, with reason>
Competing explanations: <credible alternatives>
Recommended next step: <No action | Observe | Deterministic repair | Validate candidate>
Validation readiness: <Ready | Not ready, with missing fields/evidence>
```

Đánh dấu `Ready` chỉ khi candidate có mệnh đề kiểm tra được, kỳ vọng/quan sát phân biệt được, dẫn chứng truy cập được, đúng một vấn đề gốc và có trigger hợp lệ. Không gộp nhiều candidate vào một lượt validation.

## Ranh giới và bàn giao

- Không sửa rules, skills, workflows, schema hoặc nguồn chuẩn trong lượt khám phá.
- Không tự mở `validate-agent-harness-improvement`; Chủ sở hữu chọn candidate và cho phép trial.
- Không gọi một sửa lỗi cơ học là trial nếu không còn bất định cần kiểm chứng; bàn giao cho chủ sở hữu tệp cùng phép kiểm tra hẹp.
- Nếu phát hiện rủi ro `High`/`Critical` đang hoạt động, dừng phân tích phụ thuộc, báo Chủ sở hữu và bàn giao candidate cho nhánh `Incident containment` của workflow.
- Nếu bằng chứng nhạy cảm, chỉ lưu dẫn chiếu và bản tóm tắt đã khử nhạy cảm; không sao chép secret, dữ liệu cá nhân hoặc hội thoại dài vào báo cáo.
