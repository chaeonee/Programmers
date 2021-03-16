def solution(number, k):
    i = 0
    while k:
        k -= 1
        for _ in range(i,len(number)):
            if i+1 == len(number):
                number = number[:-1]
                break
                
            if int(number[i]) < int(number[i+1]):
                number = number[:i]+number[i+1:]
                i = max(i-1,0)
                break
            i += 1
        
    return number
