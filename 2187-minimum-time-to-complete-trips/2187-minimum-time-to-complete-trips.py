class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 1 , max(time)*totalTrips
        
        def gt(given_time):
            trips = 0
            for t in time:
                trips+= given_time//t
            return trips>=totalTrips
        
        while start < end:
            mid = (start+end)//2
            if gt(mid):
                end = mid
            else:
                start = mid+1
        return start
                
            
        