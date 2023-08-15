class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def comb(amt,i):
            if i==len(coins):
                return -1
            if amt==0:
                return 1
            if coins[i]>amt:
                return comb(amt,i+1)
            total = 0
            a = comb(amt,i+1)
            b = comb(amt-coins[i],i)
            if a>0:
                total+=a
            if b>0:
                total+=b
            return total
        return comb(amount,0)
        