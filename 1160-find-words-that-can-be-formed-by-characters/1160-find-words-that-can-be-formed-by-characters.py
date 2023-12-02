class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hm = Counter(list(chars))
        def check(word):
            m = Counter(word)
            for k,v in m.items():
                if k not in hm or hm[k]<v:
                    return False
            return True
        ans = 0
        for w in words:
            if check(w):
                ans+=len(w)
        return ans
            
        