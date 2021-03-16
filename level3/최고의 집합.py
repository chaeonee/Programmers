def solution(n, s):
    if s//n == 0:
        return [-1]
    
    answer = [s//n]*n
    for i in range(s%n):
        answer[n-i-1] += 1
    
    return answer
