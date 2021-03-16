import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for i in range(len(progresses)):
        q.append(int(math.ceil((100-progresses[i])/speeds[i])))
        
    while q:
        n = 1
        x = q.popleft()
        
        while q and q[0] <= x:
            n += 1
            q.popleft()
        answer.append(n)
        
        
    
    return answer
