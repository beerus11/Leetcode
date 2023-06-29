class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans,num = 0,0
        for c in s:
            if c=="0":
                ans = min(ans+1,num)
            else:
                num+=1
        return ans
        