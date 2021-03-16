def solution(routes):
    routes = sorted(routes,key=lambda x:x[1])
    
    answer = 0
    cam = -30001
    for s, e in routes:
        if s > cam:
            answer += 1
            cam = e
            
    return answer
