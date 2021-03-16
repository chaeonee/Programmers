#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    vector<vector<bool>> graph(n,vector<bool>(n,false));
    for(int i = 0; i < edge.size(); i++){
        int x = edge[i][0], y = edge[i][1];
        graph[x-1][y-1] = true;
        graph[y-1][x-1] = true;
    }
    
    queue<int> q;
    q.push(0);
    vector<bool> visit(n,false);
    visit[0] = true;
    
    int answer = 0;
    while(!q.empty()){
        int q_size = q.size(), cnt = 0;
        for(int i = 0; i < q_size; i++){
            int vertex = q.front();
            q.pop();
            
            for(int i = 0; i < n; i++){
                if(graph[vertex][i] && !visit[i]){
                    cnt++;
                    q.push(i);
                    visit[i] = true;
                }
            }
        }     
        if(cnt != 0){
            answer = cnt;
        }
    }
    
    return answer;
}
