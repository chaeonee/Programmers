def solution(n, t, m, timetable):
    timetable = [int(time.split(':')[0]+time.split(':')[1]) for time in timetable]
    last = int(str(9+((t*(n-1))//60))+str((t*(n-1))%60).zfill(2))
    timetable = sorted(timetable)
    timetable = [time for time in timetable if time <= last]
    
    idx = 0
    for i in range(n-1):
        time = int(str(9+((t*i)//60))+str((t*i)%60).zfill(2))
        for _ in range(m):
            if idx >= len(timetable):
                break

            if timetable[idx] <= time:
                idx += 1
            else:
                break
        if idx >= len(timetable):
            break
            
    if len(timetable)-idx < m:
        answer = str(last//100).zfill(2)+":"+str(last%100).zfill(2)
    else:
        time, minute = timetable[idx+m-1]//100, timetable[idx+m-1]%100
        if minute == 0:
            time -= 1
            minute = 59
        else:
            minute -= 1
        answer = str(time).zfill(2)+":"+str(minute).zfill(2)
               
    return answer
