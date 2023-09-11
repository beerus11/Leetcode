class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1000000007
        @lru_cache(None)
        def count(unpicked, undelivered):
            if not unpicked and not undelivered:
                return 1
            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                return 0

            ans = unpicked * count(unpicked - 1, undelivered)
            ans %= MOD

            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * count(unpicked, undelivered - 1)
            ans %= MOD

            return ans
        return count(n,n)
                    
                    
            
        