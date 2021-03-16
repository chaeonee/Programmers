#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct Word{
    int cnt;
    string word;
};

int solution(string begin, string target, vector<string> words) {
    int w_len = begin.size(), list_size = words.size();
    
    queue<Word> q;
    q.push({0,begin});
    
    int answer = 0;
    vector<bool> visit(list_size,false);
    while(!q.empty()){
        int cnt = q.front().cnt;
        string word = q.front().word;
        q.pop();
        
        if(word == target){
            answer = cnt;
            break;
        }
        for(int i = 0; i < list_size; i++){
            if(visit[i]){
                continue;
            }
            
            int diff = 0;
            for(int j = 0; j < w_len; j++){
                if(words[i].at(j) != word.at(j)){
                    diff++;
                }
                if(diff > 1){
                    break;
                }
            }
            if(diff <= 1){
                visit[i] = true;
                q.push({cnt+1,words[i]});
            }
        }
        
    }
    
    return answer;
}
