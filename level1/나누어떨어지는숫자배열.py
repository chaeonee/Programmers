def solution(arr, divisor):
    arr.sort()
    
    answer = []
    for n in arr:
        if not n % divisor:
            answer.append(n)
            
    if not answer:
        answer = [-1]
    
    return answer
