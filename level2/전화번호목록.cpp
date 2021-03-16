#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(),phone_book.end());
    
    bool answer = true;
    int size = phone_book.size();
    for(int i = 1; i < size; i++){
        int num_len = phone_book[i-1].size();
        
        if(num_len > phone_book[i].size()){
            continue;
        }
        
        bool tmp = true;
        for(int j = 0; j < num_len; j++){
            if(phone_book[i-1][j] != phone_book[i][j]){
                tmp = false;
                break;
            }
        }

        if(tmp){
            answer = false;
            return answer;
        }
    }
    
    return answer;
}
