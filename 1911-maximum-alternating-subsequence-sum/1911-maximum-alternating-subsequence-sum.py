class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @lru_cache(None)
        def mas(i,even):
            if i==len(nums):
                return 0
            if even:
                return max(nums[i]+mas(i+1,False),mas(i+1,True))
            return max(-nums[i]+mas(i+1,True),mas(i+1,False))
        return mas(0,True)
            