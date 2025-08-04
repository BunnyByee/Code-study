#include <iostream>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, numbers[100], v;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> numbers[i];
	}

	cin >> v;

	int count = 0;
	for (int i = 0; i < N; i++) {
		if (numbers[i] == v) count++;
	}

	cout << count << '\n';
}