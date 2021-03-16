import re

def solution(new_id):
    new_id = new_id.lower()
    
    new_id = list(new_id)
    for i, s in enumerate(new_id):
        if  not ('0' <= s <= '9') and not ('a' <= s <= 'z') and s != '-' and s != '_' and s != '.':
            new_id[i] = ' '
    new_id = ''.join(new_id)
    new_id = new_id.replace(' ','')
    
    new_id = re.sub('\.+','.',new_id)
    
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
