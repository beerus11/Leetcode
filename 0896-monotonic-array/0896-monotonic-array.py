class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        
        pv = 0
        for i in range(1,len(nums)):
            x = nums[i]-nums[i-1]
            print(x)
            if pv ==0 or x==0 or pv*x>0:
                if x!=0:
                    pv = x
            else:
                print(pv,x)
                return False
        return True
            
            
        