def solution(numbers, target):
    answer = 0
    
    stack = []
    stack.append([0,numbers[0]])
    stack.append([0,-1*numbers[0]])
    
    while stack:
        node = stack.pop(len(stack)-1)
        
        if node[0] == len(numbers)-1:
            if node[1] == target:
                answer += 1
            continue
            
        stack.append([node[0]+1,node[1]+numbers[node[0]+1]])
        stack.append([node[0]+1,node[1]-numbers[node[0]+1]])
    
    return answer
