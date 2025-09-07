#include <iostream>
#include <string>
using namespace std;

// 65~90 A~Z
int main(){
	string str;
	int sum = 0;
	cin >> str;
	
	for (char c : str) {
		if (c >= 'W') sum += 10;
		else if (c >= 'T') sum += 9;
		else if (c >= 'P') sum += 8;
		else if (c >= 'M') sum += 7;
		else if (c >= 'J') sum += 6;
		else if (c >= 'G') sum += 5;
		else if (c >= 'D') sum += 4;
		else if (c >= 'A') sum += 3;
	}
	
	cout << sum; 
}