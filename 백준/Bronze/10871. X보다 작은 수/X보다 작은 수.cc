#include <iostream>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int N, X;
	int arr[10000];

	cin >> N >> X;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < N; i++) {
		if (arr[i] < X) cout << arr[i] << " ";
	}

	return 0;
}