def getNum(N,number):
    n_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    num = ''
    while number:
        num += n_list[number%N]
        number = number//N
    if num == '':
        return '0'
    return num[::-1]

def solution(n, t, m, p):
    answer = ''
    start, turn = -1, 0
    while True:
        start += 1
        number = getNum(n,start)
        for num in number:
            turn = (turn+1)%m
            if turn == p%m:
                answer += num
            if len(answer) == t:
                break
        if len(answer) == t:
            break
    return answer
