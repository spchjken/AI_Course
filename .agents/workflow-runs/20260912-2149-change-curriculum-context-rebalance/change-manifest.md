# Manifest thay đổi và hoàn tác

- **Lượt:** `20260912-2149-change-curriculum-context-rebalance`
- **Mục đích:** khóa danh sách tệp nguồn chuẩn đã sửa và cung cấp đường hoàn tác có phạm vi.
- **Lưu ý:** Git không cung cấp diff trong workspace này; manifest dùng các hunk thay đổi đã ghi trong lượt chạy và hash sau áp dụng. Không được coi hash sau là bằng chứng rằng thay đổi trước đó chưa tồn tại.

## Tệp nguồn chuẩn được cập nhật

| Tệp | Thao tác | Hunk/ý nghĩa | SHA-256 sau áp dụng |
|---|---|---|---|
| `AI-native-builder-curriculum-plan.md` | `Update` | Mô tả Tuần 2, 5, 6 | `4C966EF79DD3ECE0F492EC206B07DC65D6D642FA60CB2BE68849791ACE1FEBCB` |
| `curriculum-content-architecture.md` | `Update` | Hợp đồng G04, G08, G09 | `B1C8D441C2AA1E044791878127570F6EA3CC342D87D452535A200596DD0FBEE2` |
| `ai-native-builder/goals/g04-tao-harness-toi-thieu/README.md` | `Update` | Kết quả và phạm vi nền tri thức tối thiểu | `F9A1E3B5161BBEC95C33E8868E2ECFF92C56BCA92015A1232A901E1E7034E55D` |
| `ai-native-builder/goals/g08-quan-ly-context-du-an/README.md` | `Update` | Ranh giới quản lý/truy xuất trên nền đã có | `960E7A9347EF24476A416A759161B145DB79EEA00AE2744789015521701F9EE0` |
| `ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md` | `Update` | Điều kiện tự động hóa có bằng chứng | `70DB255B476ECF2FB073DB4B3695A27F4D382BDD78ED8CA274B72565B749A965` |

## Tệp quản trị và vận hành được cập nhật riêng

Các tệp sau được tạo hoặc sửa để phục vụ trạng thái và bằng chứng của lượt chạy; không thuộc danh sách nguồn chuẩn cần hoàn tác bằng inverse content patch:

- `README.md` và `.agents/workflows/README.md` — trạng thái tạm thời `Active`.
- `.agents/workflows/change-curriculum-architecture.md` — trạng thái tạm thời `Active`.
- `.agents/decisions/2026-09-12-g04-g08-g09-context-boundary-trial.md`.
- `.agents/workflow-runs/20260912-2149-change-curriculum-context-rebalance/`.

## Thủ tục hoàn tác

1. Giữ nguyên toàn bộ hồ sơ quyết định và hồ sơ lượt chạy để bảo toàn bằng chứng.
2. Đọc `rollback-hunks.md`, xác nhận ngữ cảnh `AFTER` khớp, rồi dùng các hunk inverse tương ứng với năm tệp nguồn chuẩn ở trên để khôi phục câu chữ trước lượt chạy; xác nhận bằng kiểm tra UTF-8 và dependency order.
3. Nếu hoàn tác vì thất bại kiểm định, đổi trạng thái lượt thành `Rolled back` và ghi nguyên nhân trong `verification.md`.
4. Trả trạng thái workflow trong ba vị trí (`.agents/workflows/change-curriculum-architecture.md`, `.agents/workflows/README.md`, `README.md`) về `Proposed` sau khi lượt thử đóng.
5. Không xóa hoặc reset thư mục workspace rộng; chỉ sửa đúng các hunk đã khóa.

## Kiểm tra sau hoàn tác

- Các cụm “xương sống tri thức dự án tối thiểu” và “Quản lý và truy xuất ngữ cảnh” không còn trong năm tệp nguồn nếu hoàn tác toàn phần.
- `rollback-hunks.md` phải được đối chiếu tại cổng kiểm định; không dùng hash sau áp dụng thay cho preimage.
- Mã và thứ tự `g01`–`g11` vẫn nhất quán.
- Hủy hiệu lực có chọn lọc đối với bằng chứng phụ thuộc vào phương án thử.
