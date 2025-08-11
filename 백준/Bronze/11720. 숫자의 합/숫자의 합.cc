#include <iostream>
#include <string>

using namespace std;

int main(){
	int N, sum = 0;
	string num;
	
	cin >> N >> num;
	
	for (char i : num){
		sum += (int)i -'0';
	}
	
	cout << sum;
}