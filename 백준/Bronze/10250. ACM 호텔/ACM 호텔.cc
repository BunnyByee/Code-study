#include <iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T, H, W, N;
	cin >> T; // 테스트 개수 입력 
	
	while (T--){
		cin >> H >> W >> N; // 총 층 수, 방 수, 몇번째 손님
		
		int floor = (N-1) % H + 1;
		int room = (N-1) / H + 1;
		
		cout << floor * 100 + room << '\n';
	}
	
	return 0;
}