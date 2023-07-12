class Trie:

    def __init__(self):
        self.d = {}
        

    def insert(self, word: str) -> None:
        trie = self.d
        for w in word:
            if w not in trie:
                trie[w]={}
            trie = trie[w]
        trie["$"]=True
        

    def search(self, word: str) -> bool:
        trie = self.d
        for w in word:
            if w not in trie:
                return False
            trie = trie[w]
        return '$' in trie
            
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.d
        for w in prefix:
            if w not in trie:
                return False
            trie = trie[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)