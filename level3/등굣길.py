def solution(m, n, puddles):
    road = [[0]*(m+1) for _ in range(n+1)]
    for py, px in puddles:
        road[px][py] = -1
    
    road[1][1] = 1
    for i in range(2,m+1):
        if road[1][i] == -1:
            road[1][i] = 0
            continue   
        road[1][i] = road[0][i] + road[1][i-1]
    for i in range(2,n+1):
        if road[i][1] == -1:
            road[i][1] = 0
            continue
        road[i][1] = road[i-1][1] + road[i][0]
        
    for i in range(2,n+1):
        for j in range(2,m+1):
            if road[i][j] == -1:
                road[i][j] = 0
                continue
            road[i][j] = (road[i-1][j] + road[i][j-1]) % 1000000007
            
    return road[n][m]
