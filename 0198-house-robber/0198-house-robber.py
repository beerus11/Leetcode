class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def mxa(i,x):
            if i>=len(nums):
                return 0
            if i-1==x:
                return mxa(i+1,x)
            else:
                a = nums[i]+mxa(i+2,i)
                b = mxa(i+1,x)
                return max(a,b)
        return mxa(0,-2)
            
        