def solution(s):
    answer = True if s.isdecimal() and (len(s) == 4 or len(s) == 6) else False
    return answer
