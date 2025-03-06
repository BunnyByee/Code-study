#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    long long n = num;
    
    // 아래 과정을 1이 나올때까지 반복한다. (주어진 수가 1이면 0을 반환)
    while(n != 1 && answer <= 500) {
        // 입력한 수가 짝수라면 2로 나누고
        if (n%2 == 0) n/= 2;
        // 입력한 수가 홀수라면 3을 곱하고 1을 더하고
        else n = n * 3 + 1;
        answer++;
    }
    // 반복횟수가 500회를 넘으면 -1을 반환한다.
   return answer > 500 ? -1 : answer;

    
//     while (answer < 500) {
//         if (answer == 0 && n == 1) break;
        
//         n = (n%2 == 0) ? n / 2 : n*3 + 1;
//         answer++;
        
//         if (n == 1) break;
//     }
    
//     return answer == 500 ? -1 : answer;
}