def solution(x):
    answer = True if not x%sum([int(i) for i in str(x)]) else False
    return answer
