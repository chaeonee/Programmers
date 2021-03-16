def getStart(t_end,t):
    if t_end[2] < t:
        t_end[1] -= 1
        t_end[2] = t_end[2] + 60 - t + 0.001
        
        if t_end[1] < 0:
            t_end[0] -= 1
            t_end[1] += 60
    else:
        t_end[2] -= t - 0.001
    
    if t_end[0] < 0:
        return 0
    else:
        for i in range(2):
            t_end[i] = str(int(t_end[i])).zfill(2)
        t_end[2] = str(int(t_end[2])).zfill(2) + '.' +list(str(round(t_end[2], 3)).split('.'))[1]
        
    return round(float(''.join(t_end)),3)

def afterSec(t_end):
    t_end[2] += 0.999
    for i in range(2,0,-1):
        if t_end[i] >= 60:
            t_end[i-1] += 1
            t_end[i] -= 60
            
    for i in range(2):
        t_end[i] = str(int(t_end[i])).zfill(2)
    t_end[2] = str(int(t_end[2])).zfill(2) + '.' +list(str(round(t_end[2], 3)).split('.'))[1] 
    
    return round(float(''.join(t_end)),3)
        

def solution(lines):
    lines = [list(map(float,l.replace("2016-09-15 ","").replace(":"," ").replace("s","").split())) for l in lines]
    
    start_time = []
    for l in lines:
        start_time.append(getStart(l[:3],l[3]))
        
    answer = 1
    n = len(start_time)
    for i in range(n-1):
        t = afterSec(lines[i][:3])
        tmp = 1
        for j in range(i+1,n):
            if start_time[j] <= t:
                tmp += 1
        answer = max(answer,tmp)
    
    return answer
