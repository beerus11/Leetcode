class Node(object):
    def __init__(self):
        self.children = [None]*26
        self.isEndWord = False
class Trie:
    def __init__(self):
        self.node = Node()
        self.result = []
    def insert(self,word):
        node = self.node
        for w in word:
            ind = ord(w)-ord('a')
            if node.children[ind]==None:
                node.children[ind]=Node()
            node = node.children[ind]
        node.isEndWord=True
        
    def dfs(self,node,word):
        if len(self.result)==3:
            return
        if node.isEndWord:
            self.result.append(word)
  
        for k,v in enumerate(node.children):
            if v!=None:
                self.dfs(v,word+chr(ord('a')+k))    
    
    def search(self,prefix):
        #print(prefix)
        node = self.node
        self.result = []
        for c in prefix:
            ind = ord(c)-ord('a')
            if node.children[ind]!=None:
                node = node.children[ind]
            else:
                return self.result
        self.dfs(node,prefix)
        return self.result
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        ans = []
        prefix = ""
        for c in searchWord:
            prefix+=c
            ans.append(trie.search(prefix))
        return ans

                    