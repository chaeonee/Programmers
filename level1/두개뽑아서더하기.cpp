#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    bool visit[201] = {false, };
    int s = numbers.size();
    for(int i = 0; i < s; i++){
        for(int j = i+1; j < s; j++){
            int num = numbers[i] + numbers[j];
            if(!visit[num]){
                visit[num] = true;
                answer.push_back(num);
            }
        }
    }
    sort(answer.begin(),answer.end());
    return answer;
}
