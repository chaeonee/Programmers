#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

struct Song{
    int num, plays;
};

struct cmp{
    bool operator()(Song a, Song b){
        if(a.plays == b.plays){
            return a.num > b.num;
        }
        return a.plays < b.plays;
    }
};

struct Songs{
    int s_sum = 0;
    priority_queue<Song,vector<Song>,cmp> pq;
};

bool cmp_v(pair<int, string> a, pair<int, string> b){
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, Songs> m;
    map<string, Songs>::iterator iter;
    
    int size = genres.size();
    for(int i = 0; i < size; i++){
        iter = m.find(genres[i]);
        if(iter == m.end()){
            Songs s;
            m.insert(make_pair(genres[i],s));
            m[genres[i]].s_sum += plays[i];
            m[genres[i]].pq.push({i,plays[i]});
        }
        else{
            m[genres[i]].s_sum += plays[i];
            m[genres[i]].pq.push({i,plays[i]});
        }
    }
    
    vector<pair<int, string> > v;
    vector<pair<int, string> >::iterator v_iter;
    for(iter = m.begin(); iter != m.end(); iter++){
        v.push_back(make_pair(iter->second.s_sum, iter->first));
    }
    sort(v.begin(),v.end(),cmp_v);
    
    vector<int> answer;
    for(v_iter = v.begin(); v_iter != v.end(); v_iter++){
        string g = v_iter->second;
        int idx = 0;
        while(!m[g].pq.empty() && idx < 2){
            idx++;
            answer.push_back(m[g].pq.top().num);
            m[g].pq.pop();
        }
    }
    
    return answer;
}
