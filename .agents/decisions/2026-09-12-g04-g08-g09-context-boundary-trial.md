# Chạy thử phân bổ lại năng lực quản lý tri thức giữa G04, G08 và G09

- Ngày: 2026-09-12
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình
- Phạm vi ảnh hưởng: `AI-native-builder-curriculum-plan.md`, `curriculum-content-architecture.md`, bản định hướng G04/G08/G09 và lượt chạy `20260912-2149-change-curriculum-context-rebalance`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Tuần 5 đang dùng cụm “xây cơ sở tri thức”, trong khi G04 đã có các thành phần nền như workspace, nguồn chuẩn, nhật ký quyết định và kiểm thử phiên mới. Nếu dạy toàn bộ kiến trúc tri thức ở Tuần 5, người học có thể dựng nền quá muộn; nếu đưa toàn bộ truy xuất nâng cao lên Tuần 2, tải nhận thức sẽ tăng và thiếu dữ liệu dự án để kiểm thử.

## Các phương án đã cân nhắc

1. Giữ nguyên phân bổ hiện tại.
2. Đưa toàn bộ G08 lên sớm.
3. Gieo nền tri thức tối thiểu ở G04/Tuần 2, giữ quản lý/truy xuất nâng cao ở G08/Tuần 5 và chỉ mã hóa cải tiến có bằng chứng ở G09/Tuần 6.

## Bằng chứng thuận và nghịch

G04 đã yêu cầu nguồn chuẩn, decision log và phiên tác nhân mới; G08 yêu cầu dự án có nhiều tệp/quyết định; G09 yêu cầu bằng chứng lặp lại trước khi tạo cơ chế tái sử dụng. Đây là bằng chứng thuận cho phương án phân lớp. Chưa có bằng chứng dạy thử trên người học, nên thay đổi này chỉ được coi là chạy thử kiến trúc và chưa chứng minh hiệu quả sư phạm.

## Quyết định

Cho phép chạy thử có kiểm soát `change-curriculum-architecture` ở trạng thái tạm thời `Active` để áp dụng phương án 3 trong phạm vi khóa. Không thêm goal, không đổi mã/thứ tự goal và không xây RAG/graph. Kiểm định độc lập sau áp dụng sẽ quyết định giữ, sửa hoặc hoàn tác.

## Hệ quả và phạm vi chuyển đổi

Năm tệp nguồn chuẩn được cập nhật theo bản đồ ảnh hưởng trong hồ sơ lượt chạy; các tệp trạng thái và hồ sơ vận hành được cập nhật riêng. `curriculum-map.md` giữ nguyên. Các lesson package chưa tồn tại nên chưa cần viết lại; khi soạn G04/G08/G09, workflow `complete-goal-lessons` phải dùng hợp đồng mới.

Trạng thái `Active` của workflow chỉ có hiệu lực trong lượt chạy này. Sau khi bàn giao, workflow đã được trả về `Proposed`; muốn duy trì `Active` phải có một quyết định mới dựa trên bằng chứng chạy thử và kiểm định đầy đủ.

## Điều kiện xem xét lại

Kiểm định độc lập thất bại, phát hiện bước nhảy năng lực, xung đột nguồn chuẩn, ảnh hưởng ngoài danh sách tệp hoặc bằng chứng dạy thử sau này cho thấy phân lớp này không khả thi.
