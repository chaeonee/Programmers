def solution(s):
    s = s.replace('{','')
    s = s.split('}')
    s = [x for x in s if x]
    s = [x.split(',') for x in s]
    for i in range(len(s)):
        s[i] = list(map(int,[x for x in s[i] if x]))
        
    s = sorted(s, key=lambda x: len(x))
        
    answer = s[0]
    for i in range(1,len(s)):
        t = [x for x in s[i] if x not in s[i-1]]
        answer.append(t[0])
    
    return answer
