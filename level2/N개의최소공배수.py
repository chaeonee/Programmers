def getGCD(a,b):
    while a:
        a, b = b%a, a
    return b

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    
    gcd = getGCD(arr[0],arr[1])
    answer = (arr[0]*arr[1])//gcd
    for n in arr[2:]:
        gcd = getGCD(answer,n)
        answer = (answer*n)//gcd
    
    return answer
