#include <string>
#include <vector>

using namespace std;

string solution(string rny_string) {
    string answer = "";
    string str = rny_string;
    int size = str.length();
    
    for (char c : str){
        if (c == 'm') answer += "rn";
        else answer += c;
    }
    return answer;
}