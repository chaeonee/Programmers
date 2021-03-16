#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    int top = 0, bottom = n-1, cur = 0;
    vector<vector<int>> v;
    for(int i = 1; i <= n; i++){
        vector<int> tmp;
        for(int j = 0; j < i; j++){
            tmp.push_back(0);
        }
        v.push_back(tmp);
    }
    
    int num = 0;
    while(top <= bottom){
        for(int i = top; i <= bottom; i++){
            num++;
            v[i][cur] = num;
        }
        for(int i = cur+1; i < bottom-cur; i++){
            num++;
            v[bottom][i] = num;
        }
        
        for(int i = bottom; i > top; i--){
            num++;
            v[i][i-cur] = num;
        }
        cur += 1;
        top += 2;
        bottom -= 1;
    }
    
    vector<int> answer;
    for(int i = 0; i < n; i++){
        for(int j = 0; j <= i; j++){
            answer.push_back(v[i][j]);
        }
    }
    return answer;
}
