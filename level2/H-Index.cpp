#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    sort(citations.begin(),citations.end());
    
    int answer = 0;
    int c_size = citations.size();
    for(int h = 1; h <= c_size; h++){
        if(h > citations[c_size-h]){
            break;
        }
        answer = h;
    }
    return answer;
}
