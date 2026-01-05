#include <iostream>
using namespace std;

int main(){
	int t, a, b;
	string s;
	
	cin >> t;
	
	while(t>0){
		cin >> s;
		
		// 문자형 숫자를 정수형으로 바꾸는 법 
		a = s[0] - '0';
		b = s[2] - '0';
		
		cout << a+b << '\n';
		
		t--;
	}
	
	return 0;
}