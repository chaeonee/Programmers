def solution(n):
    if n % 2:
        return 0
    
    n = n//2
    tile = [0]*n
    tile[0] = 3
    
    for i in range(1,n):
        tile[i] = (3*tile[i-1] + 2) % 1000000007
        
        for j in range(i-1):
            tile[i] = (tile[i] + 2*tile[j]) % 1000000007
    
    return tile[n-1]
