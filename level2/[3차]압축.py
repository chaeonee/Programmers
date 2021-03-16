def solution(msg):
    l_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    l_dic = {}
    for i in range(1,27):
        l_dic[l_list[i-1]] = i
    
    idx = 26
    answer = []
    while msg:
        tmp_msg = ''
        flag = True
        for i in range(len(msg)):
            tmp_msg += msg[i]
            if tmp_msg not in l_dic.keys():
                tmp_msg = tmp_msg[:-1]
                msg = msg[i:]
                flag = False
                break
        if flag:
            msg = msg = msg[i+1:]
        answer.append(l_dic[tmp_msg])
        
        idx += 1
        if msg:
            tmp_msg += msg[0]
            l_dic[tmp_msg] = idx
    
    return answer
