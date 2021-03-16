#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int N = board.size();
    vector<int> top_idx(N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(board[j][i] != 0){
                top_idx[i] = j;
                break;
            }
        }
    }
    
    int answer = 0;
    vector<int> basket;
    for(int m = 0; m < moves.size(); m++){
        int move = moves[m]-1;
        
         if(top_idx[move] == N){
            continue;
        }
        if(!basket.empty() && basket.back() == board[top_idx[move]][move]){
            basket.pop_back();
            answer += 2;
        }
        else{
            basket.push_back(board[top_idx[move]][move]);
        }
        top_idx[move]++;
    }
    
    return answer;
}
