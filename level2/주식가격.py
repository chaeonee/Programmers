def solution(prices):
    size = len(prices)
    answer = [0]*size
    
    s = []
    for i in range(size):
        while s:
            if prices[i] >= prices[s[-1]]:
                break
            answer[s[-1]] = i-s[-1]
            s.pop()
        s.append(i)
        
    while s:
        answer[s[-1]] = size-s[-1]-1
        s.pop()
    
    return answer
