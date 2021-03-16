#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = -1;
    double sq = sqrt((double)n);
    if(sq == (long long)sq){
        sq++;
        answer = (long long)(sq*sq);
    }
    return answer;
}
