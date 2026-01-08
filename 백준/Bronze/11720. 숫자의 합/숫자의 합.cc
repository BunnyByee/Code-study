#include <iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, result = 0;
	char ch;
	
	cin >> n;
	
	for(int i=0; i<n; i++){
		cin >> ch; // 숫자 하나를 문자로 인식해서 읽기 
		result += (ch - '0'); // 문자를 숫자로 변환하기 
	}
	
	cout << result;
	return 0;
}