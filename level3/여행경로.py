def dfs(n, city_list, visit, path, flag):
    if len(path) == n:
        return True, path
    
    city = path[-1]
    if city in city_list.keys():
        for i, c in enumerate(city_list[city]):
            if visit[city][i]:
                continue
            path.append(c)
            visit[city][i] = True
            flag, path = dfs(n,city_list,visit,path,flag)
            if flag:
                break
            path.pop()
            visit[city][i] = False
        
    return flag, path

def solution(tickets):
    city_list, visit = {}, {}
    for s, e in tickets:
        if s not in city_list.keys():
            city_list[s] = [e]
            visit[s] = [False]
        else:
            city_list[s].append(e)
            visit[s].append(False)
    
    for i in city_list.keys():
        city_list[i].sort()
    
    _, answer = dfs(len(tickets)+1,city_list,visit,["ICN"],False)
        
    return answer
