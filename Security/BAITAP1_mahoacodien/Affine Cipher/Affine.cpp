#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Hàm tính gcd
int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

// T?m ngh?ch ð?o modulo (a^-1 mod m)
int modInverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) return x;
    }
    return -1; // không có ngh?ch ð?o
}

// M? hóa Affine
string affineEncrypt(string text, int a, int b) {
    string result = "";
    for (char c : text) {
        if (islower(c)) {
            int x = c - 'a';
            char enc = (char)(((a * x + b) % 26) + 'a');
            result += enc;
        } else if (isupper(c)) {
            int x = c - 'A';
            char enc = (char)(((a * x + b) % 26) + 'A');
            result += enc;
        } else {
            result += c; // gi? nguyên k? t? không ph?i ch?
        }
    }
    return result;
}

// Gi?i m? Affine
string affineDecrypt(string cipher, int a, int b) {
    string result = "";
    int a_inv = modInverse(a, 26);
    if (a_inv == -1) {
        return "Không th? gi?i m? v? a không có ngh?ch ð?o modulo!";
    }

    for (char c : cipher) {
        if (islower(c)) {
            int y = c - 'a';
            char dec = (char)(((a_inv * (y - b + 26)) % 26) + 'a');
            result += dec;
        } else if (isupper(c)) {
            int y = c - 'A';
            char dec = (char)(((a_inv * (y - b + 26)) % 26) + 'A');
            result += dec;
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string text;
    int a, b;

    cout << "Nhap van ban: ";
    getline(cin, text);
    cout << "Nhap khoa a (nguyen to cung nhau voi 26): ";
    cin >> a;
    cout << "Nhap khoa b: ";
    cin >> b;

    if (gcd(a, 26) != 1) {
        cout << "Khoa a khong hop le! Phai nguyen to cung nhau voi 26.\n";
        return 0;
    }

    string encrypted = affineEncrypt(text, a, b);
    string decrypted = affineDecrypt(encrypted, a, b);

    cout << "\nBan ro: " << text;
    cout << "\nBan ma: " << encrypted;
    cout << "\nGiai ma: " << decrypted << endl;

    return 0;
}
