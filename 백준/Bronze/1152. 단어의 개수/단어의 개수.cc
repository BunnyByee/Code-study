#include <iostream>
#include <string>

using namespace std;

int main(){
	string str;
	getline(cin, str);
	
	int n = 1;
	
	if (str.front() == ' ') n--;
	if(str.back() == ' ')	n--;
	
	for (int i=0; i<str.size() ; i++){
		if (str[i] == ' ') n++;
	}
	
	cout << n;
}