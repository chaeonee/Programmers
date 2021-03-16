def solution(s):
    p_cnt = s.count('p')+s.count('P')
    y_cnt = s.count('y')+s.count('Y')
    
    answer = True if p_cnt == y_cnt else False
    
    return answer
