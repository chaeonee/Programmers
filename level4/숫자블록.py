def getAliquot(num):
    ali = 1
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 and num // i <= 10000000:
            ali = num//i
            break
    return ali

def solution(begin, end):
    answer = [0]*(end-begin+1)
    start = max(2,begin)
    for num in range(start,end+1):
        n = getAliquot(num)
        answer[num-begin] = n
    return answer
