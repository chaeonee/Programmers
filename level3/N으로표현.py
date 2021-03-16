def solution(N, number):
    if N == number:
        return 1
    
    n_list = {}
    for i in range(1,9):
        n_list[i] = [int(str(N)*i)]
    
    answer = -1
    for i in range(2,9):
        for j in range(1,(i//2)+1):
            for x in n_list[j]:
                for y in n_list[i-j]:
                    n_list[i].append(x+y)
                    n_list[i].append(x-y)
                    n_list[i].append(y-x)
                    n_list[i].append(x*y)
                    if x != 0:
                        n_list[i] = n_list[i]+[y//x] if y/x == y//x else n_list[i]
                    if y != 0:
                        n_list[i] = n_list[i]+[x//y] if x/y == x//y else n_list[i]
        n_list[i] = list(set(n_list[i]))
        if number in n_list[i]:
            answer = i
            break
    return answer
