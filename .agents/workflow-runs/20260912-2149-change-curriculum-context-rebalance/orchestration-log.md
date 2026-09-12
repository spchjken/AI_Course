# Nhật ký điều phối

| Mã đơn vị | Định danh tác nhân | Tác nhân cha | Vai trò và giai đoạn | Hành động | Tệp được phép sửa | Đầu vào | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|---|
| A | `root-20260912-2149` | `root` | Điều phối viên — A | `root` | Hồ sơ lượt chạy, không sửa nguồn chuẩn | Yêu cầu người dùng, workflow và nguồn chuẩn | `completed` | `design-review.md`, phạm vi khóa |
| B-D | `root-20260912-2149` | `root` | Phân tích/thiết kế — B, D | `root` | `design-review.md` | G04, G08, G09, curriculum plan, architecture | `completed` | Chẩn đoán, phương án và hợp đồng thay đổi |
| C | `root-20260912-2149` | `root` | Nghiên cứu tiền đề — C | `root` | `design-review.md` | Nguồn nội bộ; không có claim biến động cần tra cứu | `not-required` | Ghi rõ lý do không chạy nghiên cứu ngoại lai |
| E | `root-20260912-2149` | `root` | Phân tích ảnh hưởng — E | `root` | `design-review.md` | Phương án đã chọn | `completed` | Đồ thị trước/sau và bản đồ tệp |
| F | `human-owner-20260912-2149` | `root` | Chủ sở hữu giáo trình — F | `human-decision` | Nguồn chuẩn chỉ sau chấp thuận | Gói đề xuất trong `design-review.md` | `approved` | Cho phép áp dụng trong phạm vi khóa |
| G | `root-20260912-2149` | `root` | Người thực hiện — G | `root` | Danh sách `Update` trong `design-review.md` | Quyết định F và snapshot trước thay đổi | `completed` | Năm nguồn chuẩn đã cập nhật; `verification-preflight.md` |
| H1 | `/root/architecture_reviewer` | `root` | Người kiểm định độc lập — H | `fresh-review` | Không sửa tệp nguồn chuẩn | Đầu ra G, tiêu chí workflow và rules | `completed` | Báo cáo độc lập: `Needs revision`; ba blocker đã định tuyến sửa |
| H2 | `/root/architecture_reviewer_2` | `root` | Người kiểm định độc lập — H | `fresh-review` | Không sửa tệp nguồn chuẩn | Đầu ra G, manifest và rollback hunks | `completed` | Re-review: operation `Pass`; phạm vi rollback `Pass`; rollback thực thi `Not verified` |
| H3 | `/root/architecture_reviewer_3` | `root` | Người kiểm định độc lập — H | `fresh-review` | Không sửa tệp nguồn chuẩn | Toàn bộ hồ sơ sau sửa, manifest và rollback hunks | `completed` | Phạm vi/nhất quán `Pass`; rollback runtime và learner pilot `Not verified`; khuyến nghị `Awaiting decision` |
| I | `root-20260912-2149` | `root` | Điều phối viên — I | `root` | Hồ sơ lượt chạy, hồ sơ quyết định | H1, H2, H3 và `verification.md` | `completed` | Bàn giao hoàn tất; workflow trả về `Proposed`; lượt `Awaiting decision` |

`pending-independent-reviewer` là placeholder trong nhật ký trước khi công cụ điều phối trả định danh tác nhân thật; không được dùng nó làm bằng chứng độc lập.
