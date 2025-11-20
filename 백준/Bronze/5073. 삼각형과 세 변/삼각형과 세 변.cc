#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int arr[3];
	
	while(true){
		cin >> arr[0] >> arr[1] >> arr[2];
		
		if(arr[0]==0 && arr[1]==0 && arr[2]==0) break;
		
		sort(arr, arr+3); // 오름차순 정렬 
		
		if(arr[0] + arr[1] > arr[2]){
			if(arr[0] == arr[1] && arr[1] == arr[2]) cout << "Equilateral";
			else if (arr[0] == arr[1] || arr[1] == arr[2]) cout << "Isosceles";
			else cout << "Scalene";
		} else cout << "Invalid";
		cout << '\n';
	}
}