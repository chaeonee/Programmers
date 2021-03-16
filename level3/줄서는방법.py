def getFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

def solution(n, k):
    people = [i for i in range(1,n+1)]
    answer = []
    while people:
        n -= 1
        f = getFactorial(n)
        if k%f:
            answer.append(people.pop(k//f))
            k = k % f
        else:
            answer.append(people.pop(k//f-1))
            while people:
                answer.append(people.pop())
    return answer
