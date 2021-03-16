#include <string>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    
    int size = progresses.size();
    for(int i = 0; i < size; i++){
        q.push((int)ceil((double)(100-progresses[i])/speeds[i]));
    }
    
    while(!q.empty()){
        int i = q.front(), n = 1;
        q.pop();
        while(!q.empty() && q.front() <= i){
            n++;
            q.pop();
        } 
        answer.push_back(n);
    }
    
    return answer;
}
