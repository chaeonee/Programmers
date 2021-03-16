def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    answer = days[(sum(months[:a-1])+b+4)%7]
    
    return answer
