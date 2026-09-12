# Báo cáo kiểm định và bàn giao

- **Phạm vi:** thay đổi kiến trúc phân bổ năng lực giữa G04, G08 và G09.
- **Không đánh giá:** hiệu quả dạy học thực tế, vì chưa có pilot người học.
- **Trạng thái chất lượng:** `Needs revision` cho tới khi các câu hỏi runtime/pilot được kiểm chứng; đây không phải trạng thái của toàn bộ giáo trình.

## Kết quả kiểm định

| Hạng mục | Kết quả | Bằng chứng |
|---|---|---|
| Operation hợp lệ | `Pass` | `design-review.md` chỉ dùng `clarify`; không thêm goal hoặc đổi mã/thứ tự |
| Nhất quán G04 → G08 → G09 | `Pass` | Năm nguồn chuẩn cùng phân lớp nền sớm → truy xuất/quản trị → mã hóa có bằng chứng |
| Dependency order | `Pass` | `curriculum-map.md` giữ nguyên chuỗi `g01`–`g11` |
| Phạm vi năm tệp Update | `Pass` về danh sách; `Not verified` về VCS diff | `change-manifest.md` và hash sau áp dụng; workspace không có Git diff |
| Kế hoạch rollback | `Pass` về phạm vi và inverse hunks; `Not verified` về chạy rollback thật | `change-manifest.md`, `rollback-hunks.md`; chưa hoàn tác vì phương án đang được giữ |
| Human decision gate | `Pass` | Hồ sơ quyết định `2026-09-12-g04-g08-g09-context-boundary-trial.md` |
| Independent review | `Pass` về tính độc lập và phạm vi; `Not verified` về rollback runtime/learner pilot | H1, H2 và H3 là các lượt độc lập, không sửa tệp; H3 xác nhận phạm vi/nhất quán |

## Hạn chế còn lại

1. Không có Git snapshot/diff trong workspace nên không thể xác minh lịch sử byte-level trước thay đổi.
2. Rollback hunks đã được ghi nhưng chưa chạy; chạy rollback sẽ thay đổi phương án đang được thử và chỉ được làm khi có quyết định `Reject` hoặc `Revert`.
3. Chưa có bằng chứng pilot người học để nâng các claim về beginner clarity hoặc time feasibility.
4. Quan hệ song song G07/G08 được giữ nguyên; nếu muốn biến thành dependency bắt buộc, mở lượt kiến trúc riêng.

## Bàn giao

- `complete-goal-lessons` phải dùng hợp đồng mới khi soạn lesson package G04/G08/G09.
- `compose-learning-run` chỉ cần reverify studio 03 khi nội dung lesson được tạo; chưa có thay đổi lịch trong lượt này.
- Nếu sau này chọn công cụ metadata/index/RAG/graph cụ thể, định tuyến sang workflow/skill nghiên cứu và refresh volatile tương ứng.

## Kết luận lượt

Lượt thử đã hoàn thành phần áp dụng, kiểm định cấu trúc và bàn giao. Kết quả là `Awaiting decision`: phương án hiện đang được giữ để Chủ sở hữu kho quyết định tiếp, nhưng workflow đã trả về `Proposed` sau thời gian `Active` tạm thời. Không tuyên bố `Validated` cho thiết kế sư phạm, không coi rollback runtime hoặc learner pilot đã được kiểm chứng, và không được chạy hàng loạt.
