class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,h = 0, 10**15
        
        def isPossible(t):
            res = 0
            for a in time:
                res+= int(mid*1.0/a)
            return res>=totalTrips
        ans = None
        while l<=h:
            mid = (l+h)//2
            if isPossible(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans
            
        