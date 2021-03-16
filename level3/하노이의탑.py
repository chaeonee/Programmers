def hanoi(n, pos, result):
    s, e, m = pos
    
    if n == 1:
        result.append([s,e])
        return result
    
    restult = hanoi(n-1,[s,m,e],result)
    result.append([s,e])
    restult = hanoi(n-1,[m,e,s],result)
    
    return result
    
    
def solution(n):
    answer = hanoi(n,[1,3,2],[])
    return answer
