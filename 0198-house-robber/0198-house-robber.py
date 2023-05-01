class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def mxa(i):
            if i>=len(nums):
                return 0
            a = nums[i]+mxa(i+2)
            b = mxa(i+1)
            return max(a,b)
        return mxa(0)
            
        