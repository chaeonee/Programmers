def rotateKey(M,key):
    newKey = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            newKey[j][M-1-i] = key[i][j] 
        
    return newKey
        
def makeKey(M,N,end,key):
    unlock = [[0]*N for _ in range(N)]
    
    end_x, end_y = end
    for i in range(end_x+1):
        for j in range(end_y+1):
            x = M - (end_x - i) - 1
            y = M - (end_y - j) - 1
            if 0 <= x < M and 0 <= y < M and 0 <= i < N and 0 <= j < N:
                unlock[i][j] = key[x][y]
                
    return unlock

def solution(key, lock):
    answer = False
    
    M = len(key)
    N = len(lock)
    
    for _ in range(4):
        for i in range(M+N-1):
            for j in range(M+N-1):
                unlock = makeKey(M,N,[i,j],key)
                
                flag = True
                for x in range(N):
                    for y in range(N):
                        if lock[x][y] == unlock[x][y]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    answer = True
                    return answer
                
        key = rotateKey(M,key)       
            
    return answer
