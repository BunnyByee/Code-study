#include <iostream>
using namespace std;

int main(){
	int N, M, result = 0;
	cin >> N >> M;
	
	int nums[N];
	for(int i=0; i<N; i++){
		cin >> nums[i];
	}
	
	for(int i=0; i<N; i++){
		for (int j=i+1; j<N; j++){
			for (int k=j+1; k<N; k++){
				int n_sum = nums[i] + nums[j] + nums[k];
				
				if (n_sum <= M && n_sum > result){
					result = n_sum;
				}
			}
		}
	}
	
	cout << result;
	
	return 0;
}