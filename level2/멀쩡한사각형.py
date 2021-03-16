def getGCD(a, b):
    a, b = b, a%b
    while b:
        a, b = b, a%b    
    return a

def solution(w,h):    
    return w * h - (w + h - getGCD(w,h))
