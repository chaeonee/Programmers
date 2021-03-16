#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int sec = 0, len = truck_weights.size();
    
    queue<int> q;
    for(int i = 0; i < bridge_length; i++){
        q.push(0);
    }
    
    int w = 0, idx = 0;
    while(!q.empty()){
        sec++;
        w -= q.front();
        q.pop();
        
        if(idx >= len){
            continue;
        }
        if(w+truck_weights[idx] > weight){
            q.push(0);
        }
        else{
            q.push(truck_weights[idx]);
            w += truck_weights[idx];
            idx++;
        }
    }
    
    return sec;
}
