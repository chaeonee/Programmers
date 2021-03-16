def solution(name):
    q = [0]
    for i, n in enumerate(name):
        if i == 0:
            continue
        if n != 'A':
            q.append(i)
            
    answer = 0
    while q:
        cur = q[0]
        answer += min(ord(name[cur])-ord('A'),ord('Z')-ord(name[cur])+1)
        
        q.pop(0)
        if len(q) <= 0:
            continue
        
        go, back = min(abs(cur-q[0]),abs(len(name)-q[0]+cur)), min(abs(cur-q[-1]),abs(len(name)-q[-1]+cur))
        if go <= back:
            answer += go
        else:
            answer += back
            tmp = q.pop()
            q = [tmp] + q
        
    return answer
