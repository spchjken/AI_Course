# Chương trình “AI-native Builder” cho người mới

## Tóm tắt

Chương trình có hai phiên bản, đều dành cho người mới chỉ dùng ChatGPT trên web. Trọng tâm là dùng AI hiệu quả để xây sản phẩm, không đào tạo lý thuyết máy học hàn lâm và không bắt học viên học một ngôn ngữ lập trình trước.

- **Chương trình khám phá:** 3 buổi × 3 giờ; mỗi học viên hoàn thành một nguyên mẫu cá nhân và trình diễn nội bộ có kiểm chứng cơ bản.
- **Lộ trình 1-1 đầy đủ:** 8 tuần, **20 buổi / 32 giờ**, gồm 16 buổi học (90 phút) và 4 buổi thực hành tích hợp có kiểm định (120 phút).
- Công cụ thực hành chính: **Codex trong VS Code** và **Antigravity IDE**. Chương trình so sánh trò chuyện trên web, tác nhân AI trong IDE, nền tảng tác nhân AI và CLI; CLI chỉ là lựa chọn bổ sung sau khóa học.
- Bộ công nghệ minh họa: HTML/CSS/JavaScript. Dự án tổng kết có thể dùng phần máy chủ Node hoặc kiến trúc không máy chủ khi cần bảo vệ khóa API hoặc gọi mô hình.

## Kết quả đầu ra

Học viên có thể biến một ý tưởng thành ứng dụng và làm việc với AI theo vòng lặp:

`Orientation → Specification → System design → Harness → Agent control → Verification → Extension → Release → Reflection`

Hồ sơ năng lực gồm:

- 2 dự án nhỏ, mỗi dự án chứng minh một kỹ năng cụ thể.
- 1 ứng dụng web tổng kết theo mục tiêu cá nhân, có kho mã nguồn GitHub, README, bản trình diễn đã triển khai, nhật ký quyết định và yêu cầu cho AI, cùng video hoặc phần thuyết minh ngắn.
- Học viên phải tự giải thích sơ đồ hệ thống, kiểm chứng các quyết định quan trọng và trình bày bằng chứng về quá trình làm việc, thay vì chỉ sao chép đầu ra của AI. Điểm chạm với mã nguồn được tăng dần xuyên suốt dự án, không tách thành một chương lập trình riêng.

## Chương trình khám phá 3 buổi

1. **Định hướng và đặc tả:** dùng AI để làm rõ vấn đề, người dùng, phạm vi, luồng thao tác và tiêu chí hoàn thành.
2. **Khung hệ thống và bộ khung kiểm soát:** vẽ sơ đồ hệ thống bằng ngôn ngữ thường; tạo không gian làm việc, chỉ dẫn tối thiểu, nhật ký quyết định và kế hoạch xây dựng đầu tiên.
3. **Xây dựng, kiểm chứng và trình diễn nội bộ:** điều khiển tác nhân AI theo tác vụ nhỏ, kiểm chứng hành vi theo đặc tả, ghi bằng chứng và trình bày nguyên mẫu; không cam kết triển khai công khai.

## Lộ trình 1-1 gồm 20 buổi

- **Tuần 1 — Định hướng và đặc tả:** dùng AI như đối tác đối thoại; lập bản đồ công cụ; chọn vấn đề và viết bản định hướng cùng bản đặc tả sản phẩm. Buổi thực hành tích hợp 1 chốt phạm vi, tiêu chí thành công và bảng tiêu chí cho dự án tổng kết.
- **Tuần 2 — Khung hệ thống và bộ khung kiểm soát tối thiểu:** xây sơ đồ hệ thống bằng ngôn ngữ thường, chọn lát cắt xây dựng đầu tiên, tạo không gian làm việc và kho mã nguồn, dựng xương sống tri thức dự án tối thiểu (điểm vào, nguồn chuẩn, provenance và nhật ký quyết định), viết chỉ dẫn cơ bản và thực hiện vòng lặp lập kế hoạch–xây dựng–kiểm chứng.
- **Tuần 3 — Điều khiển tác nhân AI và kiểm chứng:** viết yêu cầu có ngữ cảnh và ràng buộc, lập kế hoạch trước, chia tác vụ, phản hồi bằng bằng chứng, kiểm tra theo đặc tả và phục hồi khi sai. Buổi thực hành tích hợp 2 kiểm định dự án nhỏ thứ nhất.
- **Tuần 4 — Mở rộng bằng công cụ:** làm việc với API, thông tin bí mật, cơ chế gọi công cụ, MCP, quyền hạn, bước phê duyệt và chi phí.
- **Tuần 5 — Quản lý và truy xuất ngữ cảnh:** tìm kiếm theo tác vụ trên nền tri thức dự án đã tích lũy, tạo và kiểm thử gói ngữ cảnh, nén có truy nguồn, làm mới thông tin lỗi thời và quyết định khi nào tệp/chỉ mục đủ, khi nào mới cần RAG hoặc chế độ xem dạng đồ thị. Buổi thực hành tích hợp 3 kiểm định dự án nhỏ thứ hai.
- **Tuần 6 — Nâng cấp bộ khung kiểm soát:** rút kinh nghiệm từ dự án để tạo quy tắc, kỹ năng và quy trình tái sử dụng; chỉ tự động hóa metadata, chỉ mục hoặc truy xuất nâng cao khi có mẫu hình lặp lại và bằng chứng trước/sau; dùng Git, phần thay đổi, công cụ trình duyệt và điểm chạm mã nguồn đúng lúc để kiểm định thay đổi của tác nhân AI.
- **Tuần 7 — Chất lượng và quyền sở hữu:** đánh giá đầu ra AI, kiểm thử theo rủi ro, xử lý quyền riêng tư, bản quyền, thông tin bí mật, lỗi môi trường và chuẩn bị phát hành. Buổi thực hành tích hợp 4 hoàn thiện dự án tổng kết.
- **Tuần 8 — Phát hành và trình bày năng lực:** triển khai sản phẩm, hoàn thiện README, bản trình diễn, sơ đồ hệ thống, bằng chứng quá trình và câu chuyện hồ sơ năng lực/CV.

Bốn buổi thực hành tích hợp dùng để kiểm định cá nhân, chốt phạm vi, xử lý lỗi chặn, kiểm tra sản phẩm trung gian và phát triển dự án tổng kết; không dùng để giảng lại lý thuyết.

## Đánh giá và vận hành

- Mỗi buổi tạo một sản phẩm trung gian nhỏ: bản định hướng hoặc đặc tả sản phẩm, sơ đồ hệ thống, kế hoạch cho tác nhân AI, nhật ký quyết định, thành phần của bộ khung kiểm soát, bằng chứng kiểm thử hoặc bản cập nhật README.
- Bảng tiêu chí tổng thể: định hướng/đặc tả/sơ đồ hệ thống (25%), điều khiển tác nhân AI và quản lý ngữ cảnh (25%), kiểm chứng/bộ khung kiểm soát/công cụ an toàn (30%), sản phẩm/triển khai/trình bày (20%).
- Hỗ trợ nhắn tin không giới hạn theo nguyên tắc sử dụng hợp lý: hướng dẫn, kiểm định và gỡ lỗi chặn; không làm hộ bài. Mặc định phản hồi trong một ngày làm việc.
- Có lộ trình dùng gói miễn phí theo mặc định. API hoặc gói AI trả phí là lựa chọn bổ sung và phải được báo trước theo nhu cầu dự án tổng kết.
- Không đi sâu vào toán, huấn luyện mô hình hoặc khung công nghệ máy học; các nội dung đó thuộc nhánh học tiếp sau khóa.

## Khung tham khảo

Các thành phần được chọn lọc từ những chương trình và tài liệu sau:

- [DeepLearning.AI — AI Python for Beginners](https://www.deeplearning.ai/courses/ai-python-for-beginners): dự án thực hành từ ngày đầu và dùng AI để học, gỡ lỗi.
- [Anthropic Academy — Claude Code 101 và Claude Code in Action](https://academy.claude.com/courses): quy trình dùng tác nhân lập trình, duy trì phiên làm việc dài và kiểm chứng kết quả.
- [GitHub Skills](https://skills.github.com/): Git, PR, Copilot, MCP và bảo mật; đặc biệt là cách chia bài thành các điểm kiểm tra nhỏ và làm việc trên kho mã nguồn thật.
- [Anthropic Prompt Engineering Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables): cấu trúc yêu cầu cho AI, ngữ cảnh, công cụ và hệ thống tác nhân.
- [Full Stack Deep Learning — LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/): yêu cầu cho AI, trải nghiệm người dùng, triển khai và vận hành ứng dụng LLM.
- [Microsoft AI for Beginners](https://github.com/microsoft/AI-For-Beginners): tham khảo cấu trúc bài học, bài thực hành, câu hỏi kiểm tra và AI có trách nhiệm; phần máy học chuyên sâu được chủ động loại khỏi khóa này.

## Giả định mặc định

Chương trình dạy bằng tiếng Việt theo hình thức 1-1. Học viên có máy tính xách tay và đã dùng công cụ trò chuyện AI trên web; không yêu cầu kiến thức lập trình trước đó. Nội dung giữ nguyên lý chung để không phụ thuộc một hãng, nhưng thực hành sâu trên Codex trong VS Code và Antigravity IDE. Cấu trúc nguồn bài giảng và 11 mục tiêu chính được quản lý trong `curriculum-content-architecture.md`.
