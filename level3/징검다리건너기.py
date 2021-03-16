def solution(stones, k):
    min_niniz, max_niniz = 1, max(stones)
    
    while min_niniz <= max_niniz:
        mid = (min_niniz+max_niniz)//2
        
        flag = True
        check = 0
        for i in stones:
            if i-mid <= 0:
                check += 1
            else:
                check = 0
            if check >= k:
                flag = False
                break
        if flag:
            min_niniz = mid + 1
        else:
            max_niniz = mid - 1
        
    return min_niniz
