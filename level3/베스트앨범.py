def solution(genres, plays):
    songs = {}
    plays_sum = {}
    for i in range(len(genres)):
        if genres[i] not in songs.keys():
            songs[genres[i]] = [[i,plays[i]]]
            plays_sum[genres[i]] = plays[i]
        else:
            songs[genres[i]].append([i,plays[i]])
            plays_sum[genres[i]] += plays[i]
            
    answer = []
    plays_sum = sorted(plays_sum.items(),key=lambda x: -x[1])
    for k, _ in plays_sum:
        n = min(len(songs[k]),2)
        tmp = list(songs[k])
        tmp = sorted(tmp, key = lambda x : (-x[1], x[0]))
        for i in range(n):
            answer.append(tmp[i][0])
    
    return answer
