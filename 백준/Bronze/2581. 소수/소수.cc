#include <iostream>
using namespace std;

bool prime(int a){
	if (a == 1) return false;
	for (int i=2; i*i<=a; i++){
		if(a % i == 0) return false;
	}
	return true;
} 

int main(){
	int M, N;
	cin >> M >> N;
	
	// 소수의 합과 최소 값 구하기 
	int sum = 0, min = 0;
	
	for (int i = M; i<=N; i++){
		// 소수 판별 : 몫이 1과 나 자신인 것 
		if (prime(i)){
			sum += i;
			if (min == 0 || min > i) min = i;
		} else {
			continue;
		}
	}
	
	if (sum == 0)cout << -1;
	else cout << sum << '\n' << min;
}