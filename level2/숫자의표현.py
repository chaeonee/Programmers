def solution(n):
    answer = 1
    for s in range(1,n//2+1):
        tmp_s = s
        tmp_n = n
        while tmp_n > 0:
            tmp_n -= tmp_s
            tmp_s += 1
        if tmp_n == 0:
            answer += 1
            
    return answer
