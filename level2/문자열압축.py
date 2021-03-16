def solution(s):
    answer = 1001
    
    iter_len = 1
    s_len = len(s)
    while iter_len <= int(s_len/2) + 1:
        compact_s = ''
        pre_s = s[:iter_len]
        
        num = 1
        i = iter_len
        while i < s_len:
            cur_s = s[i:i+iter_len]
            i += iter_len
            
            if cur_s != pre_s:
                if num == 1:
                    compact_s += pre_s
                else:
                    compact_s += str(num)+pre_s
                    
                num = 1
                pre_s = cur_s
                continue
                
            num += 1
            
        if num == 1:
            compact_s += pre_s
        else:
            compact_s += str(num)+pre_s
            
        iter_len += 1
        
        answer = min(answer,len(compact_s))
    
    return answer
