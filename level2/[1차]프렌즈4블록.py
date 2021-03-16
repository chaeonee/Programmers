def rearrangeBlock(board):
    m, n = len(board), len(board[0])
    
    blank = [-1]*n
    for j in range(n):
        for i in range(m-1,-1,-1):
            if board[i][j] == '0':
                blank[j] = i
                break
                
    for j in range(n):
        s = blank[j] - 1
        for i in range(s,-1,-1):
            if board[i][j] != '0':
                board[blank[j]][j] = board[i][j]
                board[i][j] = '0'
                blank[j] -= 1
                
    return board

def removeBlock(board, remove_list):
    for x, y in remove_list:
        board[x][y] = '0'
    return rearrangeBlock(board)

def solution(m, n, board):
    board = [list(x) for x in board]
    
    answer = 0
    check_dir = [[0,0],[1,0],[0,1],[1,1]]
    while True:
        remove_list = []
        visit = [[False]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                    
                cur = board[i][j]
                if board[i+1][j] == board[i][j+1] == board[i+1][j+1] == cur:
                    for dx, dy in check_dir:
                        dx += i
                        dy += j
                        if not visit[dx][dy]:
                            visit[dx][dy] = True
                            remove_list.append([dx,dy])
                
        if len(remove_list) == 0:
            break
                
        answer += len(remove_list)
        board = removeBlock(board, remove_list)
                           
    return answer
