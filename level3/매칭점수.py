import re

def solution(word, pages):
    word = word.lower()
    
    page_info = {}
    for idx, page in enumerate(pages):
        text = re.compile("<meta property=\"og:url\" content=\"https://\S*\"", re.I|re.S)
        text = text.findall(page)[0]
        pattern = re.compile('https://\S*\w', re.I)
        cur = pattern.findall(text)[0]
        if cur not in page_info.keys():
            page_info[cur] = [idx,0,[],0]
            
        text = re.compile("<a href=\"\S*?\"", re.I|re.S)
        text = text.findall(page)
        for i, t in enumerate(text):
            pattern = re.compile('https://\S*\w', re.I)
            text[i] = pattern.findall(t)[0]
            page_info[cur][2].append(text[i])
            
        pattern = re.compile('[a-zA-Z]+')
        text = pattern.findall(page)
        for t in text:
            if word == t.lower():
                page_info[cur][1] += 1
                
    for k in page_info.keys():
        if not page_info[k][2]:
            continue
        link_score = page_info[k][1]/len(list(set(page_info[k][2])))
        print(link_score)
        for link in list(set(page_info[k][2])):
            if link in page_info.keys():
                page_info[link][3] += link_score
    
    answer = [0,-1]
    for k in page_info.keys():
        if page_info[k][1] + page_info[k][3] > answer[1]:
            answer = [page_info[k][0],page_info[k][1]+page_info[k][3]]
        
    return answer[0]
