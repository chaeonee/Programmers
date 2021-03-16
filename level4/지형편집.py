def getCost(N, h, P, Q, land):
    cost = 0
    for i in range(N):
        for j in range(N):
            if h > land[i][j]:
                cost += (h - land[i][j]) * P
            elif h < land[i][j]:
                cost += (land[i][j] - h) * Q
    return cost

def solution(land, P, Q):
    N = len(land)
    land = [land[i][j] for i in range(N) for j in range(N)]
    land.sort()
    
    N = len(land)
    n_total = sum(land)
    
    pre = 0
    answer = float('inf')
    for n in range(N):
        cost = 0
        cur = land[n]
        cost += (n*cur-pre) * P
        
        pre += cur
        cost += (n_total-pre-((N-n-1)*cur)) * Q
        
        answer = min(answer,cost)
        
    return answer
