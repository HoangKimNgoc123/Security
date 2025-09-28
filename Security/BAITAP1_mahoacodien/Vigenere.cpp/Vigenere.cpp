#include <iostream>
#include <string>
using namespace std;

// Hàm để mở rộng key sao cho bằng độ dài bản rõ
string generateKey(string text, string key) {
    int x = text.size();
    for (int i = 0; ; i++) {
        if (x == (int)key.size())
            break;
        key.push_back(key[i % key.size()]);
    }
    return key;
}

// Hàm mã hóa Vigenère
string encryptVigenere(string text, string key) {
    string cipherText = "";
    for (int i = 0; i < (int)text.size(); i++) {
        // (P + K) mod 26
        char x = (text[i] - 'a' + key[i] - 'a') % 26 + 'a';
        cipherText.push_back(x);
    }
    return cipherText;
}

// Hàm giải mã Vigenère
string decryptVigenere(string cipherText, string key) {
    string origText = "";
    for (int i = 0; i < (int)cipherText.size(); i++) {
        // (C - K + 26) mod 26
        char x = (cipherText[i] - 'a' - (key[i] - 'a') + 26) % 26 + 'a';
        origText.push_back(x);
    }
    return origText;
}

int main() {
    string text, key;

    cout << "Nhap ban ro (plaintext, chu thuong): ";
    cin >> text;
    cout << "Nhap khoa (key, chu thuong): ";
    cin >> key;

    string newKey = generateKey(text, key);
    string cipherText = encryptVigenere(text, newKey);
    string decryptedText = decryptVigenere(cipherText, newKey);

    cout << "Ban ma (ciphertext): " << cipherText << endl;
    cout << "Giai ma (plaintext): " << decryptedText << endl;

    return 0;
}
s