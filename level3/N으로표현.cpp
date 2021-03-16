#include <string>
#include <vector>
#include <cmath>

using namespace std;

int makeNum(int N, int digit){
    int num = 0;
    for(int i = 0; i < digit; i++){
        num += pow(10,i)*N;
    }
    return num;
}

int solution(int N, int number) {
    if(N == number){
        return 1;
    }
    
    vector<vector<int>> v;
    for(int i = 0; i < 9; i++){
        vector<int> tmp;
        if(i == 0){
            v.push_back(tmp);
            continue;
        }
        tmp.push_back(makeNum(N,i));
        v.push_back(tmp);
    }
    
    int answer = -1;
    for(int i = 2; i <= 8; i++){
        for(int j = 1; j <= i/2; j++){
            for(int x = 0; x < v[j].size(); x++){
                for(int y = 0; y < v[i-j].size(); y++){
                    v[i].push_back(v[j][x]+v[i-j][y]);
                    v[i].push_back(v[j][x]-v[i-j][y]);
                    v[i].push_back(v[i-j][y]-v[j][x]);
                    v[i].push_back(v[j][x]*v[i-j][y]);
                    if(v[i-j][y] != 0){
                        v[i].push_back(v[j][x]/v[i-j][y]);
                    }
                    if(v[j][x] != 0){
                        v[i].push_back(v[i-j][y]/v[j][x]);
                    }
                }
            }
        }
        for(int j = 0; j < v[i].size(); j++){
            if(v[i][j] == number){
                answer = i;
                break;
            }
        }
        if(answer != -1){
            break;
        }
    }
    
    return answer;
}
