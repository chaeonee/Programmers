class Node:
    def __init__(self, letter = None):
        self.letter = letter
        self.n_word = 0
        self.word = []
        self.child = {}
    
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insertNode(self,word):
        node = self.root
        for w in word:
            node.n_word += 1
            
            if w not in node.child.keys():
                node.child[w] = Node(w)
            node = node.child[w]
        
        node.n_word += 1
        node.word.append(word)
        
    def searchNode(self,word):
        cnt = 0
        
        node = self.root
        for w in word:
            if w not in node.child.keys():
                return 0
            
            cnt += 1
            node = node.child[w]
            
            if node.n_word <= 1:
                break
            
        return cnt

def solution(words):
    trie = Trie()
    for word in words:
        trie.insertNode(word)
    
    answer = 0
    for word in words:
        answer += trie.searchNode(word)
        
    return answer
