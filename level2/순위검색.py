import bisect
from itertools import combinations

def addInfo(info, info_list):
    score = int(info[-1])
    info = info[:-1]
    
    for i in range(5):
        comb = list(combinations(info,i))
        for c in comb:
            key = ''.join(c)
            if key not in info_list:
                info_list[key] = []
            info_list[key].append(score)
    
    if '-' not in info_list:
        info_list['-'] = []
    info_list['-'].append(score)
        
    return info_list

def searchQuery(query, score, info_list):
    if query == '':
        query = '-'
        
    if query not in info_list:
        return 0
    
    score_list = info_list[query]
            
    return len(score_list)-bisect.bisect_left(score_list, score)
            
def solution(information, query):
    info_list = {}
    for info in information:
        info = info.split()
        info_list = addInfo(info, info_list)
        
    for k in info_list.keys():
        info_list[k].sort()
    
    answer = [0]*len(query)
    for n, q in enumerate(query):
        q = q.split()
        q, score = [i for i in q[:-1] if i != 'and' and i != '-'], int(q[-1])
        answer[n] = searchQuery(''.join(q),score,info_list)
        
    return answer
