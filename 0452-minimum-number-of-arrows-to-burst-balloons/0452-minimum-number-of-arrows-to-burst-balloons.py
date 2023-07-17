class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x :x[1])
        l = 1
        fe = points[0][1]
        for a,b in points:
            if fe< a:
                l+=1
                fe = b
        return l
            
        