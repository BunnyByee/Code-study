#include <iostream>
#include <string>

using namespace std;

int main(){
	int T, R;
	string S;
	
	cin >> T;
	
	for (int i=0; i<T; i++){
		cin >> R >> S;
		
		for (char c : S){
			for (int i=0 ; i<R; i++){
				cout << c;
			}
		}
		cout << '\n';
	}
}