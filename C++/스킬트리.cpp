#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int pre_skill[26];
    for(int i = 0; i < 26; i++){
        pre_skill[i] = i;
    }
    
    int indegree[26] = {0,};
    int s_size = skill.size();
    for(int i = 0; i < s_size-1; i++){
        pre_skill[int(skill.at(i)-65)] = int(skill.at(i+1)-65);
        indegree[int(skill.at(i+1)-65)] = indegree[int(skill.at(i)-65)] + 1;
    }
    
    int answer = 0;
    int skill_size = skill_trees.size();
    for(int i = 0; i < skill_size; i++){
        s_size = skill_trees[i].size();
        int tmp_indegree[26];
        for(int j = 0; j < 26; j++){
            tmp_indegree[j] = indegree[j];
        }
        
        answer++;
        for(int j = 0; j < s_size; j++){
            if(tmp_indegree[int(skill_trees[i].at(j)-65)] != 0){
                answer--;
                break;
            }
            int tmp = int(skill_trees[i].at(j)-65);
            while(tmp != pre_skill[tmp]){
                tmp = pre_skill[tmp];
                tmp_indegree[tmp]--;
            }
        }
    }
    
    return answer;
}
