def solution(gems):
    n_gems = len(set(gems))
    
    answer = []
    gem_list = {gems[0]:1}
    right, min_len = 1, float('inf')
    for left in range(len(gems)-n_gems+1):
        if left > 0 and gems[left-1] in gem_list.keys():
            gem_list[gems[left-1]] -= 1
            if gem_list[gems[left-1]] <= 0:
                gem_list.pop(gems[left-1])
        
        if n_gems == len(gem_list):
            answer = [left+1,right]
            min_len = right - left
            continue
            
        while right < len(gems):                
            gem_list[gems[right]] = 1 if gems[right] not in gem_list.keys() else gem_list[gems[right]] + 1
            
            right += 1
            if right -left >= min_len:
                break
                
            if n_gems == len(gem_list):
                answer = [left+1,right]
                min_len = right - left
                break
    
    return answer
