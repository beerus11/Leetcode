import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(a,b):
            x = (a)**2 + (b)**2
            return math.sqrt(x)
        return sorted(points,key = lambda x: dist(x[0],x[1]))[:k]
        