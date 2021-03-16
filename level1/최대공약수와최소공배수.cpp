#include <string>
#include <vector>

using namespace std;

int getGCD(int a, int b){
    while(b){
        int tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    int gcd = getGCD(n,m);
    answer.push_back(gcd);
    answer.push_back((n*m)/gcd);
    return answer;
}
