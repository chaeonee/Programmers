#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(vector<int> a, vector<int> b){
    if(a[1] == b[1]){
        return a[0] < b[0];
    }    
    return a[1] < b[1];
}

int solution(vector<vector<int>> routes) {
    sort(routes.begin(),routes.end(),cmp);
    
    int answer = 0, start = -30001, num_routes = routes.size();
    for(int i = 0; i < routes.size(); i++){
        if(start >= routes[i][0]){
            continue;
        }
        answer++;
        start = routes[i][1];
    }
    
    return answer;
}
