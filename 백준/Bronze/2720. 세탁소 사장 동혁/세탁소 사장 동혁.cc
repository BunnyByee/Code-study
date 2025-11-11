#include <iostream>
using namespace std;

int main(){
	int T, C;
	int coin[4] = {25, 10, 5, 1};
	
	cin >> T;
	
	for (int i=0; i<T; i++){
		cin >> C;
		int arr[4] = {0};
		
		for(int j=0; j<4; j++){
			arr[j] = C / coin[j];
			C %= coin[j];
		}
		
		for(int j=0; j<4; j++){
			cout << arr[j] << " ";
		}
		cout << '\n';
	}
	
	return 0;
}