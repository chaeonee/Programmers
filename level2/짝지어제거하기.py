def solution(S):
    stack = [S[0]] 
    for s in S[1:]:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
            
    answer = 0 if stack else 1
    
    return answer
