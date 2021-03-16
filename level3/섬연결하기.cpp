#include <string>
#include <vector>
#include <queue>

using namespace std;

struct Island{
    int node, cost;
};

struct cmp{
    bool operator()(Island &a, Island &b){
        if(a.cost == b.cost){
            return a.node > b.node;
        }
        return a.cost > b.cost;
    }
};

int solution(int n, vector<vector<int>> costs) {
    vector<vector<int>> cost(n, vector<int>(n,987654321));
    for(int i = 0; i < costs.size(); i++){
        int s = costs[i][0], e = costs[i][1], c = costs[i][2];
        cost[s][e] = c;
        cost[e][s] = c;
    }   
    
    priority_queue<Island,vector<Island>,cmp> pq;
    pq.push({0,0});
    for(int i = 1; i < n; i++){
        pq.push({i,987654321});
    }
    
    int answer = 0;
    while(!pq.empty()){
        int node = pq.top().node, n_cost = pq.top().cost;
        pq.pop();
        answer += n_cost;
        
        priority_queue<Island,vector<Island>,cmp> tmp;
        while(!pq.empty()){
            int tmp_node = pq.top().node, tmp_cost = pq.top().cost;
            pq.pop();
            
            if(cost[node][tmp_node] < tmp_cost){
                tmp.push({tmp_node,cost[node][tmp_node]});
            }
            else{
                tmp.push({tmp_node,tmp_cost});
            }
        }
        pq = tmp;
    }
    
    return answer;
}
