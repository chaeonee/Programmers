def solution(board):
    r, c = len(board)+1, len(board[0])+1
    s = [[0]*c for _ in range(r)]
    
    answer = 0
    for i in range(1,r):
        for j in range(1,c):
            if board[i-1][j-1]:
                s[i][j] = min(s[i-1][j],s[i][j-1],s[i-1][j-1])+1
            answer = max(answer,s[i][j])
    
    return answer**2
