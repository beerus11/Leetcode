class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def mo(i,j):
            if i==len(word1) and j==len(word2):
                return 0
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return mo(i+1,j+1)
            a = 1+mo(i,j+1)
            b = 1+mo(i+1,j)
            c = 1+mo(i+1,j+1)
            return min([a,b,c])
        return mo(0,0)
        
        