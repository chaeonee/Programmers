import sys
sys.setrecursionlimit(300000)

def calWeight(a, edges, visit, p_node, node, cnt):
    for e in edges[node]:
        if visit[e]:
            continue
        visit[e] = True
        
        cnt = calWeight(a,edges,visit,node,e,cnt)
    
    cnt += abs(a[node])
    a[p_node] += a[node]
    a[node] = 0
    
    return cnt

def solution(a, edges):
    if sum(a):
        return -1
    
    edge = {i:[] for i in range(len(a))}
    for u, v in edges:
        edge[u].append(v)
        edge[v].append(u)
    
    visit = [False]*len(a)
    visit[0] = True
    answer = calWeight(a,edge,visit,0,0,0)
    
    if a[0]:
        answer = -1
    
    return answer
