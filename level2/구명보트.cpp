#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int left = 0, right = people.size()-1;
    sort(people.begin(),people.end());
    
    int answer = 0;
    while(left <= right){
        if(left == right){
            answer++;
            break;
        }
        if(people[left]+people[right] <= limit){
            answer++;
            left++;
            right--;
        }
        else{
            answer++;
            right--;
        }
    }
    return answer;
}
