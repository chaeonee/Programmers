#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int area = brown + yellow;
    
    vector<int> answer;
    for(int h = 1; h <= (int)sqrt((double)area); h++){
        if(area % h != 0){
            continue;
        }
        int w = area/h;
        if(2*(w+h-2) == brown){
            answer.push_back(w);
            answer.push_back(h);
            break;
        }
    }
    return answer;
}
