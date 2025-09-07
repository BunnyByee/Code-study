#include <iostream>

using namespace std;
int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int a[6] = {1, 1, 2, 2, 2, 8};
	int b;
	
	for (int i=0; i<6; i++){
		cin >> b;
		cout << a[i] - b << " ";
	}
}