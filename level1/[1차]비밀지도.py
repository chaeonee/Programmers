def solution(n, arr1, arr2):
    answer = []
    for n1, n2 in zip(arr1, arr2):
        b = str(bin(n1|n2))
        b = b.replace('0b','')
        b = b.rjust(n,'0')
        b = b.replace('1','#')
        b = b.replace('0',' ')
        answer.append(b)
            
    return answer
