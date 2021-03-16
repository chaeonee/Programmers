def solution(n, times):
    min_t, max_t = 0, max(times)*n
    
    answer = max_t
    while min_t <= max_t:
        mid = (max_t+min_t)//2
        tmp = sum([mid//t for t in times])
        
        if tmp >= n:
            answer = min(answer,mid)
            max_t = mid-1
        else:
            min_t = mid+1
    
    return answer
