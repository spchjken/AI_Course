# Thiết kế quy trình làm mới nội dung dễ lỗi thời

- Ngày: 2026-09-06
- Trạng thái: Đề xuất — chờ duyệt
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: `.agents/workflows/refresh-volatile-content.md`, `.agents/workflows/scripts/scan_volatile_claims.py`, `.agents/workflows/README.md`, `.agents/workflows/complete-goal-lessons.md`, `.agents/rules/curriculum-contract.md`
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Khẳng định phụ thuộc công cụ và nguồn ngoài cần được kiểm tra lại, nhưng một danh mục trung tâm sẽ lặp lại phán quyết đang thuộc `references.md` gần nội dung sử dụng. Tệp giữ chỗ cũ cũng chưa phân biệt việc làm mới bằng chứng với việc sửa nội dung phụ thuộc, khiến tác nhân có thể tự thay công cụ hoặc thay bài học chỉ vì một nguồn mới hơn.

## Các phương án đã cân nhắc

1. Tạo một sổ khẳng định trung tâm cho toàn kho.
2. Chỉ để từng `references.md` tự quản lý mà không có cách quét lặp lại.
3. Giữ `references.md` là nguồn sở hữu cục bộ, dùng bộ quét chỉ đọc tạo hàng đợi dẫn xuất theo từng lượt bảo trì và định tuyến mọi sửa đổi nội dung về quy trình sở hữu.

## Bằng chứng thuận và nghịch

- Khẳng định chỉ có nghĩa trong vị trí, phiên bản và hoạt động cụ thể đang dùng nó; một sổ trung tâm dễ mất liên hệ này và tạo dữ liệu trùng.
- Không có hàng đợi dẫn xuất thì bảo trì toàn kho phụ thuộc vào trí nhớ, khó lặp lại và khó giao cho tác nhân nhẹ.
- Nguồn chính thức có thể làm rõ dữ kiện nhưng không tự chọn ưu tiên sư phạm, chi phí, quyền hạn hay công cụ phù hợp.
- Khẳng định an toàn, dữ liệu, quyền hạn hoặc chi phí cần được ưu tiên và có thể cần chặn sử dụng trước khi lời giải thay thế hoàn thiện.

## Quyết định

- Đưa `refresh-volatile-content` lên trạng thái `Proposed` với hai chế độ: làm mới có mục tiêu và rà soát trước phát hành.
- Dùng hai bảng trong mỗi `references.md`: sổ khẳng định và sổ bằng chứng, với độ cập nhật cần thiết, mức rủi ro, phiên bản/phạm vi và điều kiện kiểm tra lại.
- Tạo `scan_volatile_claims.py` chỉ đọc, không truy cập mạng, để phát hiện sổ, kiểm tra siêu dữ liệu và tạo hàng đợi dẫn xuất.
- Quy trình chỉ cập nhật `references.md`, hàng đợi dẫn xuất và hồ sơ quyết định phù hợp. Mọi sửa đổi nội dung được bàn giao về quy trình sở hữu.
- Dùng cờ `Block use` cho khẳng định an toàn hoặc trọng yếu chưa đủ căn cứ; cờ này là biện pháp phòng ngừa, không phải phán quyết toàn bộ giáo trình thất bại.

## Hệ quả và phạm vi chuyển đổi

- Các `references.md` mới phải dùng hai bảng chuẩn. Hiện chưa có `references.md` thực tế, nên chưa cần chuyển đổi dữ liệu cũ.
- `complete-goal-lessons` được cập nhật để tác nhân nhẹ tạo sổ khẳng định phù hợp với quét tự động.
- Rà soát trước phát hành có thể tạo hàng đợi nhưng không được biến thành tìm kiếm hay cập nhật hàng loạt không có phạm vi.
- Phán quyết đổi hoặc có ảnh hưởng cao cần kiểm định độc lập; lựa chọn sản phẩm và thay đổi cấu trúc vẫn thuộc cổng quyết định của con người.

## Điều kiện xem xét lại

- Số lượng khẳng định hoặc nguồn khiến Markdown không còn là định dạng đủ bền để quét.
- Bộ quét tạo quá nhiều cảnh báo giả hoặc không thể diễn đạt điều kiện kiểm tra lại cần thiết.
- Một nền tảng nguồn thay đổi cách công bố phiên bản, chính sách hoặc ngày cập nhật.
- Bằng chứng vận hành cho thấy cờ `Block use` cần cơ chế quản trị hoặc thời hạn riêng.
