from collections import deque

def solution(S):
    q = deque()
    
    answer = True
    for s in S:
        if s == '(':
            q.append('(')
        else:
            if not q:
                answer = False
                break
            q.popleft()
                
    if q:
        answer = False

    return answer
