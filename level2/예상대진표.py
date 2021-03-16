def solution(n,a,b):
    n, answer = 2, 1
    while (a-1)//n != (b-1)//n:
        answer += 1
        n *= 2
    return answer
