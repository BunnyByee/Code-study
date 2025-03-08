#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    
    if (a == b) answer = a;
    else {
        answer = (long long)(a+b) * (abs(a-b) + 1) / 2;
    }
    return answer;
    
    // // a와 b 사이에 속한 모든 정수를 더하기
    // // a < b -> a ++
    // if (a < b) {
    //     for (int i = a; i <= b; i++){
    //     answer += i;
    //     }
    // }
    // // a = b -> return a
    // else if (a == b) return a;
    // // a < b -> a--
    // else {
    //     for (int i = a; i >= b; i--){
    //     answer += i;
    //     }
    // }
}