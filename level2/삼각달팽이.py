def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
        
    num = 0
    x_start, x_end, y_start, y_end = 0, n-1, 0, n-1
    while x_start <= x_end:
        print(x_start, x_end, y_start, y_end)
        for i in range(x_start,x_end+1):
            num += 1
            answer[i][y_start] = num
            
        for i in range(y_start+1,y_end):
            num += 1
            answer[x_end][i] = num
        
        tmp = y_end
        for i in range(x_end,x_start,-1):
            num += 1
            answer[i][tmp] = num
            tmp -= 1
        
        x_start += 2
        x_end -= 1
        y_start += 1
        y_end -= 2
        
    return sum(answer, [])
