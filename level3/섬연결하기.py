import heapq

def Union(parent, node1, node2):
    p1 = Find(parent, node1)
    p2 = Find(parent, node2)
    parent[p2] = p1        
    return parent

def Find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node

def solution(n, costs):
    q = []
    for n1, n2, c in costs:
        heapq.heappush(q, (c,n1,n2))
    
    answer = 0
    parent = [i for i in range(n)]
    while q:
        c, n1, n2 = heapq.heappop(q)
        if Find(parent,n1) == Find(parent,n2):
            continue
            
        parent = Union(parent,n1,n2)
        answer += c
        
    return answer
