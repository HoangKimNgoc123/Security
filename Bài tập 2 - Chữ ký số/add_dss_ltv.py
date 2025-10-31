import pikepdf
from pikepdf import Dictionary, Name, Array, Stream
from pathlib import Path
import base64, re

def load_der(path):
    b = Path(path).read_bytes()
    if b.startswith(b"-----BEGIN"):
        pem = b.decode()
        matches = re.findall(
            r"-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----",
            pem, re.S
        )
        ders = [base64.b64decode(m.strip()) for m in matches]
        return ders
    return [b]

# ---- Cấu hình ----
pdf_in = Path("step8_visible_signature_center.pdf")
pdf_out = Path("step9_with_dss.pdf")
signer_cert = Path("hoangkimngoc_cert.pem")
chain_file = Path("chain.pem")

# ---- Load certs ----
certs = []
for f in [signer_cert, chain_file]:
    if f.exists():
        certs.extend(load_der(f))

# ---- Mở PDF ----
pdf = pikepdf.Pdf.open(str(pdf_in))

# ---- DSS ----
cert_streams = Array([Stream(pdf, c) for c in certs])
dss = Dictionary()
dss[Name("/Certs")] = cert_streams

vri_entry = Dictionary({"/Certs": cert_streams})
vri = Dictionary({"/Signature1": vri_entry})
dss[Name("/VRI")] = vri

# ---- Gắn vào Catalog ----
root = getattr(pdf, "root", None) or pdf.Root
root[Name("/DSS")] = dss

# ---- Lưu (KHÔNG incremental, để đảm bảo chạy chắc chắn) ----
pdf.save(str(pdf_out))  # hoặc pdf._quick_save(str(pdf_out))

print("✅ Đã thêm DSS (LTV structure) thành công vào:", pdf_out)
print("⚠️ Lưu ý: Bản này ghi toàn bộ file, nên chữ ký cũ bị vô hiệu (dành cho minh họa LTV).")
