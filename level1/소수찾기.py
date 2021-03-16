def solution(n):
    answer = 0
    arr = [False]*(n+1)
    for i in range(2,n+1):
        if not arr[i]:
            answer += 1
        for j in range(i,n+1,i):
            arr[j] = True
    return answer
