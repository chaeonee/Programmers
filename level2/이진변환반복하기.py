from collections import Counter

def solution(s):
    num, cnt = 0, 0
    while s != '1':
        num += 1
        cnt += Counter(s)['0']
        s = s.replace('0','')
        s = format(len(s),'b')        
    return [num,cnt]
