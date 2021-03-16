#include <string>
#include <vector>

using namespace std;

void getTarget(vector<int> numbers, int target, int s, int num, int &answer){
    if(s == numbers.size()){
        if(num == target){
            answer++;
        }
        return;
    }
    getTarget(numbers,target,s+1,num+numbers[s],answer);
    getTarget(numbers,target,s+1,num-numbers[s],answer);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    getTarget(numbers,target,0,0,answer);
    return answer;
}
