#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for(int i = 0; i < scoville.size(); i++){
        pq.push(scoville[i]);
    }
    
    int answer = -1, tmp = 0;
    while(!pq.empty()){
        int s1, s2;
        s1 = pq.top();
        pq.pop();
        
        if(s1 >= K){
            answer = tmp;
            break;
        }
        
        if(pq.empty()){
            break;
        }
        tmp++;
        
        s2 = pq.top();
        pq.pop();
        pq.push(s1+s2*2);      
    }
    return answer;
}
