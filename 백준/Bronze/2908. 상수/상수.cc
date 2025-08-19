#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	string s1, s2;
	
	cin >> s1 >> s2;
	
	reverse(s1.begin(), s1.end());
	reverse(s2.begin(), s2.end());
	
	int n1 = stoi(s1);
	int n2 = stoi(s2);
	
	cout << max(n1, n2);
}