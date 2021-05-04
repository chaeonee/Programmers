from collections import deque
from itertools import permutations

def moveCtrl(r, c, dirs, board):    
    while True:
        dr, dc = r + dirs[0], c + dirs[1]
        if dr < 0 or dr >= 4 or dc < 0 or dc >= 4:
            break
            
        r, c = dr, dc
        if board[dr][dc]:
            break
        
    return r, c

def getDist(start, end, board):
    m_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    
    visit = [[False]*4 for _ in range(4)]
    visit[start[0]][start[1]] = True
    
    q = deque()
    q.append(start+[0])
    
    dist = 0
    while q:
        r, c, d = q.popleft()
        if [r, c] == end:
            dist = d
            break
            
        for dr, dc in m_dir:
            dr += r
            dc += c
            if 0 <= dr < 4 and 0 <= dc < 4 and not visit[dr][dc]:
                q.append([dr,dc,d+1])
                visit[dr][dc] = True
            
        for dr, dc in m_dir:
            dr, dc = moveCtrl(r,c,[dr,dc],board)
            if 0 <= dr < 4 and 0 <= dc < 4 and not visit[dr][dc]:
                q.append([dr,dc,d+1])
                visit[dr][dc] = True
    
    return dist

def solution(board, r, c):
    card = {}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in card.keys():
                    card[board[i][j]] = []
                card[board[i][j]].append([i,j])
    
    answer = float('inf')
    permute = list(permutations(list(card.keys())))
    for perm in permute:
        q = deque([[r,c,0]])
        tmp_board = [[board[i][j] for j in range(4)] for i in range(4)]
        for p in perm:
            l = len(q)
            for _ in range(l):
                x, y, d = q.popleft()

                c1, c2 = getDist([x,y],card[p][0],tmp_board), getDist([x,y],card[p][1],tmp_board)
                dist1 = getDist(card[p][0],card[p][1],tmp_board) + 2
                dist2 = getDist(card[p][1],card[p][0],tmp_board) + 2
                
                q.append([card[p][0][0],card[p][0][1],d+dist2+c2])
                q.append([card[p][1][0],card[p][1][1],d+dist1+c1])

            tmp_board[card[p][0][0]][card[p][0][1]] = tmp_board[card[p][1][0]][card[p][1][1]] = 0
        
        while q:
            answer = min(answer,q.popleft()[-1])
    
    return answer
