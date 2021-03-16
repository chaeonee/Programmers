#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int a = 0, answer = 1;
    for(int i = 1; i < n; i++){
        int tmp = answer;
        answer = (a+answer) % 1234567;
        a = tmp;
    }
    return answer;
}
