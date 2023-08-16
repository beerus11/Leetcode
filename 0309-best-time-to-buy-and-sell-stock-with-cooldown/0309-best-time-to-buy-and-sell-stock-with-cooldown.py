class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            cooldown = dfs(i+1,buy)
            
            if buy:
                buy = dfs(i+1,not buy)-prices[i]
                return max(cooldown,buy)
            else:
                sell = dfs(i+2,not buy)+prices[i]
            return max(cooldown,sell)
        return dfs(0,True)