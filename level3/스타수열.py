from collections import Counter

def getMax(a):
    a = Counter(a)
    return a

def solution(a):
    if len(a) < 2:
        return 0
    
    answer = 0
    num_list = getMax(a)
    for num, n_cnt in num_list.items():
        if n_cnt < answer:
            continue
            
        idx, tmp = 0, 0
        while idx < len(a)-1:
            if a[idx] == a[idx+1] or (a[idx] != a[idx+1] and a[idx] != num and a[idx+1] != num):
                idx += 1
                continue
            idx += 2
            tmp += 1
        answer = max(answer, tmp)
        
    return answer*2
