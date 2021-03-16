from collections import deque
def solution(priorities, location):
    answer = 0
    
    q = deque()
    for i in range(len(priorities)):
        q.append([i,priorities[i]])
    
    idx = priorities.index(max(priorities))
    while True:       
        n, x = q.popleft()
        if x == priorities[idx]:
            answer += 1
            if n == location:
                break            
            priorities.pop(idx)
            idx = priorities.index(max(priorities))
            continue
        q.append([n,x])
            
        
    return answer
