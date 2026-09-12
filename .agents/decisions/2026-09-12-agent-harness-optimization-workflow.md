# Thêm khung quy trình tối ưu hệ thống harness tác nhân

- Ngày: 2026-09-12
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu kho
- Phạm vi ảnh hưởng: `.agents/workflows/optimize-agent-harness-system.md`, các danh mục quy trình và định tuyến cải tiến rules/skills/workflows/harness trong tương lai
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Kho đã có quy tắc quản trị, kỹ năng tạo kỹ năng và tiêu chí chuyển trạng thái workflow, nhưng chưa có một điểm định tuyến chung cho việc cải tiến chính hệ thống hướng dẫn, điều phối và kiểm chứng tác nhân. Nếu thay đổi trực tiếp từng tệp mà không có khung chung, bằng chứng vận hành, phạm vi ảnh hưởng và điều kiện hoàn tác dễ bị phân tán.

Ngược lại, một workflow đầy đủ ngay bây giờ sẽ đưa ra các bước thực thi khi chưa có dữ liệu chạy thử, chủ sở hữu cổng quyết định và thiết kế kiểm định phù hợp.

## Các phương án đã cân nhắc

1. Không thêm workflow, tiếp tục xử lý từng thay đổi harness như thay đổi cục bộ.
2. Thêm ngay workflow `Active` để tự động tối ưu harness.
3. Thêm một khung `Placeholder`, xác định ranh giới, bằng chứng và các câu hỏi thiết kế trước khi có quyền chạy thử.

## Bằng chứng thuận và nghịch

Các workflow hiện tại đã tách nguồn chuẩn, hồ sơ vận hành, quyết định quản trị và kiểm định độc lập. Khung mới giúp áp dụng cùng nguyên tắc này cho chính harness.

Tuy nhiên chưa có một lượt thử có kiểm soát nào chứng minh chuỗi tối ưu harness, cơ chế đo đường cơ sở, rollback hay cổng chấp thuận. Vì vậy chưa có bằng chứng để coi nó là `Proposed` hoặc `Active`.

## Quyết định

Thêm `optimize-agent-harness-system` ở trạng thái `Placeholder`. Nó chỉ định tuyến và định khung việc thiết kế cải tiến `AGENTS.md`, rules, skills, workflows, giao thức điều phối và tài sản vận hành liên quan. Nó không được thực thi và không cho phép tự thay đổi nguồn chuẩn.

## Hệ quả và phạm vi chuyển đổi

Danh mục quy trình và điểm vào ở README được cập nhật để tránh tài liệu mồ côi. Các thay đổi harness cụ thể tiếp tục phải tuân theo chủ sở hữu tệp và quy tắc quản trị hiện có; thay đổi nội dung hay kiến trúc giáo trình không thuộc quy trình này.

## Điều kiện xem xét lại

Chỉ xem xét nâng lên `Proposed` sau khi chốt được tiêu chí khởi động/dừng, nguồn bằng chứng runtime, quyền riêng tư, mô hình chạy thử và rollback, chủ sở hữu quyết định, kiểm định quản trị độc lập và kế hoạch di trú cho thay đổi đa tầng.
