def solution(n):
    n_one = format(n, 'b').count('1')
    
    answer = n
    while True:
        answer += 1
        if format(answer, 'b').count('1') == n_one:
            break
        
    return answer
