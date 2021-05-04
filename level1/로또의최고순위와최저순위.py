def solution(lottos, win_nums):
    N = len(lottos)
    lottos = sorted(lottos)
    win_nums = {i:False for i in win_nums}
    
    z_cnt = 0
    while z_cnt < N and not lottos[z_cnt]:
        z_cnt += 1
    
    cnt = 0
    for l in lottos[z_cnt:]:
        if l in win_nums.keys():
            cnt += 1
    
    return [min(6,7-cnt-z_cnt),min(6,7-cnt)]
