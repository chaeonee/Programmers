def solution(arr):
    n = (len(arr)+1)//2
    min_arr = [[float('inf')]*n for _ in range(n)]
    max_arr = [[-1*float('inf')]*n for _ in range(n)]
    
    for i in range(n):
        min_arr[i][i] = int(arr[2*i])
        max_arr[i][i] = int(arr[2*i])
    
    for k in range(1,n):
        for i in range(n):
            if i+k >= n:
                continue
                
            for j in range(i,i+k):
                if arr[2*j+1] == '+':
                    max_arr[i][i+k] = max(max_arr[i][i+k], max_arr[i][j]+max_arr[j+1][i+k])
                    min_arr[i][i+k] = min(min_arr[i][i+k], min_arr[i][j]+min_arr[j+1][i+k])
                else:
                    max_arr[i][i+k] = max(max_arr[i][i+k], max_arr[i][j]-min_arr[j+1][i+k])
                    min_arr[i][i+k] = min(min_arr[i][i+k], min_arr[i][j]-max_arr[j+1][i+k])
    
    return max_arr[0][n-1]
