import sys
sys.setrecursionlimit(10**6)

def getPreorder(root,tree):
    visit = [False]*(len(tree)+1)
    
    order = [root]
    stack = [root]
    visit[root] = True
    
    while stack:
        child = tree[stack[-1]][0]
        if child != -1 and not visit[child]:
            visit[child] = True
            order.append(child)
            stack.append(child)
        else:
            child = tree[stack.pop()][1]
            if child != -1 and not visit[child]:
                visit[child] = True
                order.append(child)
                stack.append(child)
        
    return order

def getPostorder(root,tree):
    visit = [False]*(len(tree)+1)
    
    order = []
    stack = [root]
    visit[root] = True
    
    while stack:
        child = tree[stack[-1]][0]
        if child != -1 and not visit[child]:
            visit[child] = True
            stack.append(child)
        else:
            child = tree[stack[-1]][1]
            if child != -1 and not visit[child]:
                visit[child] = True
                stack.append(child)
            else:
                order.append(stack.pop())
                
    return order

def getTree(levelinfo, cur_node, level, cur_level, tree, bound):
    if cur_level == level:
        tree[cur_node[0]] = [-1,-1] 
        return tree
    
    tree[cur_node[0]] = [-1,-1] 
    nextnodelist = levelinfo[cur_level+1]
    for node in nextnodelist:
        if bound[0] < node[1] < cur_node[1]:
            tree[cur_node[0]][0] = node[0]
            tree = getTree(levelinfo,node,level,cur_level+1,tree,[bound[0],cur_node[1]])
            break
            
    for node in nextnodelist:
        if cur_node[1] < node[1] < bound[1]:
            tree[cur_node[0]][1] = node[0]
            tree = getTree(levelinfo,node,level,cur_level+1,tree,[cur_node[1],bound[1]])
            break
    
    return tree

def solution(nodeinfo):
    nodeinfo = [[i+1]+n for i, n in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo,key=lambda x:(-x[2],x[1]))
    root = nodeinfo[0][0]
    
    level = -1
    levelinfo = {}
    while nodeinfo:
        level += 1
        levelinfo[level] = []
        node = nodeinfo[0][2]
        while nodeinfo and node == nodeinfo[0][2]:
            levelinfo[level].append(nodeinfo.pop(0))
    
    tree = getTree(levelinfo,levelinfo[0][0],level,0,{},[-1,100001])
    
    return [getPreorder(root,tree),getPostorder(root,tree)]
