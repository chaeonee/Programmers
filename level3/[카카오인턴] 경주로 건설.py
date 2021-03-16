def solution(board):
    N = len(board)
    cost = [[[float('inf')]*N for _ in range(N)] for _ in range(4)] # 방향, x, y
    for i in range(4):
        cost[i][0][0] = 0
    
    d_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    q = [[1,0,0],[3,0,0]]
    while q:
        d, x, y = q.pop(0)
        if x == N-1 and y == N-1:
            continue
        
        for i, tmp_dir in enumerate(d_dir):
            dx, dy = x+tmp_dir[0], y+tmp_dir[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
                
            if i == d and cost[i][dx][dy] > cost[d][x][y] + 100 and not board[dx][dy]:
                q.append([i,dx,dy])
                cost[i][dx][dy] = cost[d][x][y] + 100
            elif i != d and cost[i][dx][dy] > cost[d][x][y] + 600 and not board[dx][dy]:
                q.append([i,dx,dy])
                cost[i][dx][dy] = cost[d][x][y] + 600
        
    answer = min(cost[0][N-1][N-1],cost[1][N-1][N-1],cost[2][N-1][N-1],cost[3][N-1][N-1])
    return answer
