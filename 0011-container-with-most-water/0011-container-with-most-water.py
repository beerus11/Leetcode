class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0 ,len(height)-1
        area = 0
        while l<r:
            w = r-l
            area = max(area,w*min(height[l],height[r]))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return area
        