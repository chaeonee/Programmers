def solution(n, money):
    answer = [0]*(n+1)
    for m in money:
        answer[m] = (answer[m] + 1) % 1000000007
        for i in range(m+1,n+1):
            answer[i] = (answer[i] + answer[i-m]) % 1000000007
    return answer[n]
