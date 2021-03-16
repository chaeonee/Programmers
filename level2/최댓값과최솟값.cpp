#include <string>
#include <vector>
#include <cstring>

using namespace std;

string solution(string s) {
    char *str = new char[s.size()];
	strcpy(str, s.c_str());
    char *n = strtok(str," ");
    
    int min = 1234567, max = -1234567;
    while(n != NULL){
        if(min > atoi(n)){
            min = atoi(n);
        }
        if(max < atoi(n)){
            max = atoi(n);
        }
        n = strtok(NULL," ");
    }
    string answer = to_string(min) + " " + to_string(max);
    return answer;
}
