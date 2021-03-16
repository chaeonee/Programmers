from collections import deque

def solution(n, path_list, order_list):
    path = {}
    for s, e in path_list:
        if s not in path.keys():
            path[s] = [e]
        else:
            path[s].append(e)
        
        if e not in path.keys():
            path[e] = [s]
        else:
            path[e].append(s) 
            
    order = {}
    r_order = {}
    for s, e in order_list:
        order[s] = e
        r_order[e] = s
            
    visit = [False]*n
    visit[0] = True
    
    q = deque()
    q.append(0)
    while q:
        n -= 1
        room = q.popleft()
        
        if room not in path.keys():
            continue
        
        for r in path[room]:
            if visit[r]:
                continue
                
            visit[r] = True
            if r not in r_order.keys() or visit[r_order[r]]:
                q.append(r)
                if r in order.keys() and visit[order[r]]:
                    q.append(order[r])
    
    answer = True if not n else False
    
    return answer
