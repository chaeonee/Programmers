from collections import deque

def solution(record):
    user = {}
    q = deque()
    for r in record:
        r = list(r.split())
        if r[0] != "Leave":
            user[r[1]] = r[2]
        q.append([r[0],r[1]])
    
    answer = []
    while q:
        state, uid = q.popleft()
        if state == "Enter":
            answer.append(user[uid]+"님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(user[uid]+"님이 나갔습니다.")
    
    return answer
