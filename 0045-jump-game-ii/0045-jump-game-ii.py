class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def solve(i):
            if i>=len(nums)-1:
                return 0
            mn = float('inf')
            for j in range(1,nums[i]+1):
                mn = min(mn,solve(i+j))
            return 1+mn
        return solve(0)
        