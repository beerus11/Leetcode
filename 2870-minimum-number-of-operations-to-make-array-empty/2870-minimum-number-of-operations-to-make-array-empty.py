class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        @lru_cache
        def mo(i,s):
            if s==0:
                return 0
            if i==len(nums)-1:
                return float('inf')
            a,b = float('inf'),float('inf')
            if i+2<=len(nums)-1 and nums[i]==nums[i+1]==nums[i+2]:
                a = 1+mo(i+3,s-(3*nums[i]))
            if i+1<=len(nums)-1 and nums[i]==nums[i+1]:
                b = 1+mo(i+2,s-(2*nums[i]))
            return min(a,b)
        ans = mo(0,sum(nums))
        if ans == float('inf'):
            return -1
        return ans
        