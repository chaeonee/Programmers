def solution(n, words):
    answer = [0,0]
    
    order = (len(words)-1)//n
    w_list = {}
    for i in range(order+1):
        for j in range(n):
            if n*i+j >= len(words):
                break
            if not i and not j:
                w_list[words[0]] = 0
                continue
                
            if words[n*i+j] in w_list.keys() or words[n*i+j][0] != words[n*i+j-1][-1]:
                answer = [j+1,i+1]
                break
            w_list[words[n*i+j]] = 0
        
        if answer != [0,0]:
            break
    return answer
