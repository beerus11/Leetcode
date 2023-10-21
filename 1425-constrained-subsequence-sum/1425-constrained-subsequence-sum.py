class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = []
        dp = [0]*len(nums)
        
        for i in range(len(nums)):
            if q and i-q[0]>k:
                q.pop(0)
            dp[i]= (dp[q[0]] if q else 0)+nums[i]
            
            while q and dp[q[-1]]<dp[i]:
                q.pop()
                
            if dp[i]>0:
                q.append(i)
        return max(dp)
                
        