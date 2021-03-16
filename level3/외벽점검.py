from itertools import permutations

def solution(n, weak, dist):
    n_weak = len(weak)
    weak += [n+i for i in weak]
    
    permute = list(permutations(dist,len(dist)))
    
    answer = float('inf')
    for s in range(n_weak):
        for per in permute:
            tmp, n_fix, start = 0, 0, weak[s]
            for p in per:
                if n_fix == n_weak:
                    break
                
                tmp += 1
                while n_fix < n_weak:
                    if weak[s+n_fix] > start+p:
                        start = weak[s+n_fix]
                        break
                    n_fix += 1
            
            if n_fix < n_weak:
                tmp = float('inf')
                
            answer = min(answer,tmp)
    
    answer = -1 if answer == float('inf') else answer
    
    return answer
