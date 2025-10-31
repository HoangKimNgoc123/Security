##BÀI TẬP 2- CHỮ KÝ SỐ VỚI PDF

###CÁC BƯỚC TẠO CHỮ KÝ SỐ
1. Chuẩn bị file PDF gốc: original.pdf
2. Tạo Signature field (AcroForm), reserve vùng /Contents (8192 bytes).
   - Cài Python + pip:
     
    <img width="970" height="185" alt="image" src="https://github.com/user-attachments/assets/c3b95fbf-727f-4ce9-9df0-439edb11e310" />

    <img width="915" height="49" alt="image" src="https://github.com/user-attachments/assets/85787c0f-5a38-4a00-9090-8eaa98a45dea" />

   - Tạo private key:

     <img width="1488" height="267" alt="image" src="https://github.com/user-attachments/assets/e4ff8895-8027-4ecb-a367-4014e0292345" />

   - Tạo cert tự ký (1 năm):

     <img width="1481" height="256" alt="image" src="https://github.com/user-attachments/assets/295655c2-ea31-40cd-b4ca-e0a330c927a1" />

   - Tạo PKCS#12 chứa key+cert:

     <img width="1483" height="151" alt="image" src="https://github.com/user-attachments/assets/57db77bf-eb3a-4931-99a0-b3d1cffa3d83" />

   - Tạo Signature Field:

    <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8f89c74b-380f-49ce-9b17-adea13eae3b8" />

   - Cài thư viện Pyhanko:

     <img width="818" height="248" alt="image" src="https://github.com/user-attachments/assets/5f62e168-f2f8-4676-ad67-e22cddc424ce" />

3. Xác định /ByteRange:

      <img width="1919" height="998" alt="image" src="https://github.com/user-attachments/assets/bb70853f-8155-47b0-9971-c536dc2e8661" />

4. Tính hash (SHA-256/512) trên vùng ByteRange.

     <img width="1885" height="1062" alt="image" src="https://github.com/user-attachments/assets/c81f60f4-0535-4380-b6b5-33d442fc93a0" />

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/0220709b-4df6-4e89-817b-cc950472cb27" />

     <img width="478" height="631" alt="image" src="https://github.com/user-attachments/assets/45431213-eba6-4980-b681-7e9147ca26c0" />

     <img width="472" height="629" alt="image" src="https://github.com/user-attachments/assets/a5a705b4-cb09-4e5c-8240-969a63ffebe5" />
