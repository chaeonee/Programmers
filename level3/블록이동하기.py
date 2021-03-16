from collections import deque    
def solution(board):
    answer = 0
    
    N = len(board)
    visit = [[[False]*2 for _ in range(N)] for _ in range(N)]
    visit[0][0][0] = True
    
    q = deque()
    q.append([[0,0],[0,1],0])
    while q:
        robot1, robot2, n = q.popleft()
        if robot2[0] == N-1 and robot2[1] == N-1:
            answer = n
            break
        
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        for dx, dy in dir:
            d_robot1 = [robot1[0]+dx, robot1[1]+dy]
            d_robot2 = [robot2[0]+dx, robot2[1]+dy]
            
            if 0 <= d_robot1[0] < N and 0 <= d_robot1[1] < N and 0 <= d_robot2[0] < N and 0 <= d_robot2[1] < N:
                if d_robot1[0] == d_robot2[0]:
                    if not visit[d_robot1[0]][d_robot1[1]][0] and not board[d_robot1[0]][d_robot1[1]] and not board[d_robot2[0]][d_robot2[1]]:
                        visit[d_robot1[0]][d_robot1[1]][0] = True
                        q.append([d_robot1,d_robot2,n+1])
                else:
                    if not visit[d_robot1[0]][d_robot1[1]][1] and not board[d_robot1[0]][d_robot1[1]] and not board[d_robot2[0]][d_robot2[1]]:
                        visit[d_robot1[0]][d_robot1[1]][1] = True
                        q.append([d_robot1,d_robot2,n+1])
        
        if robot1[0] == robot2[0]:
            if robot1[0] > 0 and robot2[0] > 0 and not board[robot2[0]-1][robot2[1]] and not board[robot1[0]-1][robot1[1]]:
                if not visit[robot1[0]-1][robot1[1]][1]:
                    visit[robot1[0]-1][robot1[1]][1] = True
                    q.append([[robot1[0]-1,robot1[1]],robot1,n+1])
                    
            if robot1[0] < N-1 and robot2[0] < N-1 and not board[robot2[0]+1][robot2[1]] and not board[robot1[0]+1][robot1[1]]:
                if not visit[robot1[0]][robot1[1]][1]:
                    visit[robot1[0]][robot1[1]][1] = True
                    q.append([robot1,[robot1[0]+1,robot1[1]],n+1])
            
            if robot1[0] > 0 and robot2[0] > 0 and not board[robot2[0]-1][robot2[1]] and not board[robot1[0]-1][robot1[1]]:
                if not visit[robot2[0]-1][robot2[1]][1]:
                    visit[robot2[0]-1][robot2[1]][1] = True
                    q.append([[robot2[0]-1,robot2[1]],robot2,n+1])
                    
            if robot1[0] < N-1 and robot2[0] < N-1 and not board[robot2[0]+1][robot2[1]] and not board[robot1[0]+1][robot1[1]]:
                if not visit[robot2[0]][robot2[1]][1]:
                    visit[robot2[0]][robot2[1]][1] = True
                    q.append([robot2,[robot2[0]+1,robot2[1]],n+1])       
        else:
            if robot1[1] > 0 and robot2[1] > 0 and not board[robot2[0]][robot2[1]-1] and not board[robot1[0]][robot1[1]-1]:
                if not visit[robot1[0]][robot1[1]-1][0]:
                    visit[robot1[0]][robot1[1]-1][0] = True
                    q.append([[robot1[0],robot1[1]-1],robot1,n+1])
                    
            if robot1[1] < N-1 and robot2[1] < N-1 and not board[robot2[0]][robot2[1]+1] and not board[robot1[0]][robot1[1]+1]:
                if not visit[robot1[0]][robot1[1]][0]:
                    visit[robot1[0]][robot1[1]][0] = True
                    q.append([robot1,[robot1[0],robot1[1]+1],n+1])
            
            if robot1[1] > 0 and robot2[1] > 0 and not board[robot2[0]][robot2[1]-1] and not board[robot1[0]][robot1[1]-1]:
                if not visit[robot2[0]][robot2[1]-1][0]:
                    visit[robot2[0]][robot2[1]-1][0] = True
                    q.append([[robot2[0],robot2[1]-1],robot2,n+1])
                    
            if robot1[1] < N-1 and robot2[1] < N-1 and not board[robot2[0]][robot2[1]+1] and not board[robot1[0]][robot1[1]+1]:
                if not visit[robot2[0]][robot2[1]][0]:
                    visit[robot2[0]][robot2[1]][0] = True
                    q.append([robot2,[robot2[0],robot2[1]+1],n+1])
    
    return answer
