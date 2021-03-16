def factorial(n):
    fac = 1
    for i in range(2,n+1):
        fac *= i
    return fac

def solution(n):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[0][i] = 1
    
    for i in range(1,n+1):
        for j in range(i,n+1):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    
    return dp[n][n]
    #return (factorial(2*n)/(factorial(n)**2))//(n+1)
