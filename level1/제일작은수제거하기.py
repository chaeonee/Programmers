def solution(arr):
    arr.pop(arr.index(min(arr)))
    if not arr:
        arr.append(-1)
    return arr
