class WordDictionary:

    def __init__(self):
        self.d = {}
        

    def addWord(self, word: str) -> None:
        node = self.d
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]
        node['$'] = True
            
        

    def search(self, word: str) -> bool:
        def s(word,node):
            for i,ch in enumerate(word):
                if ch not in node:
                    if ch == ".":
                        for c in node:
                            if c != '$' and s(word[i+1:],node[c]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '$' in node
        return s(word,self.d)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)