#include <iostream>

using namespace std;

int main(){
	int a1, a0, c, n0;
	int result;
	
	cin >> a1 >> a0 >> c >> n0;
	
	if (a1 < c){
		result = (c-a1)*n0 >= a0 ? 1 : 0;	
	} 
	else if (a1 == c) {
		result = a0 <= 0 ? 1 : 0;
	}
	else result = 0;
	
	cout << result;
	
	return 0;
}