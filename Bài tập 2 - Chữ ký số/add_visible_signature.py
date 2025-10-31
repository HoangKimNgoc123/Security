import asyncio
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.sign.validation.dss import async_add_validation_info
from pyhanko_certvalidator import ValidationContext

input_pdf = "step8_visible_signature_center.pdf"
output_pdf = "step9_LTV.pdf"

# Context cho phép tải OCSP/CRL (có mạng)
vc = ValidationContext(revocation_mode='soft-fail', allow_fetching=True)

async def main():
    # Đọc file PDF đã ký
    with open(input_pdf, "rb") as inf:
        reader = PdfFileReader(inf)
        # Lấy chữ ký đầu tiên trong PDF
        sig = next(reader.embedded_signatures)
        # Xác thực chữ ký để lấy thông tin chứng chỉ, hash...
        await validate_pdf_signature(sig, vc)
        # Thêm LTV (OCSP, CRL, Cert chain) vào PDF
        await async_add_validation_info(sig, vc, output=output_pdf)
    print(f"✅ Đã thêm LTV (DSS + VRI) vào {output_pdf}")

# Chạy asyncio
asyncio.run(main())
