import heapq

def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap,s)
    
    answer = 0
    while heap[0] < K:   
        answer += 1
        f1 = heapq.heappop(heap)
        if not heap:
            answer = -1
            break
        f2 = heapq.heappop(heap)
        
        heapq.heappush(heap,f1+f2*2)
            
    return answer
