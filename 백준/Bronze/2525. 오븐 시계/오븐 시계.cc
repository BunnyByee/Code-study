#include <iostream>
using namespace std;

int main() {
	int A, B, C;

	cin >> A >> B >> C;

	if (B + C < 60) cout << A << " " << (B + C);
	else {
		A += (B + C) / 60;
		B = (B + C) % 60;

		if (A > 23) A -= 24;
		cout << A << " " << B;
	}

	return 0;
}