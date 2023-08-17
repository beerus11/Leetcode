class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def comb(t):
            if t==0:
                return 1
            total = 0
            for num in nums:
                if t-num>=0:
                    total += comb(t-num)
            return total
        return comb(target)
            
        