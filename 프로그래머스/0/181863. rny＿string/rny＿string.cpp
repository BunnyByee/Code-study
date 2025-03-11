#include <string>
#include <vector>

using namespace std;

string solution(string rny_string) {
    string answer = "";
    string str = rny_string;
    // 문자열의 문자 c가 m이면 "rm" 넣기
    // 그게 아니면 문자 c 넣기
    for (char c : str){
        if (c == 'm') answer += "rn";
        else answer += c;
    }
    return answer;
}