#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    if(n == 0){
        return "0";
    }
    
    char num[3] = {'1','2','4'};
    string answer = "";
    while(n){
        n--;
        answer = num[n%3] + answer;
        n /= 3;
    }
    
    return answer;
}
