#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {    
    int student1[5] = {1,2,3,4,5};
    int student2[8] = {2,1,2,3,2,4,2,5};
    int student3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    vector<int> correct(3,0);
    int a_size = answers.size();
    for(int i = 0; i < a_size; i++){
        if(student1[i%5] == answers[i]){
            correct[0]++;
        }
        if(student2[i%8] == answers[i]){
            correct[1]++;
        }
        if(student3[i%10] == answers[i]){
            correct[2]++;
        }
    }
    
    int s_max = -1;
    vector<int> answer;
    for(int i = 0; i < 3; i++){
        if(s_max < correct[i]){
            s_max = correct[i];
            vector<int> tmp;
            tmp.push_back(i+1);
            answer = tmp;
        }
        else if(s_max == correct[i]){
            answer.push_back(i+1);
        }
    }
    
    return answer;
}
