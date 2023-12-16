class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = ceil(stones_sum/2)
        
        @lru_cache(None)
        def dfs(i,total):
            if total>=target or i==len(stones):
                return abs(total-(stones_sum-total))
            a = dfs(i+1,total+stones[i])
            b = dfs(i+1,total)
            return min(a,b)
        return dfs(0,0)
                
        