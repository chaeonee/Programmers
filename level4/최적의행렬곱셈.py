def solution(matrix_sizes):
    n = len(matrix_sizes)
    matrix_sizes = [matrix_sizes[0][0]] + [matrix_sizes[i][1] for i in range(n)]
    
    matrix = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
        
    for k in range(1,n):
        for i in range(n):
            if i+k >= n:
                continue
                
            for j in range(i,i+k):
                matrix[i][i+k] = min(matrix[i][i+k], matrix[i][j] + matrix[j+1][i+k]+matrix_sizes[i]*matrix_sizes[j+1]*matrix_sizes[i+k+1])
    
    return matrix[0][n-1]
