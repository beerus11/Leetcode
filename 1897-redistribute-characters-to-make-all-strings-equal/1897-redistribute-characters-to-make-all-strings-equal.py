class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        m = Counter("".join(words))
        for k,v in m.items():
            if v%len(words):
                return False
        return True
        