from collections import deque

class Node:
    def __init__(self, keyword = None):
        self.keyword = keyword
        self.n_data = {}
        self.child = {}
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def addData(self,word):  
        cur_node = self.root
        
        w_len = len(word)
        for w in word:
            if w_len in cur_node.n_data.keys():
                cur_node.n_data[w_len] += 1
            else:
                cur_node.n_data[w_len] = 1
                
            if w in cur_node.child.keys():
                cur_node = cur_node.child[w]
            else:
                cur_node.child[w] = Node(w)
                cur_node = cur_node.child[w]
            
            w_len -= 1
    
    def search(self, query, n_blank):
        num = 0
        
        i = 0
        q = deque()
        q.append(self.root)
        while q:
            q_len = len(q)
            for _ in range(q_len):
                cur = q.popleft()
                
                if i == len(query):
                    if n_blank in cur.n_data.keys():
                        num += cur.n_data[n_blank]
                    continue
                    
                if query[i] in cur.child.keys():
                    q.append(cur.child[query[i]])
            i += 1
        
        return num

def solution(words, queries):  
    pre_trie = Trie()
    post_trie = Trie()
    for w in words:
        pre_trie.addData(w)
        post_trie.addData(w[::-1])
    
    answer = []
    for query in queries:
        n_blank = 0
        if query[0] == '?':
            for q in query:
                if q != '?':
                    break
                n_blank += 1
            query = query[n_blank:][::-1]
            
            answer.append(post_trie.search(query,n_blank))
        else:
            for q in query[::-1]:
                if q != '?':
                    break
                n_blank += 1
            query = query[:len(query)-n_blank]
            answer.append(pre_trie.search(query,n_blank))
            
    return answer
