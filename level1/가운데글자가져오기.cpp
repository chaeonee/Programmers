#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int len = s.size();
    string answer = "";
    if(len % 2 == 0){
        answer = s.substr(len/2-1,2);
    }
    else{
        answer = s.at(len/2);
    }
    return answer;
}
