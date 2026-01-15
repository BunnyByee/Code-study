#include <iostream>
#include <string>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int arr[3]; // 정수 배열로 받기 
	string s; 
	
	for (int i=0; i<3; i++){
		cin >> arr[i];
	}
	
	// 문자열로 치환해서 더하기 
	s = to_string(arr[0]) + to_string(arr[1]);
	
	cout << arr[0] + arr[1] - arr[2] << '\n';
	cout << stoi(s) - arr[2]; // 숫자로 다시 변경해서 빼기
	
	return 0;
}