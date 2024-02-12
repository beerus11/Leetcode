class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @lru_cache(None)
        def min_coin(i,free):
            if i>=len(prices):
                return 0
            a = prices[i]+min_coin(i+1,i+1)
            if free>0:
                a = min(a,min_coin(i+1,free-1))
            return a
        return min_coin(0,0)
        
        