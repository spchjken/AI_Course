# Các cổng chất lượng

## Khi nào áp dụng

Áp dụng trước khi tuyên bố hoàn thành một bài học, sản phẩm trung gian, lộ trình hoặc thay đổi đáng kể trong kiến trúc giáo trình.

## Nguyên tắc kiểm chứng

- Không tự đánh dấu `Pass` nếu không trỏ được tới bằng chứng cụ thể trong tệp, hoạt động hoặc sản phẩm trung gian.
- Kiểm định phải đánh giá hành vi học tập dự kiến, không chỉ kiểm tra sự tồn tại của tiêu đề.
- Cổng bắt buộc thất bại luôn chặn nghiệm thu, bất kể điểm chất lượng.
- Dùng `Fail` khi người kiểm định đã kiểm tra và thấy bằng chứng bắt buộc không tồn tại hoặc không đạt điều kiện.
- Dùng `Not verified` khi bằng chứng có thể tồn tại nhưng người kiểm định không truy cập được, hoặc chỉ có thể quan sát trong đợt dạy thử hay lúc vận hành. Không suy diễn thành `Pass` hoặc mô tả đây là lỗi nội dung nếu chưa đủ căn cứ.

## Tầng A — Các cổng bắt buộc

Tên cổng là mã định danh chuẩn; phần mô tả dùng tiếng Việt.

| Cổng | Điều kiện đạt |
|---|---|
| `Alignment` | Nội dung phục vụ đúng mục tiêu `gNN`, phù hợp kế hoạch và kiến trúc nội dung. |
| `Observable outcome` | Có hành vi học viên thực hiện được và bằng chứng quan sát được. |
| `Prerequisite` | Mọi kiến thức hoặc năng lực cần thiết đã được thiết lập hoặc cung cấp trong bài. |
| `Learner ownership` | Học viên phải đưa ra ít nhất một quyết định hoặc phán đoán quan trọng. |
| `Evidence` | Có sản phẩm trung gian và cách kiểm tra sản phẩm đó để chứng minh kết quả. |
| `Verification` | Có cách phát hiện đầu ra AI sai, thiếu, không chạy hoặc vượt phạm vi. |
| `Safety` | Rủi ro liên quan dữ liệu, thông tin bí mật, quyền hạn, chi phí và hoàn tác đã được xử lý phù hợp. |
| `Consistency` | Không xung đột với nguồn chuẩn và không sao chép nội dung bài học sang nơi khác. |

Kết quả mỗi cổng chỉ nhận một trong ba giá trị: `Pass`, `Fail`, `Not verified`.

Mỗi kết quả `Not verified` phải ghi nguyên nhân, bằng chứng hoặc quyền truy cập còn thiếu, người hoặc bước chịu trách nhiệm cung cấp và phạm vi cần kiểm định lại. Cả `Fail` và `Not verified` đều chặn nghiệm thu, nhưng yêu cầu khắc phục khác nhau.

## Tầng B — Điểm chất lượng

Chấm mỗi tiêu chí từ 0 đến 2:

- `0`: thiếu hoặc vi phạm.
- `1`: có nhưng mơ hồ, yếu hoặc khó áp dụng.
- `2`: rõ ràng, phù hợp và có thể thực hiện.

Tên tiêu chí là mã định danh chuẩn; phần mô tả dùng tiếng Việt.

| Tiêu chí | Nội dung đánh giá |
|---|---|
| `Beginner clarity` | Người mới chỉ quen công cụ trò chuyện AI trên web có thể theo được. |
| `Practice quality` | Học viên thực sự làm, quan sát và ra quyết định. |
| `AI-native interaction` | AI được dùng như cộng sự xuyên suốt thay vì nút tạo đáp án. |
| `Code contact` | Điểm chạm với mã nguồn xuất hiện đúng lúc, đúng mức và có mục đích. |
| `Time feasibility` | Nội dung và sản phẩm trung gian có thể hoàn thành trong thời lượng dự kiến. |
| `Reusability` | Dùng nguồn chung và không tạo nội dung trùng lặp. |
| `Currency` | Thông tin phụ thuộc công cụ hoặc API có nguồn và ngày kiểm tra phù hợp. |
| `Progression` | Bài sử dụng đúng điều kiện tiên quyết và chuẩn bị được cho bước tiếp theo. |

## Giới hạn của tự đánh giá

- Người soạn được phép chạy cổng kiểm tra cục bộ và tự kiểm tra, nhưng không được là người duy nhất cấp `Pass` hoặc nâng trạng thái chất lượng cho nội dung mình viết.
- `Pilot-ready`, `Release-ready` và `Validated` cần một lượt kiểm định độc lập bởi người khác hoặc một phiên tác nhân AI khác, đọc trực tiếp đầu ra và bằng chứng thay vì kế thừa kết luận của người soạn.
- Khi chưa có kiểm định độc lập, nội dung giữ trạng thái `Needs revision`; tự đánh giá chỉ là bước kiểm tra trước, không phải nghiệm thu.
- `Beginner clarity` và `Time feasibility` không được chấm `2` nếu chưa có bằng chứng từ một buổi dạy thử với học viên thuộc đúng đối tượng mục tiêu.
- Nhận định của tác nhân AI hoặc giảng viên trước dạy thử chỉ đủ để chấm tối đa `1` cho hai tiêu chí này.
- Điểm chất lượng không thể bù cho cổng bắt buộc thất bại.

## Tầng C — Báo cáo có bằng chứng

Lưu kết quả trong `review.md` của bài học hoặc tài liệu kiểm định tương ứng. Khối dưới đây là cấu trúc tệp kỹ thuật nên dùng tiếng Anh nhất quán:

```md
# Quality review

## Hard gates

| Gate | Verdict | Evidence | Cause or issue | Action and re-review scope |
|---|---|---|---|---|

## Quality score

| Criterion | Score | Evidence | Issue or correction |
|---|---:|---|---|

## Conclusion

- Total score: X/16
- Hard gates: Pass/Fail/Not verified
- Status: Needs revision/Pilot-ready/Release-ready/Validated
- Pilot evidence:
- Independent reviewer:
- Evidence or access limitations:
- Remaining mandatory corrections:
```

## Trạng thái chất lượng

| Trạng thái | Điều kiện |
|---|---|
| `Needs revision` | Có cổng bắt buộc `Fail` hoặc `Not verified`, có tiêu chí bằng `0`, hoặc tổng điểm dưới `11/16`. |
| `Pilot-ready` | Có kiểm định độc lập; tất cả cổng bắt buộc là `Pass`, không có điểm `0`, tổng điểm ít nhất `11/16`. |
| `Release-ready` | Đáp ứng `Pilot-ready`, tổng điểm ít nhất `13/16`, không còn thay đổi bắt buộc đã biết. |
| `Validated` | Đáp ứng `Release-ready`, đã dạy thử với học viên đúng đối tượng và có bằng chứng thực tế về kết quả, độ rõ ràng và thời lượng. |

## Tiêu chuẩn nghiệm thu

- Nội dung có thể đưa vào dạy thử từ trạng thái `Pilot-ready`.
- Không mô tả nội dung là sẵn sàng phát hành khi chưa đạt `Release-ready`.
- Không dùng trạng thái `Validated` nếu thiếu dữ liệu dạy thử hoặc dữ liệu đến từ người không thuộc đối tượng học viên mục tiêu.
- Mọi trạng thái phải có bằng chứng cụ thể cho các cổng bắt buộc, điểm số và vấn đề còn lại.
