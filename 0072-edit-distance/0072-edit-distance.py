class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def d(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return d(i+1,j+1)
            else:
                a=d(i+1,j)
                b=d(i,j+1)
                c=d(i+1,j+1)
                return min([a,b,c])+1
        return d(0,0)