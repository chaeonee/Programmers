def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    l = len(truck_weights)
    
    w = 0
    idx = 0
    sec = 0
    while q:
        sec += 1
        w -= q.pop(0)
        
        if idx >= l:
            continue
            
        if w+truck_weights[idx] <= weight:
            w += truck_weights[idx]
            q.append(truck_weights[idx])
            idx += 1
        else:
            q.append(0)
    
    return sec
