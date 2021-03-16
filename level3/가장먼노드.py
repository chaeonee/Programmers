import heapq

def solution(n, edge):
    vertex = {}
    for n1, n2 in edge:
        vertex[n1-1] = [n2-1] if n1-1 not in vertex.keys() else vertex[n1-1]+[n2-1]
        vertex[n2-1] = [n1-1] if n2-1 not in vertex.keys() else vertex[n2-1]+[n1-1]            
        
    dist = [float('inf')]*n
    dist[0] = 0
    
    q = []
    heapq.heappush(q,(0,0))
    while q:
        d, n = heapq.heappop(q)
        for i in vertex[n]:
            if dist[i] > d+1:
                dist[i] = d+1
                heapq.heappush(q,(d+1,i))
    
    max_dist = 0
    answer = 0
    for d in dist:
        if d > max_dist:
            max_dist = d
            answer = 1
        elif d == max_dist:
            answer += 1
            
    return answer
