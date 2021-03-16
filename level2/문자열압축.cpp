#include <string>
#include <vector>

using namespace std;

int getDigit(int n){
    int digit = 0;
    while(n){
        digit++;
        n /= 10;
    }
    return digit;
}

int solution(string s) {
    int s_len = s.size();
    int answer = s_len;
    for(int l = 1; l <= s_len/2; l++){
        int idx = 0, cnt = s_len;
        while(idx < s_len){
            string str = s.substr(idx,l);
            int tmp_idx = idx+l, s_cnt = 1;
            for(int i = tmp_idx; i < s_len; i+=l){
                if(str != s.substr(i,l)){
                    break;
                }
                s_cnt++;
            }
            idx += s_cnt * l;
            cnt -= (s_cnt-1)*l;
            if(s_cnt != 1){
                cnt += getDigit(s_cnt);
            }
        }
        if(answer > cnt){
            answer = cnt;
        }
    }
    return answer;
}
