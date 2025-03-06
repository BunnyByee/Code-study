#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    long long n = num;

    while (answer < 500) {
        if (answer == 0 && n == 1) break;
        
        n = (n%2 == 0) ? n / 2 : n*3 + 1;
        answer++;
        
        if (n == 1) break;
    }
    
    return answer == 500 ? -1 : answer;
}