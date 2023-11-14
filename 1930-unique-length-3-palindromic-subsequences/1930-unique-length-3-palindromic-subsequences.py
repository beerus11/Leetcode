class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for i in set(s):
            l,r = s.index(i),s.rindex(i)
            bw = set()
            for j in range(l+1,r):
                bw.add(s[j])
            ans+=len(bw)
        return ans
            
                
            
            
                
                