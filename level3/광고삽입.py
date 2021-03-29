def StrtoSec(str_time):
    str_time = str_time.split(':')
    
    time, num = 0, 3600
    for t in str_time:
        time += int(t)*num
        num //= 60
    
    return time

def SectoStr(time):    
    hour = time//3600
    time %= 3600
    minute = time//60
    time %= 60
        
    return '{:02d}:{:02d}:{:02d}'.format(hour,minute,time)

def solution(play_time, adv_time, logs):
    play_time = StrtoSec(play_time)
    adv_time = StrtoSec(adv_time)
    
    n_time = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = log.split('-')
        start = StrtoSec(start)
        end = StrtoSec(end)
        
        n_time[start] += 1
        n_time[end] -= 1
        
    for i in range(1,play_time+1):
        n_time[i] += n_time[i-1]
        
    cnt = sum(n_time[:adv_time])
    cur = cnt
    answer = 0
    for i in range(play_time-adv_time):
        cur += n_time[i+adv_time] - n_time[i]
        if cnt < cur:
            cnt = cur
            answer = i+1
            
    return SectoStr(answer)
