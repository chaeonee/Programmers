def isCorrect(word):
    if word[0] == ')':
        return False
    
    num = 1
    for w in word[1:]:
        num = num + 1 if w == '(' else num - 1
        if num < 0:
            return False
    
    return True
    

def splitString(word):
    if word == '':
        return word
    
    num = 1 if word[0] == '(' else -1
        
    idx = 1
    for w in word[1:]:
        idx += 1
        
        num = num + 1 if w == '(' else num - 1
        if num == 0:
            break
            
    u = word[:idx]
    v = word[idx:]
    v = splitString(v)
    
    answer = ''
    if not isCorrect(u):
        answer = '(' + v + ')'
        for i in u[1:-1]:
            answer = answer + ')' if i == '(' else answer + '('
    else:
        answer = u+v
        
    return answer

def solution(p):
    answer = splitString(p)
    return answer
