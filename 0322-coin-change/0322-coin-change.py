class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def cc(i,t):
            if t==0:
                return 0
            if i<0 or t<0:
                return float('inf')
            if coins[i]>t:
                return cc(i-1,t)
            a = 1+ cc(i,t-coins[i])
            b = cc(i-1,t)
            return min(a,b)
        a = cc(len(coins)-1,amount)
        return -1 if a==float('inf') else a
            
            
        