#include <iostream>

using namespace std;

int main() {
	int X, N, sum = 0;

	cin >> X >> N;
	for (int i = 0; i < N; i++) {
		int a, b;

		cin >> a >> b;
		sum += a * b;
	}

	if (X == sum) cout << "Yes";
	else cout << "No";
}