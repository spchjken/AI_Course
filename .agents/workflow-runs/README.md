# Hồ sơ thực thi quy trình

Mỗi thư mục con lưu bằng chứng điều phối và các hồ sơ bàn giao vận hành của một lượt chạy theo `.agents/workflows/agent-dispatch-protocol.md`. Một workflow có thể yêu cầu thêm sổ tiến độ, hợp đồng thiết kế hoặc bảng truy vết trong chính thư mục lượt chạy; workflow đó phải chỉ rõ tên tệp, bên chịu trách nhiệm và vòng đời của chúng.

Tên thư mục dùng dạng `<YYYYMMDD-HHMM>-<workflow>-<scope>`. Điều phối viên là bên duy nhất ghi `orchestration-log.md`; tác nhân con chỉ trả đầu ra qua tệp thuộc phạm vi hoặc thông điệp kết quả.

Hồ sơ thực thi không phải nguồn chuẩn của giáo trình và không thay hồ sơ quyết định. Chúng là điểm bàn giao bền vững cho đúng lượt chạy, không phải template hoặc nguồn để tự suy ra yêu cầu mới của bài học. Không lưu thông tin bí mật, dữ liệu cá nhân không cần thiết hoặc toàn bộ hội thoại vào đây.
