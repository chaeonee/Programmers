#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int tmp_num = 1, answer = 1;
    for(int i = 2; i <= n; i++){
        int tmp = answer;
        answer = (tmp_num+answer) % 1000000007;
        tmp_num = tmp;
    }
    
    return answer;
}
