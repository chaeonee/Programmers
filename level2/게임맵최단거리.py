from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    m_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    
    q = deque()
    q.append([0,0,1])
    
    visit = [[False]*m for _ in range(n)]
    visit[0][0] = True
    
    answer = -1
    while q:
        x, y, cnt = q.popleft()
        
        if x == n-1 and y == m-1:
            answer = cnt
            break
        
        for dx, dy in m_dir:
            dx += x
            dy += y
            if 0 <= dx < n and 0 <= dy < m and not visit[dx][dy] and maps[dx][dy]:
                visit[dx][dy] = True
                q.append([dx,dy,cnt+1])
    
    return answer
