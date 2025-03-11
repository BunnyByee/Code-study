#include <string>
#include <vector>

using namespace std;

string solution(string rny_string) {
    string answer = "";
    string str = rny_string;
    int size = str.length();
    
    for (int i=0 ; i < size; i++){
        if (str[i] == 'm') {
            answer.append("rn");
        }
        else{
            answer += (str[i]);
        }
    }
    return answer;
}