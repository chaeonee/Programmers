def solution(absolutes, signs):
    N = len(absolutes)
    
    answer = 0
    for i in range(N):
        answer = answer + absolutes[i] if signs[i] else answer - absolutes[i]
    
    return answer
