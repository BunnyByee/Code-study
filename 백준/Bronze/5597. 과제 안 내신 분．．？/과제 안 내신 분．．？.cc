#include <iostream>

using namespace std;

int main(){
    bool exist[31] = {false};
    int num;
    
    for (int i=0; i<28; i++)
    {
        cin >> num;
        exist[num] = true;
    }
    
    for (int i=1; i<31; i++){
        if(!exist[i]) cout << i << '\n';
    }
    
    return 0;
}