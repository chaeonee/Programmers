import heapq
from collections import deque

def getArea(n, height, land, area):
    move_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    
    num = 0
    sub = []
    for i in range(n):
        for j in range(n):
            if area[i][j]:
                continue
            
            num += 1
            
            q = deque()
            q.append([i,j])
            
            area[i][j] = num
            
            while q:
                x, y = q.popleft()
                
                for dx, dy in move_dir:
                    dx += x
                    dy += y
                    
                    if 0 <= dx < n and 0 <= dy < n:
                        if abs(land[x][y] - land[dx][dy]) <= height and not area[dx][dy]:
                            area[dx][dy] = num
                            q.append([dx,dy])
                        elif abs(land[x][y] - land[dx][dy]) > height:
                            heapq.heappush(sub, [abs(land[x][y] - land[dx][dy]),[x,y],[dx,dy]])
                            
                            
    return area, sub, num

def Union(a, b, parent):
    pa = Find(a, parent)
    pb = Find(b, parent)
    if pa >= pb:
        parent[pa] = pb
    else:
        parent[pb] = pa
    return parent

def Find(a, parent):
    while a != parent[a]:
        a = parent[a]
    return a

def getCost(n, n_land, sub, area):
    parent = [i for i in range(n_land+1)]
    
    cost = 0
    while sub:
        c, s, e = heapq.heappop(sub)
        if Find(area[s[0]][s[1]], parent) == Find(area[e[0]][e[1]], parent):
            continue
        
        cost += c
        parent = Union(area[s[0]][s[1]],area[e[0]][e[1]],parent)
        
    return cost
            

def solution(land, height):
    n = len(land)
    area, sub, n_land = getArea(n,height,land,[[0]*n for _ in range(n)])
    
    cost = getCost(n,n_land,sub,area)
    
    return cost
