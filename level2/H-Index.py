def solution(citations):
    citations.sort()
    
    answer = 0
    c_len = len(citations)
    for i in range(c_len,0,-1):
        if i <= citations[c_len-i]:
            answer = i
            break
              
    return answer
