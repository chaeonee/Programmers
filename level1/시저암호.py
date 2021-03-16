import string 
 
def solution(s, n):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    answer = ''
    for i in s:
        answer = answer + i if i == ' ' else answer + lower[(lower.index(i)+n)%26] if 'a' <= i <= 'z' else answer + upper[(upper.index(i)+n)%26]  
    return answer
