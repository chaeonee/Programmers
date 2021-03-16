import math

def solution(n):
    rule = ['4','1','2']
    
    answer = ''
    while n:
        answer = rule[n%3] + answer
        n = n // 3 if n % 3 else (n // 3)-1        
    return answer
