class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def count(l):
            if l>high:
                return 0
            if l==high:
                return 1
            total = 0
            if l>=low:
                total+=1
            a = count(l+zero)%mod
            b = count(l+one)%mod
            return (a+b+total)%mod
        return count(0)
                
            
        