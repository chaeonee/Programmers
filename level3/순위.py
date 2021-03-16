def solution(n, results):
    rank = [[set(),set()] for _ in range(n)]
    for w, l in results:
        rank[w-1][1].add(l-1)
        rank[l-1][0].add(w-1)
        
    for i in range(n):
        for w in rank[i][0]:
            rank[w][1] = rank[w][1].union(rank[i][1])
        for l in rank[i][1]:
            rank[l][0] = rank[l][0].union(rank[i][0])
    
    answer = 0
    for i in range(n):
        if len(rank[i][0]) + len(rank[i][1]) == n-1:
            answer += 1
    
    return answer
