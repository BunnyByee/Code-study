#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(int x) {
    int sum = 0;
//  int num = x;
    
//  while(num > 0){
//      sum += num % 10;
//      num /= 10;
//   }
    
//   return (x % sum == 0) ? true : false;
    
    // 문자열 개수만큼 자릿수의 값을 합하기
    string str = to_string(x);
    
    for (char c: str) {
        sum += (c - '0');
    }
    
    // for (int i = 0; i < str.length(); i++) {
    //     sum += (str[i] - '0');
    // }

    bool answer = (x % sum == 0);
    return answer;
}