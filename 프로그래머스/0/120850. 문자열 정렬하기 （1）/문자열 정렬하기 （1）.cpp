#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    // 문자열 길이 만큼 반복
    for (char c : my_string){
    // 인덱스별 문자가 숫자인지 확인하고 숫자면 벡터에 추가 
        if (isdigit(c)){
            // char -> int로 변환
            answer.push_back(c-'0');
        }
    // 반복문이 끝나면 오름차순으로 정렬
    } sort(answer.begin(),answer.end());
    return answer;
}