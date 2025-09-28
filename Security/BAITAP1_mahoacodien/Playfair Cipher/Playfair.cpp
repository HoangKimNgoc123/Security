#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

char matrix[5][5];

// Tạo ma trận Playfair từ khóa
void generateMatrix(string key){
    string used = "";
    for(char &c : key){
        if(!isalpha(c)) continue;
        c = toupper(c);
        if(c == 'J') c = 'I';
        if(used.find(c) == string::npos) used += c;
    }
    for(char c='A'; c<='Z'; c++){
        if(c == 'J') continue;
        if(used.find(c) == string::npos) used += c;
    }
    int k=0;
    for(int i=0;i<5;i++)
        for(int j=0;j<5;j++)
            matrix[i][j] = used[k++];
}

// Tìm vị trí ký tự trong ma trận
pair<int,int> findPos(char c){
    for(int i=0;i<5;i++)
        for(int j=0;j<5;j++)
            if(matrix[i][j]==c) return {i,j};
    return {0,0};
}

// Chuẩn hóa văn bản: bỏ ký tự không phải chữ cái, chuyển J->I, thêm X nếu lẻ hoặc trùng
string prepareText(string text){
    string res = "";
    for(char c : text){
        if(!isalpha(c)) continue;
        c = toupper(c);
        if(c=='J') c='I';
        res += c;
    }
    for(int i=0;i<res.size()-1;i+=2){
        if(res[i]==res[i+1]){
            res.insert(res.begin()+i+1,'X');
        }
    }
    if(res.size() % 2 != 0) res += 'X';
    return res;
}

// Hàm xử lý cặp ký tự
string processPair(char a, char b, bool encrypt){
    auto [r1,c1] = findPos(a);
    auto [r2,c2] = findPos(b);
    string res = "";
    if(r1==r2){ // cùng hàng
        res += matrix[r1][(c1 + (encrypt?1:4))%5];
        res += matrix[r2][(c2 + (encrypt?1:4))%5];
    } else if(c1==c2){ // cùng cột
        res += matrix[(r1 + (encrypt?1:4))%5][c1];
        res += matrix[(r2 + (encrypt?1:4))%5][c2];
    } else { // chữ nhật
        res += matrix[r1][c2];
        res += matrix[r2][c1];
    }
    return res;
}

// Mã hoá Playfair
string playfairEncrypt(string text){
    text = prepareText(text);
    string result = "";
    for(int i=0;i<text.size();i+=2){
        result += processPair(text[i], text[i+1], true);
    }
    return result;
}

// Giải mã Playfair
string playfairDecrypt(string text){
    string result = "";
    for(int i=0;i<text.size();i+=2){
        result += processPair(text[i], text[i+1], false);
    }
    return result;
}

int main(){
    string key, text;
    cout << "Nhap khoa: "; getline(cin,key);
    generateMatrix(key);
    cout << "Nhap van ban: "; getline(cin,text);

    string encrypted = playfairEncrypt(text);
    cout << "Ma hoa: " << encrypted << endl;

    string decrypted = playfairDecrypt(encrypted);
    cout << "Giai ma: " << decrypted << endl;

    return 0;
}