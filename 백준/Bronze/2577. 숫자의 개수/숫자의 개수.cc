#include <iostream>
#include <string>
using namespace std;

int main(){
	int a,b,c;
	cin >> a>> b>> c;
	
	int total = a*b*c;
	string s = to_string(total);
	
	// 0~9까지 숫자의 개수를 저장할 배열 
	int count[10] = {0}; 
	
	for (char c :s){
		int digit = c-'0';
		count[digit]++;
	}
	
	// 결과 출력
    for (int i = 0; i < 10; i++) {
        cout << count[i] << '\n';
    }
	
	return 0;
}