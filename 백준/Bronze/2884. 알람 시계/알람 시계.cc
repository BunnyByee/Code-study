#include <iostream>
using namespace std;

int main() {
	int h, m;

	cin >> h >> m;

	// m - 45가 음수면?
	if (m - 45 < 0) {
		// 0시면?
		if (h == 0) {
			h += 23;
			// m + 60 - 45 -> m +15
			m += 15;
		}
		else {
			h--;
			m += 15;
		}
	}
	else {
		m -= 45;
	}
	cout << h << " " << m;

	return 0;
}