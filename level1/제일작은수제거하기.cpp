#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int min = 7654321, idx = -1;
    for(int i = 0; i < arr.size(); i++){
        if(min > arr[i]){
            min = arr[i];
            idx = i;
        }
    }
    vector<int> answer;
    for(int i = 0; i < arr.size(); i++){
        if(i == idx){
            continue;
        }
        answer.push_back(arr[i]);
    }
    
    if(answer.empty()){
        answer.push_back(-1);
    }
    return answer;
}
