def solution(d, budget):
    d.sort()
    
    answer, b_sum = 0, 0
    for i in d:
        if b_sum+i > budget:
            break
        b_sum += i
        answer += 1
    
    return answer
