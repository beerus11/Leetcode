class Solution:
    def trap(self, height: List[int]) -> int:
        rge,lge = [],[]
        for i in range(len(height)-1,-1,-1):
            if len(rge)==0:
                rge.append(height[i])
            else:
                rge.append(max(height[i],rge[-1]))
            
        for i in range(len(height)):
            if len(lge)==0:
                lge.append(height[i])
            else:
                lge.append(max(height[i],lge[-1]))
            
        rge = rge[::-1]
        ans = 0
        for i in range(1,len(height)-1):
            mn = min(lge[i-1],rge[i+1])
            x =(mn-height[i])
            if x>0:
                ans+=x
        return ans
                
            
        