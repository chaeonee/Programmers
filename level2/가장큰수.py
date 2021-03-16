from functools import cmp_to_key

def cmp(a,b):
    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1 
    return 0

def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers = sorted(numbers, key=cmp_to_key(cmp))
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer
