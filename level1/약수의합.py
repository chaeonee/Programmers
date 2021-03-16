def solution(n):
    answer = n + sum([i for i in range(1,int(n/2)+1) if not n%i])
    return answer
