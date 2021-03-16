def solution(array, commands):
    answer = []
    
    for i in commands:
        tmp = array[i[0]-1:i[1]]
        tmp.sort()
        answer.append(tmp[i[2]-1])
    return answer

if __name__ == '__main__':
    array = input()
    commands = input()
    
    print(solution(array,commands))
