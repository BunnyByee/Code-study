#include <iostream>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int N, M;

	cin >> N >> M;

	vector<int> arr(N);

	for (int n = 0; n < M; n++) {
		int i, j, k;
		cin >> i >> j >> k;
		for (--i; i < j; i++) {
			arr[i] = k;
		}
	}

	for (int num : arr) {
		cout << num << " ";
	}
    
    return 0;
}