#include <iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T, H, W, N, result = 0;
	cin >> T; // 테스트 개수 입력 
	
	for (int i=0; i<T; i++){
		cin >> H >> W >> N; // 총 층 수, 방 수, 몇번째 손님
		
		// 나머지가 0이면 맨 꼭대기 층.
		if (N % H == 0) result = H * 100 + N/H;
		else result = (N%H) * 100 + N/H +1;
		
		cout << result << '\n';
	}
	
	return 0;
}