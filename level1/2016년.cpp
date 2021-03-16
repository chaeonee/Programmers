#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string day[7] = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
    int month[13] = {0,31,29,31,30,31,30,31,31,30,31,30,31};
    
    int sub = 0;
    for(int i = 1; i < a; i++){
        sub += month[i];
    }
    sub += b;
    
    string answer = day[sub%7];
    return answer;
}
