import itertools
import math

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    num = []
    for i in range(1,len(numbers)+1):
        tmp = list(map(''.join,itertools.permutations(numbers,i)))
        num += tmp
        
    num = list(map(int,num))
    num = list(set(num))
    
    for i in num:
        flag = 0
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                flag = 1
                break
        if flag == 0 and i > 1:
            answer += 1
    
    return answer
