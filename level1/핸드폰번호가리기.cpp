#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    int len = phone_number.size();
    string answer = "";
    for(int i = 0; i < len; i++){
        if(i < len-4){
            answer += "*";
        }
        else{
            answer += phone_number.at(i);
        }
    }
    return answer;
}
