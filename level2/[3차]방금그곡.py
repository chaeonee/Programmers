def getTime(s,e):
    s = list(map(int,s.split(':')))
    e = list(map(int,e.split(':')))
    
    time = [0,0]
    time[0] = e[0]-s[0] if e[1] >= s[1] else e[0]-s[0]-1
    time[1] = e[1]-s[1] if e[1] >= s[1] else 60+e[1]-s[1]
    
    return 60*time[0]+time[1]

def solution(m, musicinfos):
    m = m.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
    musicinfos = [music.split(',') for music in musicinfos]
    
    max_score = -1
    answer = ''
    for s, e, song, score in musicinfos:
        time = getTime(s,e)
        score = score.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
        
        score = score*(time//len(score))+score[:time%len(score)]
        if m in score and max_score < time:
            answer = song
            max_score = time
        
    answer = '(None)' if answer == '' else answer
    
    return answer
