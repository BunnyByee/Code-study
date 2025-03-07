#include <string>
#include <vector>

using namespace std;

int factorial(int n){
    if (n <= 1) return 1;
    return n * factorial(n-1);
}

int solution(int n) {
    int i = 0;
    while(factorial(i) <= n){
        i++;
    }
    return i-1;
    
}