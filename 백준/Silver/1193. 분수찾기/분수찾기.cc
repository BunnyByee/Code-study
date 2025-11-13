#include <iostream>
using namespace std;

int main(){
	int X;
	
	cin >> X;
	
	int layer = 1;
	int last = 0;
	
	while (X > last + layer) {
		last += layer;
		layer++;
	}
	
	int pos = X - last;
	
	int a, b;
	if (layer % 2 == 0) {
		a = pos;
		b = layer - pos + 1;
	} else{
		a = layer - pos + 1;
		b = pos;
	}
	
	cout << a << "/" << b;
	return 0;
}