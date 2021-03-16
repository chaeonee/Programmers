#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int n_uniform[n];
    for(int i = 0; i < n; i++){
        n_uniform[i] = 1;
    }
    for(int i = 0; i < lost.size(); i++){
        n_uniform[lost[i]-1]--;
    }
    for(int i = 0; i < reserve.size(); i++){
        n_uniform[reserve[i]-1]++;
    }
    
    int answer = 0;
    for(int i = 0; i < n; i++){
        if(n_uniform[i] != 0){
            answer += 1;
            continue;
        }
        if(i-1 >= 0 && n_uniform[i-1] > 1){
            answer += 1;
            n_uniform[i-1]--;
        }
        else if(i+1 < n && n_uniform[i+1] > 1){
            answer += 1;
            n_uniform[i+1]--;
        }
    }
    return answer;
}
