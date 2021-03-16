def solution(n, lost, reserve):
    answer = n
    
    uniform = [1] * n
    for l in lost:
        if l not in reserve:
            answer -= 1
            
        uniform[l-1] -= 1
    for r in reserve:
        uniform[r-1] += 1
    
    reserve.sort()
    for r in reserve:
        if r >= 2 and uniform[r-1] > 1 and not uniform[r-2]:
            answer += 1
            uniform[r-2] += 1
        elif r < n and uniform[r-1] > 1 and not uniform[r]:
            answer += 1
            uniform[r] += 1
            
    return answer
