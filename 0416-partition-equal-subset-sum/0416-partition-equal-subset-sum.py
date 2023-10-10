class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        t = s/2
        @lru_cache(None)
        def ss(i,t):
            if i== len(nums):
                return False
            if t==0:
                return True
            return ss(i+1,t) or ss(i+1,t-nums[i])
        return ss(0,t)