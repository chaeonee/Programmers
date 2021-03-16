from collections import Counter
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    str1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if 'A' <= str1[i] <= 'Z' and 'A' <= str1[i+1] <= 'Z'])
    str2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if 'A' <= str2[i] <= 'Z' and 'A' <= str2[i+1] <= 'Z'])
    
    intersection = 0
    union = 0
    for k in str1.keys():
        if k in str1.keys():
            intersection += min(str1[k],str2[k])
            union += max(str1[k],str2[k])
        else:
            union += str1[k]
    for k in str2.keys():
        if k not in str1.keys():
            union += str2[k]
    answer = 1 if union == 0 else intersection/union
    
    return int(answer*65536)
