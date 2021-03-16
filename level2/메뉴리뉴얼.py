from itertools import combinations

def solution(orders, course):
    menu_list = {}
    for order in orders:
        order = sorted(list(order))
        for n in range(2,len(order)+1):
            comb = list(combinations(order,n))
            for c in comb:
                menu = ''.join(list(c))
                if menu in menu_list.keys():
                    menu_list[menu] += 1
                else:
                    menu_list[menu] = 1
                    
    cmp_list = {}
    for key, value in menu_list.items():
        if len(key) in cmp_list:
            if cmp_list[len(key)][0] < value:
                cmp_list[len(key)] = [value, key]
            elif cmp_list[len(key)][0] == value:
                cmp_list[len(key)].append(key)
                
        elif len(key) not in cmp_list and value > 1:
            cmp_list[len(key)] = [value, key]
            
    answer = sorted([x for n in course if n in cmp_list.keys() for x in cmp_list[n][1:]])
    
    return answer
