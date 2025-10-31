import re, binascii
from pikepdf import Pdf, Dictionary, Name, Array, String, Stream

pdf_in = "step3_with_ByteRange.pdf"
sig_der = "signature.p7s"
pdf_out = "step7_signed_incremental.pdf"

with open(pdf_in, "rb") as f:
    pdf_data = f.read()

# Tìm ByteRange
m = re.search(rb"/ByteRange\s*\[\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*\]", pdf_data)
if not m:
    raise ValueError("Không tìm thấy /ByteRange!")
br = [int(m.group(i)) for i in range(1, 5)]
print(f"ByteRange hiện tại: {br}")

# Đọc chữ ký PKCS#7
sig_data = open(sig_der, "rb").read()
sig_hex = binascii.hexlify(sig_data).upper()
sig_hex_str = "<" + sig_hex.decode("ascii") + ">"

# Mở PDF
pdf = Pdf.open(pdf_in)

# Tạo stream chứa chữ ký
sig_stream = Stream(pdf, sig_hex_str.encode("ascii"))
sig_stream["/Type"] = Name("/Sig")

# Lấy trang đầu tiên
page = pdf.pages[0]

# Tạo /Annots nếu chưa có
if "/Annots" not in page:
    page["/Annots"] = pdf.make_indirect(Array())

# Tạo annotation (vùng ký)
annot = Dictionary()
annot[Name("/Type")] = Name("/Annot")
annot[Name("/Subtype")] = Name("/Widget")
annot[Name("/FT")] = Name("/Sig")
annot[Name("/T")] = String("HoangKimNgocSig")
annot[Name("/Rect")] = Array([100, 100, 300, 150])
annot[Name("/V")] = sig_stream

page["/Annots"].append(pdf.make_indirect(annot))

# Lưu file mới (không incremental=True nữa)
pdf.save(pdf_out)

print(f"✅ Đã thêm chữ ký số vào {pdf_out}")
