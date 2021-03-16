#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    int len = number.size(), start = 0;
    int end = len-k;
    
    string answer = "";
    while(end--){
        int tmp_num = -1;
        for(int i = start; i < len-end; i++){
            if(tmp_num < (int)(number.at(i)-'0')){
                start = i+1;
                tmp_num = (int)(number.at(i)-'0');
            }
        }
        answer += tmp_num + '0';
    }
    
    return answer;
}
