import heapq

def solution(N, road, K):
    cost = [[float('inf')]*N for _ in range(N)]
    for a, b, c in road:
        cost[a-1][b-1] = min(c,cost[a-1][b-1])
        cost[b-1][a-1] = min(c,cost[b-1][a-1])
        
    visit = [False]*N
    
    answer = 0
    
    q = []
    heapq.heappush(q,[0,0])
    while q:
        c, pos = heapq.heappop(q)
        
        if not visit[pos]:
            answer += 1
            visit[pos] = True
            for i in range(N):
                if cost[pos][i] + c <= K and not visit[i]:
                    heapq.heappush(q,[cost[pos][i] + c,i])
    
    return answer
