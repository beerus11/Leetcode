class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr,rtl= [],[]
        p = 1
        for i in nums:
            p*=i
            ltr.append(p)
        p = 1
        for i in range(len(nums)-1,-1,-1):
            p*=nums[i]
            rtl.append(p)
        rtl = rtl[::-1]
        ans = []
        for i in range(len(nums)):
            if i ==0:
                ans.append(rtl[i+1])
            elif i == len(nums)-1:
                ans.append(ltr[i-1])
            else:
                ans.append(rtl[i+1]*ltr[i-1])
        return ans
                
            
        