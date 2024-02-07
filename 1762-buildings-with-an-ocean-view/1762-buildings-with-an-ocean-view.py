class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ngl = []
        for i in range(len(heights)-1,-1,-1):
            if not ngl:
                ngl.append(heights[i])
            else:
                ngl.append(max(ngl[-1],heights[i]))
        ngl=ngl[::-1]
        ans = []
        for i in range(len(heights)-1):
            if heights[i]>ngl[i+1]:
                ans.append(i)
        ans.append(len(heights)-1)
        return ans
            
        