def solution(string):
    answer = string[0].upper()
    for s in string[1:]:
        answer = answer + s.upper() if answer[-1] == ' ' else answer + s.lower()
    return answer
