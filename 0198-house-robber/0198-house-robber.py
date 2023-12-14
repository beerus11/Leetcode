class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def ma(i):
            if i>=len(nums):
                return 0
            return max(nums[i]+ma(i+2),ma(i+1))
        return ma(0)
            
        