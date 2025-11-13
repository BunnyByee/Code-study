#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int N;
	
	cin >> N;
	
	// 한 변의 점이 이전 점의 개수 *2 -1 만큼 증가함
	// (이전 점  * 2 -1) ^ 2
	// 그러나 횟수에 초점을 두고 계산해야 됨
	
	int s = pow(2, N) +1;
	// 가로 점 개수 x 세로 점 개수 -> 정사각형이니 제곱 
	int result = pow(s, 2); 
	 
	cout << result;
}