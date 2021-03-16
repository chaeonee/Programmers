def solution(board, moves):
    top_idx = []
    N = len(board)
    for j in range(N):
        flag = False
        for i in range(N):
            if board[i][j] != 0:
                flag = True
                top_idx.append(i)
                break
        if not flag:
            top_idx.append(N)
    
    answer = 0
    stack = []
    for m in moves:
        if top_idx[m-1] >= N:
            continue
            
        if stack and stack[-1] == board[top_idx[m-1]][m-1]:
            answer += 2
            stack.pop()
        else:
            stack.append(board[top_idx[m-1]][m-1])
            
        board[top_idx[m-1]][m-1] = 0
        top_idx[m-1] += 1
    
    return answer
