def solution(arr1, arr2):
    answer = [[x2+y2 for x2, y2 in zip(x1,y1)] for x1, y1 in zip(arr1,arr2)]
    return answer
