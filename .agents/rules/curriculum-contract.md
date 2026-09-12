# Đặc tả giáo trình

## Khi nào áp dụng

Áp dụng cho mọi thay đổi ảnh hưởng mục tiêu học tập, thứ tự bài, cấu trúc kho dự án, chương trình thực hành ngắn, khóa đầy đủ hoặc sản phẩm trung gian của học viên.

## Nguồn chuẩn có thẩm quyền

- `AI-native-builder-curriculum-plan.md`: mục đích, đối tượng, phạm vi, thời lượng và đầu ra chương trình.
- `curriculum-content-architecture.md`: nguồn chuẩn về định nghĩa mục tiêu, ranh giới năng lực, quan hệ phụ thuộc và mô hình tái sử dụng.
- `ai-native-builder/curriculum-map.md`: hình chiếu vận hành được suy ra từ kiến trúc nội dung; chỉ biểu diễn mã mục tiêu, thứ tự, quan hệ phụ thuộc và liên kết điều hướng cần cho `runs/`.
- `ai-native-builder/`: phần triển khai theo các tài liệu cấp trên.
- `ai-native-builder/goals/`: nguồn chuẩn của nội dung triển khai từng bài học; mỗi `README.md` là bản định hướng thiết kế và các tệp còn lại là tài liệu thực thi.
- `ai-native-builder/runs/`: lịch và cách ghép bài; không chứa bản sao nội dung bài học.
- `ai-native-builder/pilots/`: hồ sơ dạy thử đã ẩn danh, gồm phạm vi bằng chứng, phiên bản đã khóa, phân tích, quyết định và kiểm định; không chứa dữ liệu nhận dạng hay bản sao dữ liệu thô.
- `references.md` cạnh nội dung phụ thuộc: nguồn sở hữu cục bộ cho khẳng định dùng nguồn bên ngoài, phán quyết, bằng chứng, phạm vi và điều kiện kiểm tra lại; không tạo bản sao tập trung của sổ này.
- `ai-native-builder/shared/`: mẫu, chính sách và phương pháp thực hành dùng chung.
- `.agents/decisions/`: lịch sử quyết định quản trị, bằng chứng và hệ quả; không thay thế các nguồn chuẩn ở trên.

### Ranh giới giữa kiến trúc và bản đồ chương trình

- Sửa `curriculum-content-architecture.md` khi thay đổi ý nghĩa, phạm vi, mã, điều kiện tiên quyết hoặc quan hệ phụ thuộc của mục tiêu.
- Sửa `ai-native-builder/curriculum-map.md` để phản ánh kiến trúc đã được chấp thuận hoặc bổ sung liên kết điều hướng không làm thay đổi nghĩa của mục tiêu.
- Không đặt mô tả bài học, bảng tiêu chí, hoạt động hoặc lý do thiết kế đầy đủ trong bản đồ chương trình.
- Nếu hai tệp xung đột, kiến trúc nội dung chi phối; phải sửa bản đồ và rà soát mọi lộ trình phụ thuộc trước khi tiếp tục triển khai.

## Quan hệ phụ thuộc bắt buộc

Giữ trục chính:

`Orientation → Specification → System design → Minimum harness → Agent control → Verification → Tools and context → Advanced harness → Release → Capstone`

- Không đưa triển khai công khai hoặc dự án tổng kết vào trước khi học viên có đặc tả, sơ đồ hệ thống và bằng chứng kiểm chứng tối thiểu.
- Chương trình thực hành ngắn kết thúc bằng nguyên mẫu hoặc bản trình diễn nội bộ có kiểm chứng cơ bản, không được trình bày như một dự án tổng kết hoàn chỉnh.
- Khi thêm, xóa, đổi mục tiêu hoặc quan hệ phụ thuộc, phải rà soát `ai-native-builder/curriculum-map.md` và mọi lộ trình tham chiếu đến mục tiêu đó.

## Đơn vị nội dung

- Mỗi thư mục `ai-native-builder/goals/gNN-*` là một bài học xoay quanh một mục tiêu chính.
- “Đọc và can thiệp mã nguồn” là năng lực xuyên suốt, không tạo thành một bài hoặc giai đoạn độc lập.
- Không tạo bài chỉ để giới thiệu một công cụ; công cụ phải phục vụ một năng lực hoặc kết quả sản phẩm.
- Nội dung dùng chung chỉ có một bản chuẩn trong `shared/`; bài học và lộ trình liên kết tới bản đó.

## Ngôn ngữ và đặt tên

- Văn bản diễn giải, tài liệu quản trị và nội dung dành cho học viên phải dùng tiếng Việt tự nhiên. Không chen từ tiếng Anh khi đã có cách diễn đạt tiếng Việt rõ nghĩa và không làm mất độ chính xác.
- Chỉ giữ nguyên tên tệp, đường dẫn, lệnh, tên kỹ năng, tên quy trình, mã định danh, giá trị trạng thái chuẩn hóa, nhãn giao diện và thuật ngữ kỹ thuật chưa có cách dịch phù hợp. Đặt tên định danh trong dấu mã khi xuất hiện trong câu tiếng Việt.
- Các khối ký hiệu kỹ thuật dùng để điều phối — gồm sơ đồ kiến trúc, sơ đồ trạng thái, cây thư mục, đặc tả dữ liệu, đặc tả giao việc cho tác nhân AI, sổ theo dõi thực thi và mã giả — phải dùng tiếng Anh nhất quán cho toàn bộ nhãn, trường và chú thích bên trong. Giải thích ý nghĩa bằng tiếng Việt bên ngoài khối; không trộn hai ngôn ngữ trong cùng khối.
- Ngoại lệ: khối mẫu tạo nội dung trực tiếp cho học viên hoặc giảng viên phải dùng tiếng Việt, trừ tên định danh và nhãn công cụ cần giữ nguyên.
- Dùng từ vựng ưu tiên trong `glossary.md`. Một từ tiếng Anh được lặp lại nhiều lần trong kho dự án không tự trở thành thuật ngữ bắt buộc phải giữ nguyên.
- Tên tệp và thư mục dùng chữ thường, ASCII và kebab-case.
- Mục tiêu dùng mã ổn định `gNN-*`; không tái sử dụng một mã cho mục tiêu khác.
- Ưu tiên Markdown. Chỉ tạo slide, kịch bản hoặc tài nguyên khác khi có nhu cầu cụ thể trong bài.

## Tự kiểm chứng

- Mục tiêu mới có vị trí rõ trong quan hệ phụ thuộc và không trùng mục tiêu hiện có.
- Mọi liên kết từ lộ trình trỏ tới bài học chuẩn.
- Không sao chép nội dung bài học vào `runs/` hoặc nhiều thư mục mục tiêu.
- Hồ sơ dạy thử chỉ trỏ tới phiên bản đã khóa và không chứa dữ liệu nhận dạng, thông tin bí mật hoặc dữ liệu thô ngoài phạm vi.
- Khẳng định phụ thuộc nguồn bên ngoài có `references.md` cục bộ với ngày kiểm tra, phạm vi và điều kiện kiểm tra lại; mọi tệp phụ thuộc chỉ trỏ tới khẳng định sở hữu thay vì sao chép phán quyết.
- Các tài liệu cấp cao và phần triển khai mô tả cùng một quyết định.
