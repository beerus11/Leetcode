class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def mp(i,buy):
            if i==len(prices):
                return 0
            ans = mp(i+1,buy)
            if buy:
                ans = max(ans,mp(i+1,False)-prices[i])
            else:
                ans = max(ans,prices[i]+mp(i+1,True)-fee)
            return ans
        return mp(0,True)
                
            
            
        
        
        