#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

bool isPrime(int n){
    if(n == 1){
        return false;
    }
    for(int i = 2; i <= sqrt(n); i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
}

void countPrime(vector<int> numbers, vector<bool> visit, int &cnt, int d, int N, int cur){
    if(d == N){
        return;
    }
    int pre_num = -1;
    for(int i = 0; i < N; i++){
        if((!d & !numbers[i]) || visit[i] || pre_num == numbers[i]){
            continue;
        }
        pre_num = numbers[i];
        int tmp_cur = cur;
        cur = stoi(to_string(cur)+to_string(numbers[i]));
        if(isPrime(cur)){
            cnt++;
        }
        visit[i] = true;
        countPrime(numbers,visit,cnt,d+1,N,cur);
        visit[i] = false;
        cur = tmp_cur;
    }
}

int solution(string numbers) {
    vector<int> num;
    for(int i = 0; i < numbers.size(); i++){
        num.push_back(int(numbers.at(i)-'0'));
    }
    sort(num.begin(),num.end());
    
    int answer = 0;
    vector<bool> visit(numbers.size(),false);
    countPrime(num,visit,answer,0,numbers.size(),0);
    return answer;
}
