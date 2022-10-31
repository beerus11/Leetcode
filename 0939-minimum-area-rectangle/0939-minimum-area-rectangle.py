class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        S = set(map(tuple,points))
        ans = float('inf')
        for j,p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if (p1[0]!=p2[0] and p1[1]!=p2[1] and (p1[0],p2[1]) in S and (p2[0],p1[1]) in S):
                    ans = min(ans,abs(p1[0]-p2[0])*abs(p1[1]-p2[1]))
        return ans if ans!=float('inf') else 0
        