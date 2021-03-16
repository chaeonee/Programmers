def solution(N, stages):
    fail = [[0]*2 for _ in range(N)]
    for stage in stages:
        for s in range(1,stage):
            fail[s-1][0] += 1
            
        if stage <= N:
            fail[stage-1][1] += 1
    
    for i in range(len(fail)):
        if fail[i][0]+fail[i][1] == 0:
            fail[i] = [i,0]
            continue
        fail[i][1] = fail[i][1]/(fail[i][0]+fail[i][1])
        fail[i][0] = i

    fail = list(sorted(fail, key = lambda x: (x[1], -x[0]), reverse = True))
    answer = []
    for f, _ in fail:
        answer.append(f+1)
    
    return answer
