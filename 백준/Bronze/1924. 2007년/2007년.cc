#include <iostream>
#include <string>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	string week[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	int x, y, num = 0;
	cin >> x >> y;
	
	for (int i=0; i<x; i++){
		num += days[i];
	}
	num += y;
	
	cout << week[num % 7];
	
	return 0;
}