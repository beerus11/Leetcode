class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x,z = 0,0
        for i in nums:
            if i==0:
                z+=1
            elif i<0:
                x+=1
        if z>0:
            return 0
        if x>0 and x%2!=0:
            return -1
        return 1
        