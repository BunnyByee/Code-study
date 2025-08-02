#include <iostream>
using namespace std;

int main() {
	int a, b;

	while(true){
		cin >> a >> b;

		// 종료 조건
		if ((a == 0) && (b == 0)) break;

		cout << a + b << '\n';
	}
}