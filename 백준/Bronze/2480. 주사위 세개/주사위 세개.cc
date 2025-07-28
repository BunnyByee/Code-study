#include <iostream>

using namespace std;

int main() {
	int a, b, c, max = 0;

	cin >> a >> b >> c;
	max = a;

	// 같은 눈 3개
	if ((a == b) && (a == c)) {
		cout << 10000 + a * 1000;
	}
	// 같은 눈 2개
	else if ((a == b) && (b != c)) {
		cout << 1000 + a * 100;
	}
	else if ((a != b) && (b == c)) {
		cout << 1000 + b * 100;
	}
	else if ((a != b) && (a == c)) {
		cout << 1000 + c * 100;
	}
	// 다 다르면?
	else {
		if (max < b) max = b;
		if (max < c) max = c;
		cout << max * 100;
	}

	return 0;
}