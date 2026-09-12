# Gói thiết kế và phân tích ảnh hưởng

## A — Tiếp nhận và phân loại

### Mệnh đề cần kiểm tra

Lộ trình hiện đặt cụm “xây cơ sở tri thức” ở Tuần 5. Trong khi đó G04 đã yêu cầu không gian dự án, nguồn chuẩn, nhật ký quyết định và một phiên mới có thể tiếp tục; G08 lại yêu cầu dự án đã có nhiều tệp và quyết định. Cách diễn đạt hiện tại có thể khiến nền tri thức xuất hiện quá muộn, dù chiến lược truy xuất nâng cao vẫn phù hợp để dạy ở Tuần 5.

### Phân loại

- Thao tác: `clarify` ranh giới và phân bổ năng lực xuyên suốt; không `add`, `rename`, `retire` hoặc đánh lại mã mục tiêu.
- Chế độ: `Architecture change`, vì thay đổi ranh giới và sản phẩm trung gian giữa G04, G08 và G09.
- Quyết định kích hoạt: đạt; thay đổi tác động tới kết quả quan sát được, ranh giới trách nhiệm và sản phẩm bàn giao.

## B — Chẩn đoán

### Bằng chứng nội bộ

- `AI-native-builder-curriculum-plan.md` mô tả Tuần 2 có workspace, kho mã nguồn, chỉ dẫn và nhật ký quyết định; Tuần 5 lại dùng “xây cơ sở tri thức”.
- G04 đã yêu cầu nguồn chuẩn, nhật ký quyết định, vị trí sản phẩm trung gian và kiểm thử bằng phiên tác nhân mới.
- G08 yêu cầu đầu vào là kho dự án có nhiều tệp/quyết định và đầu ra cho G09 là quy ước ngữ cảnh để mã hóa.
- G09 yêu cầu bằng chứng lặp lại trước khi tạo rule, skill hoặc workflow.

### Chẩn đoán

Đây là lỗi phân bổ và diễn đạt năng lực, không phải thiếu một goal mới. Nền tri thức dự án tối thiểu phải xuất hiện ở G04/Tuần 2; G08 nên quản trị, đóng gói và đánh giá chiến lược truy xuất trên nền đã tích lũy; G09 chỉ mã hóa những cải tiến đã có bằng chứng.

### Kết quả trước/sau

| Điểm | Trước | Sau |
|---|---|---|
| G04/Tuần 2 | Workspace, repo, chỉ dẫn và decision log; vai trò tri thức chưa nói rõ | Thêm “xương sống tri thức dự án tối thiểu”: source map, điểm vào, provenance và decision log |
| G08/Tuần 5 | Tìm kiếm, context package, nén và “xây cơ sở tri thức” | Quản lý/truy xuất tri thức đã tích lũy; so sánh tệp/index/RAG/graph theo nhu cầu và chi phí |
| G09/Tuần 6 | Mã hóa quy tắc, skill, workflow từ bằng chứng | Có thể mã hóa quy ước truy xuất, index hoặc harness chỉ khi mẫu hình lặp lại |

### Phản biện phương án

- Giữ nguyên: ít chi phí sửa nhưng để nguyên tín hiệu sư phạm dễ hiểu sai.
- Đưa toàn bộ G08 lên Tuần 2: làm quá tải người mới và khiến bài học về truy xuất thiếu dữ liệu dự án để kiểm thử.
- Tạo goal riêng về knowledge base: không cần thiết; năng lực này vừa là nền xuyên suốt vừa có phần nâng cao.
- Phương án được chọn: gieo nền ở G04, dạy quản trị/truy xuất ở G08, mã hóa có bằng chứng ở G09; giữ nguyên thứ tự goal.

## C — Kiểm chứng tiền đề thực tế

Không chạy `$curriculum-reference-research` trong lượt này. Quyết định dựa trên cách các nguồn chuẩn nội bộ hiện định nghĩa G04/G08/G09 và không phụ thuộc vào claim về API, công cụ, giá, chính sách hoặc kết quả nghiên cứu bên ngoài. Nếu sau này chọn công cụ cụ thể, phải định tuyến sang `$curriculum-reference-research` hoặc `refresh-volatile-content` phù hợp.

## D — Phương án và hợp đồng thay đổi

### Phương án được duyệt thử

Giữ 11 goal và thứ tự hiện tại; cập nhật năm nguồn chuẩn để:

1. Nói rõ ở G04/Tuần 2 rằng người học thiết lập nền tri thức dự án tối thiểu.
2. Đổi mô tả G08/Tuần 5 từ “xây cơ sở tri thức” sang quản lý, đóng gói, truy xuất và quyết định chiến lược trên nền đã có.
3. Nêu ở G09/Tuần 6 rằng tự động hóa index, metadata, RAG hoặc graph là ứng viên chỉ sau khi có bằng chứng lặp lại.
4. Giữ `curriculum-map.md` không đổi vì đồ thị thứ tự không đổi.

### Hợp đồng mục tiêu

- **Đầu vào:** các nguồn chuẩn hiện hành, dự án có cấu trúc và quyết định, bằng chứng thiết kế ở lượt này.
- **Hành vi mới cần quan sát:** người học hiểu nền tri thức được dựng sớm, nhưng chỉ chọn công cụ truy xuất nâng cao sau khi xác định nhu cầu và chi phí.
- **Quyết định của người học:** phần nào là nền bắt buộc, phần nào là chiến lược nâng cao, có mã hóa mẫu hình hay không.
- **Sản phẩm trung gian:** xương sống tri thức tối thiểu ở G04; context package và quyết định chiến lược ở G08; ứng viên rule/skill/workflow có test trước/sau ở G09.
- **Bằng chứng hoàn thành:** trace từ tuần/goal tới sản phẩm và không có bước nhảy yêu cầu RAG/graph bắt buộc.
- **Nơi sử dụng tiếp:** G05/G06 dùng nền tìm kiếm và nguồn gốc; G08 dùng dự án đủ lớn; G09 nhận bằng chứng lặp lại.

## E — Đồ thị trước/sau và bản đồ ảnh hưởng

```text
BEFORE
G04 minimum harness ──→ G05/G06
G07 tools + G08 context (including “build knowledge base” in Week 5)
                         └──→ G09 advanced harness

AFTER
G04 minimum harness + project knowledge spine
  └──→ G05/G06 use searchable sources and decision provenance
G07 tools + G08 context retrieval/packaging/strategy
  └──→ G09 evidence-based harness upgrade (optional index/RAG/graph)
```

### Bản đồ tệp

| Tệp | Nhãn | Lý do | Chủ sở hữu |
|---|---|---|---|
| `AI-native-builder-curriculum-plan.md` | `Update` | Sửa mô tả Tuần 2, 5, 6 | Chủ sở hữu chương trình |
| `curriculum-content-architecture.md` | `Update` | Đồng bộ hợp đồng G04, G08, G09 | Chủ sở hữu kiến trúc |
| `ai-native-builder/goals/g04-tao-harness-toi-thieu/README.md` | `Update` | Nêu nền tri thức tối thiểu và provenance | Chủ sở hữu G04 |
| `ai-native-builder/goals/g08-quan-ly-context-du-an/README.md` | `Update` | Đổi ranh giới “xây” thành “quản lý/truy xuất” | Chủ sở hữu G08 |
| `ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md` | `Update` | Đưa tự động hóa truy xuất vào nhánh có bằng chứng | Chủ sở hữu G09 |
| `ai-native-builder/curriculum-map.md` | `No change` | Thứ tự và cạnh goal không đổi | Chủ sở hữu bản đồ |
| `ai-native-builder/runs/full-1-1-20-buoi/schedule.md` | `No change` | Tệp hiện chỉ là placeholder kiểm kê | Chủ sở hữu run |
| `ai-native-builder/runs/full-1-1-20-buoi/studio-03-mo-rong-va-context.md` | `Reverify` | Heading không đổi nhưng cần đối chiếu khi soạn bài | Chủ sở hữu run |
| `.agents/workflows/*` | `Reverify` | Chỉ workflow trạng thái và hồ sơ quyết định thay đổi; không đổi quy trình nội dung | Chủ sở hữu quản trị |

### Kế hoạch hoàn tác

Khôi phục đúng năm tệp có nhãn `Update` về trạng thái trước lượt chạy theo manifest trong `change-manifest.md`; không dùng thao tác phá hủy rộng. Các tệp trạng thái workflow, quyết định và hồ sơ vận hành không được xóa; chúng phải ghi lại việc hoàn tác. Nếu kiểm định chỉ tìm lỗi câu chữ cục bộ, sửa trong danh sách này. Nếu phát hiện cần đổi thứ tự hoặc tạo goal mới, dừng, ghi `Revision requested` và quay lại D/F.

### Câu hỏi mở được giữ lại

`curriculum-map.md` hiện biểu diễn G07/G08 cùng một nhánh song song, trong khi G08 không nhận G07 làm điều kiện tiên quyết. Lượt này giữ nguyên vì không liên quan trực tiếp tới việc gieo nền tri thức; nếu cần biến quan hệ này thành thứ tự bắt buộc, phải mở một lượt kiến trúc riêng.
