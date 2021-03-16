def solution(sticker):
    n = len(sticker)
    
    s_sum = [[0]*n for _ in range(2)]
    s_sum[0][0] = sticker[0]
    
    for i in range(1,n):
        if i == 1:
            s_sum[0][i] = sticker[i]
            s_sum[1][i] = sticker[i]
            continue
        elif i == n-1:
            s_sum[0][i] = max(s_sum[0][i-1],s_sum[0][i-2],s_sum[0][i-3])
        elif i == 2:
            s_sum[0][i] = s_sum[0][i-2] + sticker[i]
            s_sum[1][i] = s_sum[1][i-2] + sticker[i]
            continue
        else:
            s_sum[0][i] = max(s_sum[0][i-2],s_sum[0][i-3]) + sticker[i]
        s_sum[1][i] = max(s_sum[1][i-2],s_sum[1][i-3]) + sticker[i]
    
    return max(s_sum[0][n-1],s_sum[1][n-1])
