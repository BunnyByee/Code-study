#include <iostream>
using namespace std;

int main(){
	int N;
	
	cin >> N;
	
	for (int i=0; i<N; i++){
		for (int j=1; j<N-i ; j++){
			cout << " ";
		}
		for (int k=0; k<i+1 ; k++){
			cout << "*";
		}
		for (int a=0; a<i ; a++){
			cout << "*";
		}
		cout <<'\n';
	}
	
	for (int i=0; i<N-1; i++){
		for (int j=0; j<i+1; j++){
			cout << " ";
		}
		for (int k=1; k<N-i;k++){
			cout << "*";
		}
		for (int a=2; a<N-i; a++){
			cout << "*";
		}
		cout <<'\n';
	}
}