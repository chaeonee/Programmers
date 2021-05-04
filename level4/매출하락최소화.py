def solution(sales, links):
    N = len(sales)
    teams = {}
    for a, b in links:
        if a-1 not in teams.keys():
            teams[a-1] = []
        teams[a-1].append(b-1)
    
    stack = [0]
    visit = [False]*N
    loss = [[-1]*N for _ in range(2)]
    while stack:
        n = stack[-1]
        if n in teams.keys() and not visit[n]:
            visit[n] = True
            for c in teams[n]:
                stack.append(c)
            continue
            
        stack.pop()
        
        flag = True
        loss[0][n], loss[1][n] = 0, sales[n]
        if n in teams.keys():
            tmp, sub = 0, float('inf')
            for c in teams[n]:
                tmp += min(loss[0][c], loss[1][c])
                sub = min(sub,loss[1][c]-loss[0][c])
                if loss[0][c] > loss[1][c]:
                    flag = False
                
            loss[0][n] += tmp
            loss[1][n] += tmp
            
            if flag:
                loss[0][n] += sub
                
    return min(loss[0][0],loss[1][0])
