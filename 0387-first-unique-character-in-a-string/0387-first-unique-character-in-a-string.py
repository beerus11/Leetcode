class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = Counter(s)
        for k,v in enumerate(s):
            if hm[v]==1:
                return k
        return -1
        