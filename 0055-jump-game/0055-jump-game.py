class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def reach(i):
            if i>=len(nums):
                return False
            if i==len(nums)-1:
                return True
            for j in range(nums[i],0,-1):
                if reach(i+j):
                    return True
            return False
        return reach(0)
                