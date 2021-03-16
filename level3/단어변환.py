from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visit = {}
    candidate = [[] for _ in range(len(begin))]
    for word in words:
        visit[word] = False
        for i, w in enumerate(word):
            candidate[i].append(w)
    candidate = [list(set(c)) for c in candidate]
    
    q = deque()
    q.append([0,begin])
    
    answer = 0
    while q:
        n, w = q.popleft()
        
        if w == target:
            answer = n
            break
            
        for i, can in enumerate(candidate):
            for c in can:
                dw = w[:i]+c+w[i+1:]
                if dw in visit.keys() and not visit[dw]:
                    visit[dw] = True
                    q.append([n+1,dw])
    return answer
