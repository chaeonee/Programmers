#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int getDigit(int n){
    int digit = 0;
    do{
        digit++;
        n /= 10;
    }while(n);
    return digit;
}

bool cmp(int a, int b){
    int a_size = getDigit(a), b_size = getDigit(b);
    long long int tmp1 = a*pow(10,b_size)+b, tmp2 = b*pow(10,a_size)+a;
    if(tmp1 > tmp2){
        return true;
    }
    return false;
}

string solution(vector<int> numbers) {
    sort(numbers.begin(),numbers.end(),cmp);
    
    string answer = "";
    for(int i = 0; i < numbers.size(); i++){
        answer += to_string(numbers[i]);
    }
    
    if(answer.at(0) == '0'){
        answer = '0';
    }
    
    return answer;
}
