#include <iostream>
using namespace std;

int main(){
	int N;
	cin >> N;
	
	// 사각형 좌표값 변수 
	int min_x = 0, min_y = 0, max_x = 0, max_y = 0;
	
	for (int i=0; i<N; i++){
		int x, y;
		cin >> x >> y;
		
		// 사각형 좌표 지정
		if (min_x == 0 || min_x > x) min_x = x;
		if (min_y == 0 || min_y > y) min_y = y;
		if (max_x == 0 || max_x < x) max_x = x;
		if (max_y == 0 || max_y < y) max_y = y;
	}
	
	cout << (max_x - min_x)*(max_y - min_y);
}