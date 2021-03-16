def solution(arrows):
    m_dir = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    r_dir = [4,5,6,7,0,1,2,3]
    
    edge = {}    
    x, y = 0, 0    
    answer = 0
    for i, arrow in enumerate(arrows):        
        dx = x + m_dir[arrow][0]
        dy = y + m_dir[arrow][1]
        
        if dx in edge.keys() and dy in edge[dx].keys() and not edge[dx][dy][r_dir[arrow]]:
            answer += 1
        
            if arrow % 2:
                tmp_dir = [[0,1],[1,0],[0,-1],[-1,0]]

                tmp_x = x + tmp_dir[arrow//2][0]
                tmp_y = y + tmp_dir[arrow//2][1]

                tmp_arrow = (arrow+2)%8
                if tmp_x in edge.keys() and tmp_y in edge[tmp_x].keys() and edge[tmp_x][tmp_y][tmp_arrow]:
                    answer += 1
                    
        elif dx not in edge.keys() or (dx in edge.keys() and dy not in edge[dx].keys()):
            if arrow % 2:
                tmp_dir = [[0,1],[1,0],[0,-1],[-1,0]]

                tmp_x = x + tmp_dir[arrow//2][0]
                tmp_y = y + tmp_dir[arrow//2][1]

                tmp_arrow = (arrow+2)%8
                if tmp_x in edge.keys() and tmp_y in edge[tmp_x].keys() and edge[tmp_x][tmp_y][tmp_arrow]:
                    answer += 1
        
        if x not in edge.keys():
            edge[x] = {}
        if y not in edge[x].keys():
            edge[x][y] = [False]*8
        edge[x][y][arrow] = True
        
        x, y = dx, dy
        if x not in edge.keys():
            edge[x] = {}
        if y not in edge[x].keys():
            edge[x][y] = [False]*8
        edge[x][y][r_dir[arrow]] = True
            
    return answer
