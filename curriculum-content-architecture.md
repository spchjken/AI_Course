# Kiến trúc nguồn bài giảng AI-native Builder

## Nguyên tắc

Khung bài giảng được tổ chức theo ba lớp:

1. **Mục tiêu chính** — các kết quả học tập có quan hệ phụ thuộc rõ ràng.
2. **Năng lực xuyên suốt** — các hành vi được dùng lặp lại ở nhiều mục tiêu, không trở thành một chương riêng.
3. **Lộ trình** — cách ghép các mục tiêu thành chương trình thực hành ngắn hoặc khóa 1-1 đầy đủ.

“Đọc và can thiệp mã nguồn” không phải mục tiêu hoặc chương độc lập. Điểm chạm này tăng dần trong từng mục tiêu để học viên dùng mã nguồn khi cần sở hữu và kiểm chứng sản phẩm, thay vì phải học lập trình trước rồi mới dùng AI.

Hồ sơ trong `pilots/` không phải lớp nội dung thứ tư. Chúng lưu bằng chứng dạy thử theo phiên bản để kiểm chứng hoặc cải thiện ba lớp trên; không thay định nghĩa mục tiêu, nội dung bài học hay lộ trình.

## Cây thư mục

```text
ai-native-builder/
├── README.md
├── curriculum-map.md
│
├── shared/
│   ├── templates/
│   │   ├── product-brief.md
│   │   ├── product-spec.md
│   │   ├── system-map.md
│   │   ├── agent-plan.md
│   │   ├── decision-log.md
│   │   └── project-readme.md
│   ├── policies/
│   │   ├── privacy-secrets-and-permissions.md
│   │   └── verification-standard.md
│   └── practices/
│       ├── ai-conversation.md
│       ├── code-contact.md
│       ├── evidence-and-reflection.md
│       └── safe-experimentation.md
│
├── goals/
│   ├── g01-dinh-huong-van-de/
│   ├── g02-viet-spec-san-pham/
│   ├── g03-thiet-ke-khung-he-thong-san-pham/
│   ├── g04-tao-harness-toi-thieu/
│   ├── g05-dieu-khien-agent-theo-vong-lap/
│   ├── g06-kiem-chung-output-va-quyet-dinh/
│   ├── g07-mo-rong-san-pham-bang-tools/
│   ├── g08-quan-ly-context-du-an/
│   ├── g09-nang-cap-harness-rules-skills-workflows/
│   ├── g10-ship-va-so-huu-san-pham/
│   └── g11-xay-va-trinh-bay-capstone/
│
├── runs/
    ├── workshop-3-buoi/
    │   ├── buoi-01-dinh-huong-va-spec.md
    │   ├── buoi-02-khung-he-thong-va-harness.md
    │   └── buoi-03-build-verify-va-demo-noi-bo.md
    └── full-1-1-20-buoi/
        ├── schedule.md
        ├── studio-01-khoi-tao-san-pham.md
        ├── studio-02-kiem-chung-mini-project.md
        ├── studio-03-mo-rong-va-context.md
        └── studio-04-ship-capstone.md
│
└── pilots/
    └── pYYYYMMDD-<target-slug>-<sequence>/
        ├── README.md
        ├── collection-plan.md
        ├── evidence-register.md
        ├── observations.md
        ├── analysis.md
        ├── decision.md
        └── review.md
```

## Quan hệ phụ thuộc giữa các mục tiêu

```text
Problem orientation
  → Product specification
    → Product system design
      → Minimum harness
        → Agent control
          → Verification
            → Tools and context
              → Advanced harness
                → Product release
                  → Capstone
```

### G01 — Định hướng vấn đề

Học viên dùng AI như đối tác đối thoại để làm rõ vấn đề, người dùng, giá trị, giới hạn và kết quả mong muốn.

### G02 — Viết đặc tả sản phẩm

Biến vấn đề thành hành vi người dùng, luồng thao tác, ràng buộc và tiêu chí nghiệm thu có thể kiểm chứng.

### G03 — Thiết kế khung hệ thống sản phẩm

Xây bản đồ sản phẩm bằng ngôn ngữ thường: các thành phần cần có, trách nhiệm, luồng dữ liệu hoặc trạng thái, quan hệ phụ thuộc, rủi ro, phần chưa làm và lát cắt xây dựng nhỏ nhất.

### G04 — Tạo bộ khung kiểm soát tối thiểu

Biến khung hệ thống thành môi trường để AI làm việc nhất quán: không gian làm việc, kho mã nguồn, cấu trúc dự án, xương sống tri thức tối thiểu (điểm vào, nguồn chuẩn, provenance và nhật ký quyết định), chỉ dẫn cơ bản và vòng lặp lập kế hoạch–xây dựng–kiểm chứng.

### G05 — Điều khiển tác nhân AI theo vòng lặp

Dùng yêu cầu cho AI, ngữ cảnh, phân rã tác vụ, lập kế hoạch trước và phản hồi bằng bằng chứng để điều khiển tác nhân AI qua nhiều bước.

### G06 — Kiểm chứng đầu ra và quyết định

Xác nhận hành vi sản phẩm theo tiêu chí, phản biện đầu ra AI, phát hiện thông tin bịa đặt và hoàn tác khi cần.

### G07 — Mở rộng sản phẩm bằng công cụ

Làm việc với API, thông tin bí mật, cơ chế gọi công cụ, MCP, quyền hạn và chi phí theo nguyên tắc có kiểm soát.

### G08 — Quản lý ngữ cảnh dự án

Quản lý và truy xuất tri thức dự án đã tích lũy: tìm kiếm theo tác vụ, tạo và kiểm thử gói ngữ cảnh, ghi nguồn gốc, nén và làm mới thông tin, rồi quyết định khi nào tệp/chỉ mục đủ và khi nào cần cơ sở tri thức được tuyển chọn, RAG hoặc chế độ xem dạng đồ thị.

### G09 — Nâng cấp bộ khung kiểm soát

Rút kinh nghiệm từ dự án để tạo quy tắc, kỹ năng và quy trình tái sử dụng, bao gồm metadata, chỉ mục hoặc truy xuất nâng cao chỉ khi có mẫu hình lặp lại và bằng chứng kiểm thử trước/sau, giúp tác nhân AI làm việc đáng tin cậy hơn qua thời gian.

### G10 — Phát hành và sở hữu sản phẩm

Đánh giá chất lượng, bảo vệ dữ liệu và thông tin bí mật, triển khai, viết README và chịu trách nhiệm với sản phẩm công khai.

### G11 — Xây dựng và trình bày dự án tổng kết

Hoàn thiện dự án tổng kết theo mục tiêu cá nhân, có kho mã nguồn, bản trình diễn, bằng chứng quá trình, phần giải thích kiến trúc và câu chuyện hồ sơ năng lực/CV.

## Năng lực xuyên suốt

Các tài liệu trong `shared/practices/` được liên kết từ mọi mục tiêu phù hợp:

- **Đối thoại với AI:** học viên yêu cầu AI phản biện rồi tự chốt quyết định.
- **Điểm chạm mã nguồn:** nêu rõ phần mã nguồn cần quan sát, mô tả, kiểm định, sửa hoặc chẩn đoán trong mục tiêu hiện tại.
- **Bằng chứng và phản tư:** lưu yêu cầu cho AI, quyết định, phần thay đổi, kết quả kiểm thử và điều đã học.
- **Thử nghiệm an toàn:** dùng nhánh hoặc bản chụp, kiểm soát dữ liệu, thông tin bí mật, quyền hạn và khả năng hoàn tác.

Mỗi thư mục `goals/gNN-*` có một `README.md` trả lời tối thiểu:

```md
## Mục tiêu và tiêu chí đạt
## Vai trò của AI
## Quyền quyết định của học viên
## Điểm chạm với mã nguồn
## Sản phẩm trung gian và bằng chứng hoàn thành
## Quy tắc an toàn áp dụng
```

## Lộ trình

- **Chương trình thực hành 3 buổi:** dùng `g01` đến `g06` ở mức tối thiểu; kết thúc bằng một bản trình diễn nội bộ có kiểm chứng cơ bản, không hứa dự án tổng kết hoặc triển khai công khai.
- **Khóa 1-1 gồm 20 buổi:** đi qua toàn bộ `g01` đến `g11`, với các buổi thực hành tích hợp để kiểm định sản phẩm trung gian, áp dụng vào dự án và hoàn thiện dự án tổng kết.
- Thư mục `runs/` chỉ điều phối thứ tự, thời lượng và điểm kiểm tra; không sao chép nội dung từ `goals/`.
- Thư mục `pilots/` lưu hồ sơ dạy thử theo từng phiên bản và phạm vi kiểm chứng; chỉ chứa bằng chứng đã ẩn danh, không chứa dữ liệu thô hoặc thông tin nhận dạng của học viên.
