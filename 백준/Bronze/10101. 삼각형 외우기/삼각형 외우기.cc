#include <iostream>
using namespace std;

int main(){
	int a,b,c;
	
	cin >> a>> b>> c;
	
	int sum = a+b+c;
		
	if(sum == 180){
		if(a==60 && b==60 && c==60) cout << "Equilateral";
		else if(a == b || b == c || a == c) cout << "Isosceles";
		else cout << "Scalene";
	} else cout << "Error";
} 