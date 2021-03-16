def check(n, x, board):
    for i in range(n):
        if board[i] != -1 and x != i and abs(x-i) == abs(board[x]-board[i]):
            return False
    return True

def selectPos(n, board, cnt, n_queen):
    if n_queen == n:
        cnt += 1
        return cnt
    for i in range(n):
        if board[i] != -1:
            continue
            
        board[i] = n_queen
        if check(n,i,board):
            cnt = selectPos(n,board,cnt,n_queen+1)
        board[i] = -1
    return cnt

def solution(n):
    board = [-1]*n
    return selectPos(n,board,0,0)
