import heapq

def solution(n, works):
    q = []
    for w in works:
        heapq.heappush(q,-w)
        
    while q and n:
        n -= 1
        w = heapq.heappop(q)
        if w+1:
            heapq.heappush(q,w+1)
    answer = sum([i**2 for i in q])
    return answer
