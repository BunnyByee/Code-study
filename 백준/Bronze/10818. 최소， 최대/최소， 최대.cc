#include <iostream>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;

	// 크기 N짜리 동적 배열 생성
	vector<int> arr(N);
	
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	int min = arr[0];
	int max = arr[0];

	for (int num : arr) {
		if (num > max) max = num;
		if (num < min) min = num;
	}

	cout << min << " " << max;
}