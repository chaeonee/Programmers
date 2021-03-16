def solution(phone_book):
    answer = True
    
    phone_book.sort(key=len)
    
    dic = {phone_book[0]:0}
    for i in phone_book:
        check = 0
        for key in dic:
            if key == i[:len(key)]:
                dic[key] += 1
                check = 1
                if dic[key] > 1:
                    answer = False
                    return answer
        if check == 0:
            dic[i] = 1                
    
    return answer
