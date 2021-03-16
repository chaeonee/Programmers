def solution(a):
    answer = min(2,len(a))
    check = [False]*len(a)
    
    left = float('inf')
    for i in range(1,len(a)-1):
        left = min(left, a[i-1])
        if left > a[i]:
            check[i] = True
            answer += 1
            
    right = float('inf')
    for i in range(len(a)-2,0,-1):
        right = min(right,a[i+1])
        if right > a[i] and not check[i]:
            answer += 1
        
    return answer
