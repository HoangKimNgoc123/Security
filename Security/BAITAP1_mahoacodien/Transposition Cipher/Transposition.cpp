
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Mã hoá hoán vị (columnar transposition)
string transposeEncrypt(string text, vector<int> key){
    int n = key.size();
    string result = "";
    
    // Chia văn bản thành các khối theo độ dài khóa
    for(int i=0; i<text.size(); i+=n){
        for(int k : key){
            int idx = i + k - 1; // vì key bắt đầu từ 1
            if(idx < text.size()) result += text[idx];
        }
    }
    return result;
}

// Giải mã hoán vị
string transposeDecrypt(string text, vector<int> key){
    int n = key.size();
    string result(text.size(), ' '); // tạo chuỗi kết quả cùng độ dài
    int i=0; // chỉ số trong bản mã
    
    // Chia bản mã thành các khối theo độ dài khóa
    for(int blockStart=0; blockStart<text.size(); blockStart+=n){
        for(int k=0; k<n; k++){
            int idx = blockStart + key[k] - 1;
            if(idx < text.size()) result[idx] = text[i++];
        }
    }
    return result;
}

int main(){
    string text;
    int n;
    cout << "Nhap van ban: ";
    getline(cin,text);

    cout << "Nhap so ky tu trong khoa: ";
    cin >> n;

    vector<int> key(n);
    cout << "Nhap khoa (day so 1..n): ";
    for(int i=0; i<n; i++) cin >> key[i];

    string encrypted = transposeEncrypt(text,key);
    cout << "Ma hoa: " << encrypted << endl;

    string decrypted = transposeDecrypt(encrypted,key);
    cout << "Giai ma: " << decrypted << endl;

    return 0;
}
