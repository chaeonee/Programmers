def solution(dartResult):
    score = []
    bonus = []
    
    oper = ''
    num = ''
    for r in dartResult:
        if r.isdecimal():
            if oper != '':
                bonus.append(oper)
                oper = ''
            num += r
        else:
            if num != '':
                score.append(int(num))
                num = ''
            oper += r
    bonus.append(oper)
    
    answer = 0
    pre_score = 0
    for n, b in zip(score,bonus):
        if len(b) == 2:
            tmp = 0
            if b[0] == 'S':
                tmp = n
            elif b[0] == 'D':
                tmp = int(pow(n,2))
            elif b[0] == 'T':
                tmp = int(pow(n,3))
                
            if b[1] == '*':
                answer -= pre_score
                answer += pre_score*2 + tmp*2
                pre_score = tmp*2
            elif b[1] == '#':
                pre_score = -tmp
                answer -= tmp
        else:
            if b == 'S':
                pre_score = n
                answer += n
            elif b == 'D':
                pre_score = int(pow(n,2))
                answer += int(pow(n,2))
            elif b == 'T':
                pre_score = int(pow(n,3))
                answer += int(pow(n,3))
                
    return answer
