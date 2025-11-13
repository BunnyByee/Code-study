#include <iostream>
using namespace std;

int main(){
	int N;
	
	cin >> N;
	
	int layer = 1;
	int last = 1;
	
	while(N>last){
		last += 6 * layer;
		layer++;
	}
	
	cout << layer;
	
	return 0; 
}