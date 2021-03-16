def solution(land):
    r = len(land)
    for i in range(1,r):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    answer = max(land[r-1])
    return answer
