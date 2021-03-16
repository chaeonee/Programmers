def solution(n):
    s = '수박'
    answer = ''.join([s[i%2] for i in range(n)] )
    return answer
