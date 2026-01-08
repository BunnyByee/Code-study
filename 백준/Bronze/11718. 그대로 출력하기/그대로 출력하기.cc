#include <iostream>
#include <string>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	string t;
	
	// 입력이 들어오면 그대로 출력하기 
	while(getline(cin, t)){
		cout << t << '\n';
	}
	
	return 0; 
}