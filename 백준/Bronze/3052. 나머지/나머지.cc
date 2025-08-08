#include <iostream>

using namespace std;

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	
    // 나머지 0부터 41까지 확인 !
	bool mode[42] = {false}; // 배열크기 확인!!
	int num;
	
	for (int i=0; i<10; i++){
		cin >> num;
		mode[num % 42] = true;
	}
	
	int count = 0; // 초기화 필수 
	for (int i=0; i<42; i++){
		if(mode[i]) count++;
	}
	
	cout << count << '\n';
	
	return 0;
}