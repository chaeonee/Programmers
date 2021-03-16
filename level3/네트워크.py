def solution(n, computers):
    answer = 0

    visit = [0]*n
    stack = []
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            for j in range(n):
                if computers[i][j] == 1:
                    stack.append(j)
                    computers[i][j] = 0
                    computers[j][i] = 0    
                    
            while stack:
                num = stack.pop()
                if visit[num] == 0:
                    visit[num] = 1
                    for j in range(n):
                        if computers[num][j] == 1:
                            stack.append(j)
                            computers[num][j] = 0
                            computers[j][num] = 0                            
            answer += 1
                                
    return answer
