#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    if (s == "F") {
        cout << "0.0" << endl;
        return 0;
    }

    double score = 0.0;

    // 1. 첫 글자로 기본 점수 설정
    switch (s[0]) {
        case 'A': score = 4.0; break;
        case 'B': score = 3.0; break;
        case 'C': score = 2.0; break;
        case 'D': score = 1.0; break;
    }

    // 2. 두 번째 글자로 보정
    if (s[1] == '+') score += 0.3;
    else if (s[1] == '-') score -= 0.3;

    printf("%.1f\n", score);

    return 0;
}