#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(),participant.end());
    sort(completion.begin(),completion.end());
    completion.push_back("");
    
    int size = completion.size();
    string answer = "";
    for(int i = 0; i < size; i++){
        if(participant[i] != completion[i]){
            answer = participant[i];
            break;
        }
    }
    
    return answer;
}
