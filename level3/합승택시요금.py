import heapq        

def getCost(n, s, fares):
    pq = []
    heapq.heappush(pq, [0,s])
    
    cost = [float('inf')]*n
    cost[s] = 0
    while pq:
        c, idx = heapq.heappop(pq)
        
        for i, f in enumerate(fares[idx]):
            if c+f < cost[i]:
                cost[i] = c+f
                heapq.heappush(pq,[c+f,i])
                
    return cost    
    
def solution(n, s, a, b, fares):
    fares_info = [[float('inf')]*n for _ in range(n)]
    for start, end, f in fares:
        fares_info[start-1][end-1] = min(fares_info[start-1][end-1],f)
        fares_info[end-1][start-1] = min(fares_info[end-1][start-1],f)
        
    s_cost = getCost(n, s-1, fares_info)
    a_cost = getCost(n, a-1, fares_info)
    b_cost = getCost(n, b-1, fares_info)
    
    answer = float('inf')
    for i in range(n):
        cost = s_cost[i] + a_cost[i] + b_cost[i]
        answer = min(answer,cost)
    
    return answer
