from collections import deque

def solution(str_list, t):
    strs = {}
    for st in str_list:
        s = st[0]
        if s not in strs.keys():
            strs[s] = []
        strs[s].append(st)
        
    if t[0] not in strs.keys():
        return -1
    
    q = deque()
    visit = [False]*len(t)
    for s in strs[t[0]]:
        n = len(s)
        if t[:n] == s:
            q.append([1,n-1,t[n:]])
            visit[n-1] = True
            
    answer = -1
    while q:
        cnt, leng, st = q.popleft()
        
        if st == '':
            answer = cnt
            break
            
        if st[0] not in strs.keys():
            continue
        
        for s in strs[st[0]]:
            n = len(s)
            if st[:n] == s and not visit[leng+n]:
                q.append([cnt+1,leng+n,st[n:]])
                visit[leng+n] = True
        
    return answer
