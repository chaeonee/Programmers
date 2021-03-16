from itertools import permutations
def solution(expression):
    num = ''
    num_list = []
    oper_list = []
    for x in expression:
        if x == '+' or x == '-' or x == '*':
            oper_list.append(x)
            num_list.append(int(num))
            num = ''
            continue
        num += x
    num_list.append(int(num))
    
    answer = 0
    oper_priority = list(permutations(['+','-','*'],3))
    for oper_pri in oper_priority:
        tmp_num = [x for x in num_list]
        tmp_oper = [x for x in oper_list]
        for oper in oper_pri:
            size = len(tmp_oper)
            n = tmp_num.pop(0)
            for _ in range(size):
                if not tmp_oper:
                    tmp_num.append(n)
                    break
                    
                o = tmp_oper.pop(0)
                
                if o != oper:
                    tmp_num.append(n)
                    tmp_oper.append(o)
                    n = tmp_num.pop(0)
                    continue
                
                if o == '+':
                    n += tmp_num.pop(0)
                elif o == '-':
                    n -= tmp_num.pop(0)
                elif o == '*':
                    n *= tmp_num.pop(0)
            tmp_num.append(n)
            
        answer = max(answer,abs(tmp_num[0]))
            
    return answer
