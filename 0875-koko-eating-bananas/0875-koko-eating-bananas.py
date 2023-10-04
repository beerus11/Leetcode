import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def tt(arr,x):
            t = 0
            for i in arr:
                t+= math.ceil(i/x)
            return t
        
        l,r = 1,max(piles)
        while l<r:
            mid = l+(r-l)//2
            if tt(piles,mid)  <= h:
                r = mid
            else:
                l = mid+1
        return r
            