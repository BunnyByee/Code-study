#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int N, M;
	int arr[100];
	
	cin >> N >> M;
	
	// 바구니 채워놓기 
	for (int i=0; i<N; i++) arr[i] = i+1;
	
	// i부터 j까지 역순 
	for (int k=0; k<M; k++){
		int i, j;
		
		cin >> i >> j;
		reverse(arr+ --i, arr+j);
	}
	
	// 숫자 출력 
	for(int i=0; i<N; i++) cout << arr[i] << " ";
	
	return 0;
}