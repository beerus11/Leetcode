class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def ma(i,first=False):
            if i>=len(nums):
                return 0
            if i==len(nums)-1 and first:
                    return 0 
            a = ma(i+1,first)
            b = nums[i]+ma(i+2,i==0 or first)    
            return max(a,b)
        return ma(0)
        