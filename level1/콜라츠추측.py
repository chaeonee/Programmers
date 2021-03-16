def solution(num):
    it = 0
    while it < 500 and num != 1:
        it += 1
        num = num//2 if not num%2 else num*3+1
    return it if num == 1 else -1
