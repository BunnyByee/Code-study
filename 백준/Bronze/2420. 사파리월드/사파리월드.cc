#include <iostream>
#include <cstdlib> // llabs()
using namespace std;

int main(){
	long long n, m, result;
	cin >> n >> m;
	
	result = llabs(n-m);
	
	cout << result;
	
	return 0;
}