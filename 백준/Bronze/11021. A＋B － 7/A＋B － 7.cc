#include <iostream>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;

	for (int i = 1; i < T + 1; i++) {
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i << ": " << a + b << '\n';
	}
}