from collections import deque

def putBlack(board):
    N = len(board)
    
    for j in range(N):
        for i in range(N):
            if board[i][j] > 0:
                break
            board[i][j] = -1
            
    return board

def getCoordinate(board):
    N = len(board)
    check_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    
    coord = []
    visit = [[False]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if visit[i][j] or board[i][j] <= 0:
                continue
            
            q = deque()
            q.append([i,j])
            
            s, e = [float('inf'),float('inf')],[-1,-1]
            while q:
                x, y = q.popleft()
                
                s[0] = min(s[0],x)
                s[1] = min(s[1],y)
                e[0] = max(e[0],x)
                e[1] = max(e[1],y)
                
                for dx, dy in check_dir:
                    dx += x
                    dy += y
                    if 0 <= dx < N and 0 <= dy < N:
                        if not visit[dx][dy] and board[x][y] == board[dx][dy]:
                            visit[dx][dy] = True
                            q.append([dx,dy])
            
            coord.append([s,e])
            
    return coord            
                
def solution(board):
    board = putBlack(board)
    coord = getCoordinate(board)
    
    answer = 0
    change = True
    while change:
        n_coord = len(coord)
        
        change = False
        for _ in range(n_coord):
            s, e = coord.pop(0)

            num = board[s[0]][s[1]] if board[s[0]][s[1]] != -1 else board[e[0]][e[1]]
            flag = True
            for i in range(s[0],e[0]+1):
                for j in range(s[1],e[1]+1):
                    if board[i][j] != -1 and board[i][j] != num:
                        flag = False
                        break
                if not flag:
                    break

            if not flag:
                coord.append([s,e])
            else:
                answer += 1
                change = True
                for i in range(s[0],e[0]+1):
                    for j in range(s[1],e[1]+1):
                        board[i][j] = 0
                board = putBlack(board)
                
        
    return answer
