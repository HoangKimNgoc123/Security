import re, hashlib

pdf_path = "step3_with_ByteRange.pdf"

# Đọc toàn bộ file PDF vào bộ nhớ
with open(pdf_path, "rb") as f:
    data = f.read()

# Tìm dòng /ByteRange [...]
m = re.search(rb"/ByteRange\s*\[\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*\]", data)
if not m:
    raise ValueError("Không tìm thấy /ByteRange trong PDF!")

# Lấy 4 giá trị trong ByteRange
br = [int(m.group(i)) for i in range(1, 5)]
print("ByteRange:", br)

# Tách hai vùng dữ liệu thực sự cần hash
part1 = data[br[0] : br[0] + br[1]]
part2 = data[br[2] : br[2] + br[3]]
to_hash = part1 + part2

# --- SHA-256 ---
hash256 = hashlib.sha256(to_hash).hexdigest()
print("SHA-256:", hash256)

# --- (tuỳ chọn) SHA-512 ---
hash512 = hashlib.sha512(to_hash).hexdigest()
print("SHA-512:", hash512)

# Ghi phần dữ liệu được ký ra file để dùng cho bước 5 (tạo PKCS#7)
with open("to_sign.bin", "wb") as f:
    f.write(to_hash)

print("Đã ghi dữ liệu cần ký vào to_sign.bin")
