def checkPole(n,x,y,town):
    flag = False
    if y == 0 or town[y-1][x][0] or town[y][x][1] or (x > 0 and town[y][x-1][1]):
        flag = True
    
    return flag

def checkBeam(n,x,y,town):
    flag = False
    if town[y-1][x][0] or town[y-1][x+1][0]:
        flag = True
    elif (x > 0 and town[y][x-1][1]) and (x < n and town[y][x+1][1]):
        flag = True
        
    return flag

def check(n,x,y,town): 
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i < 0 or i > n or j < 0 or j > n:
                continue
            
            if town[j][i][0]:
                if not checkPole(n,i,j,town):
                    return False
            if town[j][i][1]:
                if not checkBeam(n,i,j,town):
                    return False
                
    return True

def solution(n, build_frame):
    town = [[[0]*2 for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        town[y][x][a] = 1 if b else 0
        
        if not check(n,x,y,town):
            town[y][x][a] = 0 if b else 1
        
            
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if town[j][i][0]:
                answer.append([i,j,0])
            if town[j][i][1]:
                answer.append([i,j,1])
                
    return answer
