#include <string>
#include <vector>

using namespace std;

bool getHarshad(int n){
    int s_digit = 0, tmp = n;
    while(tmp){
        s_digit += tmp%10;
        tmp /= 10;
    }
    
    if(n % s_digit == 0){
        return true;
    }
    return false;
}

bool solution(int x) {
    return getHarshad(x);
}
