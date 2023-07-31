class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def reach(i):
            if i>len(nums)-1:
                return float('inf')
            if i== len(nums)-1:
                return 0
            mn = float('inf')
            for j in range(1,nums[i]+1):
                mn = min(mn,1+reach(i+j))
            return mn
        return reach(0)
                
        