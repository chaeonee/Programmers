import heapq

def solution(operations):
    q = []
    reverse = False
    for oper in operations:
        oper = oper.split()
        if oper[0] == 'I':
            q = [-i for i in q] if reverse else q
            reverse = False
            q.append(int(oper[1]))
        elif oper[0] == 'D' and q:            
            if oper[1] == '1':
                q = q if reverse else [-i for i in q]
                reverse = True
                heapq.heapify(q)
                n = heapq.heappop(q)
            elif oper[1] == '-1':
                q = [-i for i in q] if reverse else q
                reverse = False
                heapq.heapify(q)
                n = heapq.heappop(q)
    
    if not q:
        return [0,0]
    
    answer = []
    q = q if reverse else [-i for i in q]
    heapq.heapify(q)
    answer.append(-q[0])
    q = [-i for i in q]
    heapq.heapify(q)
    answer.append(q[0])
    
    return answer
