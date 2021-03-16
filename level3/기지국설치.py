def solution(n, stations, w):
    l_range = 2*w+1
    answer, start = 0, 1
    for s in stations:
        end = max(1,s-w)
        if end-start == 0:
            start = min(n+1,s+w+1)
            continue
        answer += (end-start-1)//l_range+1
        start = s+w+1
    answer = answer + (n-start)//l_range+1 if start <= n else answer
    return answer
