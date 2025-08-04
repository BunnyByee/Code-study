#include <iostream>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
		
	int N, M;
	
	cin >> N >> M;

	vector<int> arr(N);

	for (int i = 0; i < N; i++) {
		arr[i] = i+1;
	}

	for (int n = 0; n < M; n++) {
		int i, j, temp =0;
		cin >> i >> j;

		temp = arr[--i];
		arr[i] = arr[--j];
		arr[j] = temp;
	}

	for (int num : arr) {
		cout << num << " ";
	}

	return 0;
}