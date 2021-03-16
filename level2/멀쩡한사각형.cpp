#include <iostream>
using namespace std;

int getGCD(int a, int b){
    while(a){
        int tmp = a;
        a = b % a;
        b = tmp;
    }
    return b;
}

long long  solution(int w,int h) {
    long long answer = (long long)w * (long long)h - (long long)(w + h - getGCD(w,h));
    return answer;
}
