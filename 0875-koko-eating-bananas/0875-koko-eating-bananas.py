class Solution:
    def minEatingSpeed(self, piles: List[int], hr: int) -> int:
        def get_hour(m):
            t = 0
            for i in piles:
                t+=math.ceil(i/m)
            return t
        l,h=1,max(piles)
        while l<h:
            m = l+(h-l)//2
            if get_hour(m)<=hr:
                h=m
            else:
                l=m+1
        return h
                