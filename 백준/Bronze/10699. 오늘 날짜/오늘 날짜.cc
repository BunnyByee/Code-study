#include <iostream>
#include <ctime>
using namespace std;

int main(){
	time_t timer;
	struct tm* t;
	timer = time(NULL); // 1970-01-01 0:0:0 시작해서 현재까지 
	t = localtime(&timer); // 포맷팅을 위해 구조체 활용 

	int year = t->tm_year +1900;
	int mon = t->tm_mon +1;
	int day = t->tm_mday;
	
	cout << year << "-";
	
	if (mon < 10)
		cout << "0" << mon << "-";
	else
		cout << mon << "-";
	
	if (day < 10)
		cout << "0" << day;
	else
		cout << day;
	
	return 0;
}