#include <iostream>
using namespace std;

int main(){
	int T, A, B;
	
	cin >> T;
	
	while(T>0){
		cin >> A >> B;
		cout << A+B << '\n';
		T--;
	}
}