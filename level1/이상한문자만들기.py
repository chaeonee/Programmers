def solution(string):
    answer = ''
    i = 0
    for s in string:
        if s == ' ':
            i = 0
            answer += s
            continue
        answer = answer + s.lower() if i%2 else answer + s.upper()
        i += 1
        
    return answer
