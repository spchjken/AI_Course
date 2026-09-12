# Hồ sơ dạy thử

Thư mục này lưu hồ sơ đã ẩn danh của từng đợt dạy thử bài học hoặc lộ trình. Mỗi hồ sơ là bằng chứng của một phiên bản và một phạm vi cụ thể; nó không thay thế bài học, lộ trình, quy tắc chất lượng hay hồ sơ quyết định quản trị.

## Tạo hồ sơ mới

Chỉ tạo hồ sơ khi đối tượng dạy thử tối thiểu `Pilot-ready` và đã đi qua giai đoạn lập kế hoạch của [`pilot-and-validate`](../../.agents/workflows/pilot-and-validate.md).

```text
pYYYYMMDD-<target-slug>-<sequence>/
├── README.md             # Target, scope, context, and version lock
├── collection-plan.md    # Claims, measures, consent notice, and data handling
├── evidence-register.md  # Anonymized evidence inventory and access limits
├── observations.md       # Expected and observed behavior
├── analysis.md           # Findings, explanations, and change hypotheses
├── decision.md           # Human decisions and routed handoffs
└── review.md             # Independent pilot-evidence review
```

Tên thư mục không được chứa tên, email, tổ chức hoặc dữ liệu có thể nhận diện học viên. Mỗi hồ sơ chỉ có một đối tượng chính: một bài học hoặc một lộ trình.

`review.md` trong hồ sơ này chỉ kiểm định bằng chứng của phiên pilot. Trạng thái chất lượng hiện hành vẫn thuộc `review.md` của bài học hoặc lộ trình được dạy; Người kiểm định độc lập liên kết hai tệp khi cập nhật phán quyết.

Một lượt `No-go` chỉ cần `README.md` và `collection-plan.md`. Lượt dừng ở kiểm tra toàn vẹn bằng chứng cần thêm `evidence-register.md` và `observations.md` nếu đã thu dữ liệu được phép. Chỉ lượt đã đi qua phân tích và quyết định mới cần đủ toàn bộ bộ tệp ở trên.

## Ranh giới dữ liệu

- Chỉ lưu dữ liệu đã giảm thiểu và ẩn danh, cùng trích đoạn cần thiết cho kiểm định.
- Không lưu thông tin nhận dạng, bản đồng ý có chữ ký, khóa truy cập, dữ liệu khách hàng, ảnh chụp nhạy cảm hoặc lịch sử trò chuyện đầy đủ.
- Nếu bằng chứng thô được lưu bên ngoài kho, chỉ ghi loại bằng chứng, người giữ, giới hạn truy cập và phạm vi kiểm định lại trong `evidence-register.md`.
- Không sửa nội dung giáo trình trong thư mục này. Thay đổi được chấp nhận phải được bàn giao về quy trình sở hữu.

Xem [`pilot-and-validate`](../../.agents/workflows/pilot-and-validate.md) để biết điều kiện tạo, quyền sở hữu tệp, cách cập nhật trạng thái và quy tắc dạy thử lại.
