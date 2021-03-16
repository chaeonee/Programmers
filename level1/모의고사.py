def solution(answers):
    answer = []
    
    person = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    max_c = -1
    for i in range(3):
        count = 0
        for j in range(len(answers)):
            if answers[j] == person[i][j%len(person[i])]:
                count += 1
        if max_c < count:
            answer = []
            answer.append(i+1)
            max_c = count
        elif max_c == count:
            answer.append(i+1)
            
    return answer

if __name__ == '__main__':
    answers = input()
    
    print(solution(answers))
