#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> stk;
    int i = 0;
    
    // 변수 i = 0, i가 arr길이보다 작을때까지 반복
    while(i < arr.size()){
        // stk 비어있다면 arr[i] 추가하고 i++
        if (stk.empty()) {
            stk.push_back(arr[i]);
            i++;
        }
        // 원소가 있다면 stk 마지막 원소 < arr[i] -> arr[i]를 뒤에 추가 i++
        else {
            if (stk.back() < arr[i]) {
                stk.push_back(arr[i]);
                i++;
            }
             // -> stk 마지막 원소 >= arr[i] 이라면 stk 마지막 원소 제거.
            else {
                stk.pop_back();
            }
        }
    }
    return stk;
}