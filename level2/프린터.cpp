#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    queue<pair<int,int> > q;
    for(int i = 0; i < priorities.size(); i++){
        q.push(make_pair(i,priorities[i]));
    }
    sort(priorities.begin(),priorities.end());
    
    while(!q.empty()){
        if(q.front().second == priorities.back()){
            answer++;
            if(q.front().first == location){
                break;
            }
            q.pop();
            priorities.pop_back();
            continue;
        }
        q.push(q.front());
        q.pop();
    }
    
    return answer;
}
