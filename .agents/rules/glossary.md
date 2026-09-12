# Bảng thuật ngữ

Các định nghĩa dưới đây có hiệu lực trong quy tắc, kỹ năng, quy trình và tài liệu điều phối. Nội dung dành cho học viên có thể diễn đạt đơn giản hơn nhưng không được làm đổi nghĩa vận hành.

## Từ vựng tiếng Việt ưu tiên

| Từ tiếng Anh không dùng như danh từ thông thường | Cách diễn đạt ưu tiên |
|---|---|
| `workflow` | quy trình |
| `lesson` | bài học |
| `learner` | học viên |
| `instructor` | giảng viên |
| `artifact` | sản phẩm trung gian hoặc đầu ra |
| `evidence` | bằng chứng |
| `review` | kiểm định hoặc đánh giá |
| `scope` | phạm vi |
| `owner` | bên chịu trách nhiệm |
| `handoff` | bàn giao |
| `claim` | khẳng định |
| `phase` | giai đoạn |
| `checkpoint` | điểm kiểm tra |
| `feedback` | phản hồi |
| `assessment` | đánh giá năng lực |
| `rubric` | bảng tiêu chí đánh giá |
| `goal` | mục tiêu học tập |
| `run` | lộ trình triển khai |
| `input/output` | đầu vào/đầu ra |
| `failure/recovery` | lỗi/phục hồi |
| `timebox` | giới hạn thời gian |
| `dependency` | quan hệ phụ thuộc |
| `design brief` | bản định hướng thiết kế |
| `canonical` | chuẩn hoặc có thẩm quyền |
| `source of truth` | nguồn chuẩn có thẩm quyền |

Bảng này không đổi tên định danh. Ví dụ, giữ nguyên `$lesson-authoring`, `complete-goal-lessons.md` và `Pilot-ready`, nhưng dùng “kỹ năng soạn bài”, “quy trình hoàn thiện bài học” và “trạng thái chất lượng” trong phần diễn giải.

## Khái niệm vận hành

| Thuật ngữ | Nghĩa chuẩn |
|---|---|
| Mục tiêu học tập | Một năng lực hoặc kết quả học tập có mã ổn định `gNN`, với phạm vi và quan hệ phụ thuộc được định nghĩa trong kiến trúc nội dung. |
| Bài học | Bộ tài liệu triển khai một mục tiêu trong `ai-native-builder/goals/gNN-*`, gồm bản định hướng thiết kế và tài liệu cần để học, thực hành, đánh giá. |
| Bản định hướng thiết kế | `README.md` trong thư mục mục tiêu; quy định kết quả, phạm vi, sản phẩm trung gian, bằng chứng, điều kiện tiên quyết và bàn giao. |
| Lộ trình triển khai | Cách chọn, sắp lịch và điều phối các bài học cho một chương trình; chỉ tham chiếu nội dung chuẩn. |
| Mã lộ trình (`run-slug`) | Định danh bền vững của một lộ trình và thư mục chuẩn tương ứng trong `ai-native-builder/runs/`. |
| Mã lượt chạy (`run-id`) | Định danh của một lượt thực thi workflow trong `.agents/workflow-runs/`; không phải tên hoặc định danh bền vững của lộ trình. |
| Buổi thực hành tích hợp (`studio`) | Khoảng thực hành có hướng dẫn trong một lộ trình, nơi học viên kết nối, phản biện hoặc chuyển giao các sản phẩm trung gian đã khóa và nhận phản hồi; không tự đưa vào năng lực mới chưa được khai báo. `studio` chỉ giữ nguyên trong tên tệp, nhãn định danh hoặc khối kỹ thuật. |
| Điểm kiểm tra | Điểm dừng có tiêu chí và bằng chứng để quyết định tiếp tục, học bổ sung hoặc chưa sẵn sàng. |
| Vòng lặp thực hành | Chu kỳ học viên thực hiện hành động, quan sát kết quả, kiểm chứng, sửa và ghi bằng chứng. |
| Sản phẩm trung gian của học viên | Đầu ra lưu được do học viên sở hữu và dùng để chứng minh một quyết định hoặc năng lực. |
| Bằng chứng | Dữ liệu, hành vi hoặc phần cụ thể của sản phẩm trung gian mà người kiểm định có thể quan sát để kiểm tra một khẳng định. |
| Khẳng định dễ lỗi thời | Mệnh đề phụ thuộc công cụ, phiên bản, giá, quyền hạn, chính sách, giao diện hoặc nguồn ngoài có thể thay đổi; phải có nguồn, phạm vi và điều kiện kiểm tra lại. |
| Sổ khẳng định | Bảng trong `references.md` sở hữu mệnh đề, loại, độ cập nhật cần thiết, tác động, rủi ro, phán quyết, phạm vi, vị trí sử dụng và điều kiện kiểm tra lại. |
| Sổ bằng chứng | Bảng trong `references.md` liệt kê từng nguồn thuận, nghịch hoặc làm hẹp một mã khẳng định; không thay sổ khẳng định. |
| Hàng đợi dẫn xuất | Danh sách tạm theo một lượt thực thi, được tạo từ các sổ khẳng định để điều phối việc kiểm tra lại; không phải nguồn chuẩn và không được dùng làm nguồn cho bài học. |
| Cờ chặn sử dụng | Biện pháp phòng ngừa tạm thời cho một phạm vi phụ thuộc khẳng định an toàn hoặc trọng yếu chưa đủ căn cứ; không tự là phán quyết rằng toàn bộ giáo trình thất bại. |
| Phạm vi kiểm chứng | Giới hạn của kết luận theo phiên bản, đối tượng học viên, hình thức tổ chức, môi trường và bằng chứng đã kiểm tra. |
| Bảng truy vết nội dung | Bảng ánh xạ yêu cầu trong bản định hướng sang nội dung, tệp hoặc phần chịu trách nhiệm và bằng chứng trước khi soạn bài. |
| Hợp đồng thiết kế học tập | Hồ sơ bàn giao trong một lượt chạy, do Người thiết kế lập trước khi soạn bài; cụ thể hóa sản phẩm trung gian, hành động học viên, bằng chứng, tiêu chí, phản hồi, thử lại và tình huống lỗi mà không thay bản định hướng thiết kế. |
| Sổ theo dõi tiến độ | Hồ sơ vận hành tại `.agents/workflow-runs/<run-id>/progress-tracker.md` theo dõi trạng thái thực thi, đầu vào, lỗi chặn và liên kết bằng chứng; không có thẩm quyền cấp trạng thái chất lượng. |
| Cổng kiểm tra cục bộ | Kiểm tra phạm vi hẹp trước khi một tệp hoặc đơn vị công việc được bàn giao; không thay thế kiểm định độc lập. |
| Cổng bắt buộc | Điều kiện bắt buộc trong `quality-gates.md`; một kết quả `Fail` hoặc `Not verified` chặn nghiệm thu. |
| Đặc tả năng lực | Mô tả năng lực cần chứng minh, hành vi quan sát được, bằng chứng và điều mà hoạt động đánh giá không được kết luận. |
| Hồ sơ quyết định giáo trình | Hồ sơ trong `.agents/decisions/` ghi xung đột, bằng chứng, lựa chọn và hệ quả quản trị; không thay thế nguồn chuẩn có thẩm quyền. |
| Nhật ký quyết định của học viên | Sản phẩm trung gian dùng để ghi lựa chọn sản phẩm hoặc kỹ thuật và lý do trong quá trình học. |
| Điểm kiểm tra trong lộ trình | Thời điểm thu bằng chứng trong một lộ trình triển khai. |
| Sẵn sàng sang mục tiêu tiếp theo | Kết luận về năng lực của học viên, không phải trạng thái chất lượng của giáo trình. |
| Bàn giao | Thao tác chuyển sản phẩm trung gian, trạng thái và trách nhiệm giữa các giai đoạn hoặc quy trình. |
| Trạng thái thực thi | Trạng thái của lượt quy trình hoặc gói công việc, như `Queued`, `Awaiting input` hoặc `Ready for handoff`; không phải phán quyết chất lượng. |
| `Needs revision` | Chưa đủ điều kiện nghiệm thu hoặc chưa có kiểm định độc lập. |
| `Pilot-ready` | Đã qua kiểm định độc lập, toàn bộ cổng bắt buộc `Pass`, không có điểm `0` và tổng ít nhất `11/16`. |
| `Release-ready` | Đáp ứng `Pilot-ready`, đạt ít nhất `13/16` và không còn thay đổi bắt buộc đã biết. |
| `Validated` | Đáp ứng `Release-ready` và có bằng chứng dạy thử phù hợp về kết quả, độ rõ ràng và thời lượng. |
