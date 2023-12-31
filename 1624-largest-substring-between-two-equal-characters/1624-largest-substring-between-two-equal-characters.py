class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ls = -1
        hm = {}
        for k,ch in enumerate(s):
            if ch not in hm:
                hm[ch]=k
            elif k-hm[ch]>0:
                ls = max(ls,k-hm[ch]-1)
        return ls
        