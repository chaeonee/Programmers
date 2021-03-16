def getDist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])
    
def solution(numbers, hand):
    phone = [[i,j] for i in range(3) for j in range(3)]
    phone = [[3,1]] + phone
    
    left = [3,0]
    right = [3,2]
    
    answer = ''
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = phone[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = phone[num]
        else:
            d1 = getDist(left,phone[num])
            d2 = getDist(right,phone[num])
            
            if d1 < d2:
                answer += 'L'
                left = phone[num]
            elif d1 > d2:
                answer += 'R'
                right = phone[num]
            else:
                if hand == "right":
                    answer += 'R'
                    right = phone[num]
                else:
                    answer += 'L'
                    left = phone[num]
    
    return answer
