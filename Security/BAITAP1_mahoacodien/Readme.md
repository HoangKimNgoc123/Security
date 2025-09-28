## SINH VIÊN: HOÀNG KIM NGỌC - K225480106053 - K58KTP
### BÀI TẬP MÔN: An toàn và bảo mật thông tin 
### BÀI TẬP 1: TÌM HIỂU CÁC PHƯƠNG PHÁP MÃ HOÁ CỔ ĐIỂN 
1. Caesar
2. Affine
3. Hoán vị
4. Vigenère
5. Playfair

**Với mỗi phương pháp, hãy tìm hiểu:**
1. Tên gọi
2. Thuật toán mã hoá, thuật toán giải mã
3. Không gian khóa
4. Cách phá mã (mà không cần khoá)
5. Cài đặt thuật toán mã hoá và giải mã bằng code C++ và bằng html+css+javascript

### BÀI LÀM 
#### Thuật toán mã hóa Caesar
1. Mô tả bài toán
     - Thuật toán mã hóa Caesar được thực hiện bằng cách thay thế một ký tự bằng 1 ký tự khác cách nó k bước trong bảng chữ cái để tạo thành ký tự mới.
     - Mã hóa: = (P + k) mod 26
        + Ví dụ key = 3:  a → d, b → e, c → f, …, x → a, y → b, z → c.
     - Giải mã: P = (C - k mod 26)
        + Dịch ngược lại k vị trí.
     - Không gian khóa: 25 khóa có nghĩa (dịch 0 thì vô nghĩa).
     - Cách phá:
        + Thử brute-force tất cả 25 khóa.
        + Hoặc dùng phân tích tần suất.
2. Cài đặt thuật toán mã hoá và giải mã bằng code C++

   <img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/3d246755-feae-42e0-bcd1-0c88e08131a6" />

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a08ad858-3fc2-44c4-be13-c05367542b44" />

3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript
   - Khi mã hóa:
     
  <img width="1916" height="1079" alt="image" src="https://github.com/user-attachments/assets/a8dde8c9-0fe7-4eff-b888-1352a3cb27d7" />

    - Khi giải mã:

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ff2b016d-e34c-47b0-8982-0ed217b8db06" />


#### Thuật toán mã hóa Affine Cipher
1. Mô tả thuật toán
    - Tên gọi: Mã Affine (tuyến tính).
    - Ý tưởng: Giống Caesar nhưng thêm nhân và cộng:
    - Công thức: C = (a*P + b) mod 26.
        + Với a phải nguyên tố cùng nhau với 26 (để đảo ngược được).
    - Giải mã: P = a⁻¹ * (C - b) mod 26 (với a⁻¹ là nghịch đảo modulo 26 của a).
    - Không gian khóa: 312 khóa khả thi.
    - Cách phá:
          + Brute-force 312 khóa (vẫn nhỏ).
          + Biết 2 cặp (plaintext, ciphertext) thì giải được hệ và tìm (a,b).
2. Cài đặt thuật toán mã hoá và giải mã bằng code C++


3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript
