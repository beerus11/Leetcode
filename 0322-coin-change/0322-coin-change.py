class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @lru_cache(None)
        def cc(amt,i):
            if amt==0:
                return 0
            if amt<0 or i>=len(coins) or coins[i]>amount:
                return float('inf')  
            return min(1+cc(amt-coins[i],i),cc(amt,i+1))
        x = cc(amount,0)
        if x==float('inf'):
            return -1
        return x
            
            
        