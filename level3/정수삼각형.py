def solution(triangle):
    t_sum = [[0]*(i+2) for i in range(1,len(triangle)+1)]
    t_sum[0][1] = triangle[0][0]
    for i in range(1,len(t_sum)):
        for j in range(1,len(t_sum[i])-1):
            t_sum[i][j] = max(t_sum[i-1][j-1], t_sum[i-1][j]) + triangle[i][j-1]
    print(t_sum)
    return max(t_sum[-1])
