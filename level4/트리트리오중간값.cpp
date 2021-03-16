from collections import deque

def getMaxdist(edges, s, n):
    q = deque()
    q.append([s,0])
    
    visit = [False]*n
    visit[s] = True
    
    far_node = []
    max_dist = 0
    while q:
        node, d = q.popleft()
        
        if max_dist < d:
            far_node = [node]
            max_dist = d
        elif max_dist == d:
            far_node.append(node)
        
        for j in edges[node]:
            if not visit[j]:
                visit[j] = True
                q.append([j,d+1])

    return max_dist, far_node

def solution(n, edge_list):
    edges = {}
    for s, e in edge_list:
        if s-1 not in edges:
            edges[s-1] = []
        if e-1 not in edges:
            edges[e-1] = []
        edges[s-1].append(e-1)
        edges[e-1].append(s-1)
    
    answer, node = getMaxdist(edges,0,n)
    
    answer, node = getMaxdist(edges,node[0],n)
    if len(node) != 1:
        return answer
    
    answer, node = getMaxdist(edges,node[0],n)
    if len(node) == 1:
        return answer - 1
            
    return answer
