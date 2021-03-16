#include <string>
#include <vector>
#include<iostream>
using namespace std;

int solution(int num) {
    if(num == 1){
        return 0;
    }
    
    int answer = 0, t = 0;
    long long int n = (long long int)num;
    while(++t){
        if(t > 500){
            answer = -1;
            break;
        }
        
        if(n%2 == 0){
            n /= 2;
        }
        else{
            n = n * 3 + 1;
        }
        
        if(n == 1){
            answer = t;
            break;
        }
    }
    return answer;
}
