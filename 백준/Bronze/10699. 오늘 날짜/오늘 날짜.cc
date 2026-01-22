#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

int main(){
	time_t timer;
	struct tm* t;
	timer = time(NULL); // 1970-01-01 0:0:0 시작해서 현재까지 
	t = localtime(&timer); // 포맷팅을 위해 구조체 활용 

	int year = t->tm_year +1900;
	int mon = t->tm_mon +1;
	int day = t->tm_mday;
	
	cout << year << "-"
         << setw(2) << setfill('0') << mon << "-"
         << setw(2) << setfill('0') << day;
	
	return 0;
}