def solution(enroll, referral, seller, amount):
    pyramid = {i:[0,'center'] for i in enroll}
    
    for i, e in enumerate(enroll):
        if referral[i] == '-':
            continue
        pyramid[e][1] = referral[i]
        
    for s, b in zip(seller,amount):
        b *= 100
        
        while b > 0 and s != 'center':
            pyramid[s][0] += b - int(b*0.1)
            
            b //= 10
            s = pyramid[s][1]
        
    return [pyramid[e][0] for e in enroll]
