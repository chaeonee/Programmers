import string

def solution(skill, skill_trees):
    pre_skill = [i for i in range(26)]
    for i in range(1,len(skill)):
        pre_skill[ord(skill[i])-65] = ord(skill[i-1])-65
    
    answer = 0
    for skills in skill_trees:
        answer += 1
        visit = [False]*26
        for s in skills:
            visit[ord(s)-65] = True
            
            pre = pre_skill[ord(s)-65]
            if not visit[pre]:
                answer -= 1
                break
            
    return answer
