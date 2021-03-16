def solution(dirs):
    c_dir = {}
    c_dir['U'] = [0,1]
    c_dir['D'] = [0,-1]
    c_dir['R'] = [1,0]
    c_dir['L'] = [-1,0]
    
    answer = 0
    character = [5,5]
    visit = {}
    visit['U'] = [[False]*11 for _ in range(11)]
    visit['D'] = [[False]*11 for _ in range(11)]
    visit['R'] = [[False]*11 for _ in range(11)]
    visit['L'] = [[False]*11 for _ in range(11)]
    for d in dirs:
        ori_dir = 'U' if d == 'D' else 'D' if d == 'U' else 'R' if d == 'L' else 'L'
        visit[ori_dir][character[0]][character[1]] = True
        dx, dy = [character[i]+c_dir[d][i] for i in range(2)]
        if 0 <= dx <= 10 and 0 <= dy <= 10:
            character = [dx,dy]
            if not visit[d][dx][dy]:
                visit[d][dx][dy] = True
                answer += 1
    return answer
