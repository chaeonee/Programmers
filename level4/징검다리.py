def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    answer = distance
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        
        n_remove = 0
        pre_rock = 0
        for rock in rocks:
            if rock-pre_rock < mid:
                n_remove += 1
            else:
                pre_rock = rock
        
        if n_remove > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
    return answer
