#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    if(s/n == 0){
        answer.push_back(-1);
        return answer;
    }
    
    for(int i = 0; i < n; i++){
        if(i >= n-s%n){
            answer.push_back(s/n+1);
        }
        else{
            answer.push_back(s/n);
        }
    }
    return answer;
}
