# Derived context index tools

Thư mục này chứa bộ công cụ tạo và giữ derived index của repository. Index là
ảnh cấu trúc có thể tái tạo, không phải nguồn chuẩn và không thay thế nội dung
gốc. Mặc định các file cache và lock cục bộ nằm ở `.context-index-cache.json`
và `.context-index-lock` (có thể đổi bằng CLI); file index được sinh ở
`.agents/generated/context-index.json` và được commit để worker khác có thể sử
dụng ngay.

## Invariant

Mỗi entry giữ hai fingerprint:

```text
content_hash = SHA256(normalized UTF-8 content)
entry_hash   = SHA256(content_hash + NUL + normalized repository-relative path)
```

`content_hash` nhận diện nội dung; `entry_hash` nhận diện cặp nội dung–path.
Vì vậy move nguyên vẹn có cùng `content_hash` nhưng có `entry_hash` mới, còn
move kèm chỉnh sửa được báo như delete + create. Khi có nhiều file trùng hash,
tool không đoán cặp move; trạng thái index cuối vẫn đúng.

Không lưu `keywords` trong index. Lexical search đọc file hiện tại qua Python
stdlib và có thể dùng `rg` nếu máy có cài để lọc nhanh hơn. Classification,
authority và `default_search` là metadata cấu trúc; `.agents/workflow-runs/**`
được index với authority `operational` nhưng bị loại khỏi tìm kiếm mặc định.

## Commands

Chạy từ root repository:

```powershell
python .agents/indexing/sync_index.py --full --report .agents/workflow-runs/<run>/index-report.json
python .agents/indexing/sync_index.py --check
python .agents/indexing/sync_index.py --update
python .agents/indexing/search_index.py "quality gate" --authority canonical
python .agents/indexing/build_context_package.py `
  --query "derived index" `
  --task "review-index" `
  --role reviewer `
  --output .agents/workflow-runs/<run>/context-package.json
```

`--check` không ghi file, hash lại toàn bộ nguồn và trả exit code `2` khi index
đã stale (kể cả trường hợp metadata file không đổi). `--update` dùng cache stat
hash để bỏ qua file không đổi; `--full` bỏ qua cache. Output
JSON được sort và ghi atomically, không chứa timestamp nên có thể kiểm tra tính
lặp lại. Scheduler và hook vào workflow chưa thuộc phạm vi pha này.

## Scope an toàn

Config chỉ cho phép file UTF-8 thuộc include globs và bỏ qua `.git/`, generated
index, cache, binary-like extensions và symlink. Tool không tự sửa canonical
source. Context package chỉ chứa tham chiếu, hash và snippet; worker vẫn phải
đọc source được allowlist và tuân thủ ownership của workflow.
