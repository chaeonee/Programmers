def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n == 0:
            return False        
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                n = nums[i] + nums[j] + nums[k]
                answer = answer + 1 if isPrime(n) else answer  
    return answer
