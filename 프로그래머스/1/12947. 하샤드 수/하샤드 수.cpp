#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(int x) {
    string str = to_string(x);
    
    // 문자열 개수만큼 자릿수의 값을 합하기
    int i = 0;
    int sum = 0;
    
    for (int i = 0; i < str.length(); i++) {
    sum += (str[i] - '0');
    }

    bool answer = (x % sum == 0);
    return answer;
}