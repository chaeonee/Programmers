from collections import deque

def solution(s):
    N = len(s)
    s = deque([i for i in s])
    
    pair = {j:i for i, j in [['(',')'],['[',']'],['{','}']]}
    
    answer = 0
    if N % 2:
        return answer
    
    for _ in range(N):
        n = s.append(s.popleft())
        
        flag = True
        stack = []        
        for i in s:
            if not i in pair.keys():
                stack.append(i)
            else:
                if not stack or stack.pop() != pair[i]:
                    flag = False
                    break
                    
        if flag:
            answer += 1
    
    return answer
