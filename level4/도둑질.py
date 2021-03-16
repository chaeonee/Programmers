def solution(money):
    thief = [[0]*len(money) for _ in range(2)]
    thief[0][0] = money[0]
    thief[0][1], thief[1][1] = money[1], money[1]
       
    for i in range(2,len(money)):
        if i == len(money)-1:
            thief[0][i] = thief[0][i-1]
        else:
            thief[0][i] = max(money[i]+thief[0][i-2], thief[0][i-1], thief[0][i-1]-money[i-1]+money[i])
        thief[1][i] = max(money[i]+thief[1][i-2], thief[1][i-1], thief[1][i-1]-money[i-1]+money[i])
    print()            
    return max(thief[0][len(money)-1],thief[1][len(money)-1])
