#include <iostream>
using namespace std;

int solve(int n){
	int answer = 0;
	
	while(n>0){
		answer += n % 10;
		n /= 10;
	}
	
	return answer;
}

int main(){
	int N, result = 0;
	cin >> N;
	
	for (int i=1; i<N+1; i++){
		int x = i + solve(i);
		
		if(x == N){
			result = i;
			break;
		}
	}
	
	cout << result;
	
	return 0;
}