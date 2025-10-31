import pikepdf
from pikepdf import Pdf
import inspect

print("🔹 PikePDF version:", pikepdf.__version__)
print("🔹 Pdf object class:", Pdf)
print("🔹 Pdf defined in:", inspect.getfile(Pdf))

print("\n--- Available methods on Pdf ---")
for name in dir(Pdf):
    if "save" in name.lower():
        print("  ", name)

print("\n--- Help on Pdf.save ---")
try:
    print(inspect.signature(Pdf.save))
except Exception as e:
    print("Cannot inspect Pdf.save:", e)

print("\n--- Does Pdf have save_incremental? ---", hasattr(Pdf, "save_incremental"))
