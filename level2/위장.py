def solution(clothes):
    answer = 0
    
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = []
            dic[i[1]].append(i[0])
    
    len_list = []
    for key in dic:
        len_list.append(len(dic[key]))
    
    for i in range(len(len_list)):
        tmp = len_list[i]
        for j in range(i+1,len(len_list)):
            tmp *= len_list[j]+1
        answer += tmp
    
    
    return answer

if __name__ == '__main__':
    clothes = input()
    
    print(solution(clothes))
