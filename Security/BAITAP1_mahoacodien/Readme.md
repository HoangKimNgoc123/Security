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

   <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f1c6bb47-fe1e-471a-82c1-040aca3acfe3" />

   <img width="1472" height="760" alt="image" src="https://github.com/user-attachments/assets/59a95992-25a8-4716-9a6d-1b7e058f251f" />

3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript
     
   <img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/7d5d6828-5980-4637-b1c5-d74623a7ca12" />

   <img width="1911" height="1079" alt="image" src="https://github.com/user-attachments/assets/0261b25a-f65a-46f2-a523-a1c7641f62d8" />

#### Thuật toán mã hóa Hoán vị (Transposition Cipher)
1. Mô tả thuật toán
     - Tên gọi: Mã hóa Hoán vị.
     - Ý tưởng: Không thay đổi chữ cái, chỉ đổi chỗ.
            + Viết plaintext vào bảng nhiều cột.
            + Đọc theo thứ tự cột dựa trên khóa.
     - Ví dụ:
            + Key = “ZEBRA” → sắp xếp thành thứ tự cột 3-2-5-1-4.
            + Viết vào hàng rồi đọc theo cột.
     - Giải mã: Sắp xếp cột lại đúng vị trí, đọc theo hàng.
     - Không gian khóa: n! (n = độ dài khóa).
     - Cách phá:
            + Thử các hoán vị nhỏ.
            + Với khóa dài → dùng heuristic (đánh giá văn bản theo tần suất từ).
2. Cài đặt thuật toán mã hoá và giải mã bằng code C++

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3cf83c9d-be73-4a2d-82b3-69f12420a8fc" />

     <img width="1477" height="753" alt="image" src="https://github.com/user-attachments/assets/0aa3db65-dda7-4ea2-b8d6-91711112a042" />

3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript

     <img width="1873" height="1079" alt="image" src="https://github.com/user-attachments/assets/a14f34fb-bd27-4b2b-ba21-1aed2f7fd286" />

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f50c585c-c86d-4b88-afe8-0a9e14a17ace" />

#### Thuật toán mã hóa Vigenère Cipher 
1. Mô tả thuật toán
     - Tên gọi: Mã hóa Vigenère 
     - Ý tưởng: Poly-alphabetic substitution — thay đổi bảng Caesar theo chu kỳ.
          + Key là một từ, ví dụ “LEMON”.
          + Plaintext “ATTACKATDAWN” → lặp key thành “LEMONLEMONLE”.
     - Mã hóa: mỗi chữ dùng dịch Caesar theo chữ key tương ứng.
     - Giải mã: dịch ngược lại với cùng key.
     - Không gian khóa: 26^m (m = độ dài key).
     - Cách phá:
          + Kasiski: tìm khoảng cách lặp → đoán độ dài key.
          + Friedman test (Index of Coincidence) → ước lượng độ dài key.
          + Sau khi biết m, chia bản mã thành m dãy → giải như Caesar bằng phân tích tần suất
2. Cài đặt thuật toán mã hoá và giải mã bằng code C++

     <img width="1915" height="1079" alt="image" src="https://github.com/user-attachments/assets/48c22a31-bf33-4cb1-8ae2-9900c92078d2" />

     <img width="1488" height="755" alt="image" src="https://github.com/user-attachments/assets/098b9827-1d7c-47c3-8006-55db2fb445ed" />

3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript

     <img width="1878" height="1078" alt="image" src="https://github.com/user-attachments/assets/bf5889f7-b73e-4962-b167-b8b2cde48e2c" />

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/4f583926-6080-4705-824c-77874cb912f8" />

#### Thuật toán mã hóa Playfair Cipher
 1. Mô tả thuật toán
     - Tên gọi: Mã Playfair (do Charles Wheatstone phát minh, Lord Playfair phổ biến).
     - Ý tưởng: Dùng ma trận 5×5 tạo từ khóa (gộp I/J).
     - Mã hóa:
          + Chuẩn hóa plaintext → chia thành cặp chữ (digraph).
          + Nếu 2 chữ giống nhau → chèn X vào.
          + Nếu cặp cùng hàng → lấy chữ bên phải.
          + Nếu cặp cùng cột → lấy chữ bên dưới.
          + Nếu khác hàng & cột → thay bằng chữ ở cùng hàng nhưng cột đối nhau (tạo hình chữ nhật).
     - Giải mã: ngược lại (bên trái, bên trên).
     - Không gian khóa: rất lớn (tất cả cách sắp xếp 25 chữ cái).
     - Cách phá:
          + Phân tích tần suất digram.
          + Dùng máy tính + thuật toán tìm kiếm heuristic (hill climbing).
 2. Cài đặt thuật toán mã hoá và giải mã bằng code C++

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/2c1d8993-09de-4536-9122-35d5639064bb" />

     <img width="1477" height="757" alt="image" src="https://github.com/user-attachments/assets/7811c768-5b4b-4941-8bd8-2371c6e1af60" />

 3. Cài đặt thuật toán mã hoá và giải mã bằng code html+css+javascript

     <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e367ee22-bd5f-4981-b210-d727abaa51f1" />

     <img width="1916" height="1079" alt="image" src="https://github.com/user-attachments/assets/0e80472c-0684-4929-a498-66accbd770a5" />
