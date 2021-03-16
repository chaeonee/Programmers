def solution(files):
    for i,file in enumerate(files):
        tmp = ''
        tmp_list = []
        file = list(file)
        while file and not file[0].isdecimal():
            tmp += file.pop(0)
        tmp_list.append(tmp)
        
        tmp = ''
        while file and file[0].isdecimal():
            tmp += file.pop(0)
        tmp_list.append(tmp)
        
        tmp_list.append(''.join(file))
        
        files[i] = tmp_list
        
    return [''.join(f) for f in sorted(files,key=lambda x:(x[0].lower(),int(x[1])))]
