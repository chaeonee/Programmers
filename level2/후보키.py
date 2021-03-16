from itertools import combinations

def solution(relations):
    n_att = len(relations[0])
    relation = {}
    for i, r in enumerate(relations[0]):
        relation[i] = [r]
    for rel in relations[1:]:
        for i, r in enumerate(rel):
            relation[i].append(r)
    
    answer = 0
    primary_key = {}
    for i in range(1,n_att+1):
        if i > len(relation):
            break
        candidate = list(combinations([i for i in relation.keys()],i))
        
        for cand in candidate:
            cand = list(cand)
            
            sub_cand = []
            for j in range(i):
                sub_cand += list(combinations(cand,j))
            
            flag = True
            for s in sub_cand:
                s = list(s)
                if ''.join(list(map(str,s))) in primary_key.keys():
                    flag = False
                    break
            if not flag:
                continue
            
            student = []
            for c in cand:
                student.append(relation[c])
            student = list(zip(*student))
            
            if len(list(set(student))) == len(student):
                answer += 1
                primary_key[''.join(list(map(str,cand)))] = True
            
        
    return answer
