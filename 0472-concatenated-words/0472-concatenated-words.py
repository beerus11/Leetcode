class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie, res = Trie(), []
        for word in sorted(words, key=len):
            print(word)
            if trie.find(word):
                res.append(word)
            else:
                trie.insert(word)
        return res
        
class Trie:
    def __init__(self):
        self.node = {}

    def insert(self, word: str) -> None:
        node = self.node
        for ch in word + '$':
            node = node.setdefault(ch, {})

    def find(self, word):
        node = self.node
        for i, w in enumerate(word):
            if '$' in node:
                if self.find(word[i:]):
                    return True
            if w in node:
                node = node[w]
            else:
                return False
        return '$' in node
        