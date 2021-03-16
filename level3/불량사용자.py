from itertools import product

def getBanned(s,candidate,ban_list,result):
    if s == len(candidate):
        result.append(sorted([i for i in ban_list]))
        return result
    
    for c in candidate[s]:
        if c in ban_list:
            continue
        ban_list.append(c)
        result = getBanned(s+1,candidate,ban_list,result)
        ban_list.pop()
        
    return result
    
def solution(user_id, banned_id):
    unknown = []
    for banned in banned_id:
        tmp = []
        for i, b in enumerate(banned):
            if b == '*':
                tmp.append(i)
        unknown.append(tmp)
        
    candidate = [[] for _ in range(len(banned_id))]
    for user in user_id:
        for i, un in enumerate(unknown):
            if len(user) != len(banned_id[i]):
                continue
            tmp = list(user)
            for u in un:
                tmp[u] = '*'
            if ''.join(tmp) == banned_id[i]:
                candidate[i].append(user)
    answer = len(list(set(tuple(tuple(i) for i in getBanned(0,candidate,[],[])))))
    return answer
