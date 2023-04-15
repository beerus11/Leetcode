class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def maxL(i,lc,lcc,k):
            if k<0:
                return float('inf')
            if i == n:
                return 0 
            delete_char = maxL(i+1,lc,lcc,k-1)
            
            if s[i]==lc:
                keep_char = maxL(i+1,lc,lcc+1,k)
                if lcc in [1, 9, 99]:
                    keep_char+=1
            else:
                keep_char = maxL(i+1,s[i],1,k)+1
            
            return min(delete_char,keep_char)
        return maxL(0,"",0,k)
        
        