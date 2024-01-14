class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count = 0
        end_time = -1
        for a,b in points:
            if count==0 or a>end_time:
                count+=1
                end_time = b
        return count
            
        