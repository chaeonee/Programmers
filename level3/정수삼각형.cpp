#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int t_size = triangle.size(), answer = 0;
    vector<vector<int>> dp(t_size);
    dp[0].push_back(triangle[0][0]);
    for(int i = 1; i < t_size; i++){
        for(int j = 0; j <= i; j++){
            if(j == 0){
                dp[i].push_back(triangle[i][j] + dp[i-1][j]);
            }
            else if(j == i){
                dp[i].push_back(triangle[i][j] + dp[i-1][j-1]);
            }
            else{
                dp[i].push_back(triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j]));
            }
            answer = max(answer,dp[i][j]);
        }
    }
    return answer;
}
