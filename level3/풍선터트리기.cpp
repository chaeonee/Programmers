#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a) {
    int a_size = a.size();
    vector<bool> check(a_size,false);
    
    int a_min = a[0];
    int answer = a_size;
    for(int i = 1; i < a_size-1; i++){
        if(a_min < a[i]){
            check[i] = true;
        }
        else{
            a_min = a[i];
        }
    }
    
    a_min = a[a_size-1];
    for(int i = a_size-2; i > 0; i--){
        if(a_min < a[i]){
            if(check[i]){
                answer--;
            }
        }
        else{
            a_min = a[i];
        }
    }
    return answer;
}
