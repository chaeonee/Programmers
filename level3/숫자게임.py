def solution(A, B):
    B.sort()
    A.sort()
    
    answer, A_idx, B_idx = 0, 0, 0
    while B_idx < len(B):
        if A[A_idx] >= B[B_idx]:
            B_idx += 1
        else:
            answer += 1
            A_idx += 1
            B_idx += 1
            
    return answer
