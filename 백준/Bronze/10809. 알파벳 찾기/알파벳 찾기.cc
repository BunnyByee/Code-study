#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int check[26];
	// 전부 일단 -1로 채워넣기 
	fill_n(check, 26, -1);
	
	string s;
	
	cin >> s;
	
	for (int i=0; i<s.length(); i++){
		int n = (int)s[i] -'a';
		
		if(check[n] == -1) check[n] = i;
	}
	
	for (int i : check){
		cout << i << " ";
	}
	
	return 0; 
}