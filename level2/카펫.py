def solution(brown, yellow):
    answer = []  
    area = brown+yellow
    for y in range(1,area//2):
        if area % y:
            continue
        
        x = area//y
        if 2*x+2*(y-2) == brown:
            answer = [x,y]
            break
        
    return answer
