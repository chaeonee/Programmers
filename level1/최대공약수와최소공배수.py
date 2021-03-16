def getGCD(a, b):
    while a:
        a, b = b%a, a
    return b

def solution(n, m):
    gcd = getGCD(n,m)
    answer = [gcd,(n*m)//gcd]        
    return answer
