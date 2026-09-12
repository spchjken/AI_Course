# Kiểm tra trước kiểm định độc lập

- **Phạm vi:** cấu trúc và tính nhất quán của phần thay đổi G04–G08–G09.
- **Người chạy:** `root-20260912-2149`.
- **Thời điểm:** 2026-09-12.

## Phép kiểm tra và kết quả

1. Đọc UTF-8 năm tệp nguồn chuẩn bị thay đổi: `PASS`.
2. Kiểm tra `g01` đến `g11` vẫn theo thứ tự hiện có trong `ai-native-builder/curriculum-map.md`: `PASS`.
3. Kiểm tra các câu chữ mới về nền tri thức, truy xuất và tự động hóa có mặt đúng ở plan/architecture/G04/G08/G09: `PASS`.
4. Kiểm tra thay đổi không tạo goal mới, không đổi mã goal và không yêu cầu RAG/graph vận hành: `PASS` theo phạm vi tệp.
5. Kiểm tra liên kết nội bộ trong các tệp run và design package: `PASS`, không có liên kết hỏng.

Đây là preflight của người thực hiện, không thay cho kiểm định độc lập ở giai đoạn H.
