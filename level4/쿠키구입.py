def solution(cookie):
    n = len(cookie)
    
    answer = 0
    for m in range(n):
        left = m
        right = m
        
        l_cookie = cookie[left]
        r_cookie = 0
        while left >= 0 and right < n:
            if l_cookie < r_cookie:
                left -= 1
                if left >= 0:
                    l_cookie += cookie[left]
            elif l_cookie > r_cookie:
                right += 1
                if right < n:
                    r_cookie += cookie[right]
            else:
                answer = max(answer, l_cookie)
                left -= 1
                right += 1
                if left >= 0:
                    l_cookie += cookie[left]
                if right < n:
                    r_cookie += cookie[right]
            
    return answer
