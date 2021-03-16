def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s),0,-1):
            if not i:
                if s[i] == s[j-1] and s[i:j] == s[j-1::-1]:
                    answer = max(answer,j-i)
                    break
                continue
            if s[i] == s[j-1] and s[i:j] == s[j-1:i-1:-1]:
                answer = max(answer,j-i)
                break         
    return answer
