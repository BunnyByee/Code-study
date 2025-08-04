#include <iostream>

using namespace std;

int main() {
	int arr[9];

	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
	}

	int max = arr[0], n = 0;

	for (int i = 1; i < 9; i++) {
		if (arr[i] > max) {
			max = arr[i];
			n = i;
		}
	}

	cout << max << '\n';
	cout << n+1;
}