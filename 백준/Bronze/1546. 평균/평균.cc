#include <iostream>
#include <algorithm>
using namespace std;

// 배열의 최대값 구하는 방법
// 1. 반복문을 이용한 함수 생성
// 2. std::max_element() 사용
 
int main(){
	int N, arr[1000];
	double result = 0.0;
	
	cin >> N;
	
	for (int i=0; i<N; i++){
		cin >> arr[i];
	} 
	
	// max_element 값은 포인터 형식이기 때문에
	// *를 붙여 역참조 해야함. 
	int max = *max_element(arr, arr+N);
	
	for (int i=0; i<N; i++){
		// 정수 ÷정수 -> 0 또는 1만 나옴.
		// 실수로 변경해줘야 함. 
		result += (double)arr[i]/max*100;
	}
	cout << fixed;
	cout.precision(15);
	cout << result / N << '\n';
	return 0;
} 