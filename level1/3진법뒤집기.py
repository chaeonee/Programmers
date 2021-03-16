def getTernary(num):
    n = ''
    while num:
        n = str(num%3) + n
        num //= 3
    return n

def getDecimal(num):
    dec = 0
    for i, n in enumerate(num):
        dec += int(n)*pow(3,i)
    return dec

def solution(n):
    return getDecimal(getTernary(n))
