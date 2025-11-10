#include <iostream>
using namespace std;

int main()
{
	int N, B, i = 0;
	int arr[50];
	
	cin >> N >> B;
	while (N > 0){
		arr[i++] = N % B;
		N /= B;
	}
	
	for (int j=i-1; j>-1; j--){
		if(arr[j] < 10) 
			cout << arr[j];
		else
			cout << (char)(arr[j] + 55);
	}
	
	return 0;
}