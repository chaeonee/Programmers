import collections

def solution(arr):
    answer = []
    q = [[0,0,len(arr)]]
    while q:
        x, y ,l = q.pop(0)
        
        flag = True
        num = arr[x][y]
        for i in range(x,x+l):
            for j in range(y,y+l):
                if arr[i][j] != num:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            answer.append(num)
        else:
            q.append([x,y,l//2])
            q.append([x+(l//2),y,l//2])
            q.append([x,y+(l//2),l//2])
            q.append([x+(l//2),y+(l//2),l//2])
    answer = collections.Counter(answer)
    
    return [answer[0],answer[1]]
