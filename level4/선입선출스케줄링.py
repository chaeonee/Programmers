import math

def solution(n, cores):
    left, right = 0, max(cores)*n
    
    answer = 0
    while left <= right:
        mid = (right+left)//2
        
        num = sum([((mid-1)//c)+1 for c in cores])
        if num >= n:
            right = mid - 1
        else:
            left = mid + 1
            
            for i, c in enumerate(cores):
                if not mid % c:
                    num += 1
                    if num == n:
                        answer = i + 1
                        
    return answer
