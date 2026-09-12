# Chuẩn hóa ngôn ngữ và ký hiệu kỹ thuật

- Ngày: 2026-09-05
- Trạng thái: Đã chấp thuận
- Bên quyết định: Chủ sở hữu giáo trình và cộng sự AI
- Phạm vi ảnh hưởng: toàn bộ tài liệu tiếng Việt trong kho dự án; ưu tiên `.agents/rules/`, `.agents/workflows/`, tài liệu kiến trúc và các bản định hướng bài học
- Thay thế hồ sơ: Không có

## Bối cảnh và xung đột

Tài liệu đang chen từ tiếng Anh thông thường vào câu tiếng Việt, đồng thời dùng nhãn nửa Anh nửa Việt trong sơ đồ và khối ký hiệu. Điều này làm mờ ranh giới giữa tên định danh chuẩn với lời diễn giải và khuyến khích tác nhân AI tiếp tục tạo nội dung thiếu nhất quán.

## Các phương án đã cân nhắc

1. Giữ cách viết hiện tại và chỉ sửa từng chỗ gây hiểu nhầm.
2. Chuyển toàn bộ kho dự án sang tiếng Anh.
3. Dùng tiếng Việt tự nhiên cho văn bản; dùng tiếng Anh nhất quán trong khối ký hiệu kỹ thuật; giữ nguyên tên định danh chính xác.

## Bằng chứng thuận và nghịch

- Các khái niệm về nội dung bài học, kiểm định độc lập và ranh giới mục tiêu đều có cách diễn đạt tiếng Việt rõ nghĩa nhưng trước đây vẫn bị viết bằng tiếng Anh trong câu tiếng Việt.
- Một số sơ đồ từng pha trộn tên định danh như `complete-goal-lessons` với lời chú thích nửa Anh nửa Việt, khiến người đọc khó phân biệt tên bước với phần giải thích.
- Tên tệp, tên kỹ năng, lệnh, trạng thái chuẩn và nhãn giao diện cần được giữ nguyên để có thể gọi hoặc kiểm tra chính xác.
- Dịch tên định danh sẽ làm hỏng tham chiếu; giữ mọi từ tiếng Anh lại sẽ tiếp tục tạo văn phong pha trộn.

## Quyết định

- Văn bản tiếng Việt phải ưu tiên cách diễn đạt tiếng Việt rõ nghĩa.
- Chỉ giữ nguyên tên định danh và thuật ngữ không có bản dịch đủ chính xác.
- Khối ký hiệu kỹ thuật dùng tiếng Anh nhất quán; khối mẫu dành trực tiếp cho học viên hoặc giảng viên dùng tiếng Việt.
- Chuẩn hóa trước các tài liệu quản trị mà tác nhân AI dùng làm chỉ dẫn, sau đó rà toàn bộ tài liệu tiếng Việt hiện có.

## Hệ quả và phạm vi chuyển đổi

- Các kỹ năng đang viết hoàn toàn bằng tiếng Anh được giữ nguyên; chỉ sửa nếu bản thân một đoạn trộn hai ngôn ngữ không có lý do.
- Không đổi tên tệp, thư mục, kỹ năng, quy trình, mã mục tiêu hoặc giá trị trạng thái trong đợt chuẩn hóa này.
- Liên kết và ý nghĩa nội dung phải được kiểm tra lại sau khi thay từ.

## Điều kiện xem xét lại

- Một bản dịch tiếng Việt làm mất nghĩa kỹ thuật hoặc khiến học viên không nhận ra nhãn trong công cụ.
- Kho dự án chọn một ngôn ngữ vận hành duy nhất khác trong tương lai.
