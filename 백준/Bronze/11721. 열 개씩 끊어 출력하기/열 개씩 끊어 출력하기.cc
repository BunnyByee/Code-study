#include <iostream>
#include <string>
using namespace std;

int main(){
	string s; 
	
	cin >> s;
	
	// 전체 문자 출력 
	for (int i=1; i<s.length()+1; i++){
		cout << s[i-1];
		
		// 만약 단어 길이가 10이 되면 끊어주기 
		if (i % 10 == 0) cout << '\n';
	}
	
	return 0;
}