def solution(s):
    s_len = len(s)
    
    mid = int(s_len/2)
    answer = s[mid:mid+1] if s_len % 2 else s[mid-1:mid+1]
    
    return answer
