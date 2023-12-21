class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        print(points)
        mx = 0
        lp = points[0][0]
        for a,b in points[1::]:
            mx = max(mx,a-lp)
            lp = a
        return mx
        