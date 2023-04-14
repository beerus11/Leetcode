import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return math.sqrt(x**2 +y**2)

        arr = [(dist(p[0],p[1]),p)for p in points]
        arr = sorted(arr,key= lambda a:a[0])[:k]
        return [a[1] for a in arr]