import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def reach(speed):
            time = 0
            for k,v in enumerate(dist):
                if k< len(dist)-1:
                    time += math.ceil(v/speed)
                else:
                    time += v/speed
            return time <= hour
        
        low,high = 1,10**7
        while low<high:
            s = low+(high-low)//2
            if reach(s):
                high=s
            else:
                low=s+1
        if reach(high):
            return high
        return -1
            
            
        