class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s)
        for k,v in enumerate(s):
            if m[v]==1:
                return k
        return -1
                
        