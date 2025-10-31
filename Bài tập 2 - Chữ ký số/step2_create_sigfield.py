from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import (
    NameObject,
    DictionaryObject,
    NumberObject,
    ByteStringObject,
    ArrayObject
)

# === CẤU HÌNH ===
input_pdf = "original.pdf"                  # file PDF gốc của bạn
output_pdf = "original_with_sigfield.pdf"   # file có signature field

# === 1️⃣ ĐỌC FILE GỐC ===
reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# === 2️⃣ TẠO DICTIONARY CHO FIELD CHỮ KÝ ===
sig_field = DictionaryObject()
sig_field.update({
    NameObject("/Type"): NameObject("/Sig"),
    NameObject("/Filter"): NameObject("/Adobe.PPKLite"),
    NameObject("/SubFilter"): NameObject("/adbe.pkcs7.detached"),
    # Vùng Contents 8192 bytes (8192*2 hex ký tự)
    NameObject("/Contents"): ByteStringObject(b"\x00" * 8192),
    # ByteRange placeholder (sẽ cập nhật ở bước 3)
    NameObject("/ByteRange"): ArrayObject([
        NumberObject(0),
        NumberObject(0),
        NumberObject(0),
        NumberObject(0)
    ])
})

# === 3️⃣ THÊM FIELD VÀO ACROFORM ===
sig_field_ref = writer._add_object(sig_field)

acro_form = DictionaryObject()
acro_form.update({
    NameObject("/Fields"): ArrayObject([sig_field_ref])
})
writer._root_object.update({
    NameObject("/AcroForm"): acro_form
})

# === 4️⃣ GHI RA FILE ===
with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"✅ Đã tạo file: {output_pdf}")
print("File này có vùng /Contents (8192 bytes) và /ByteRange placeholder.")

