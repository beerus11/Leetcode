class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        ltr,rtl = [],[]
        for i in range(len(nums)):
            if i == 0 :
                ltr.append(nums[i])
            else:
                ltr.append(nums[i]+ltr[-1])
                
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                rtl.append(nums[i])
            else:
                rtl.append(nums[i]+rtl[-1])
        rtl = rtl[::-1]
        
        for i in range(len(nums)):
            if i==0 and rtl[i+1]==0:
                return i
            if i==len(nums)-1 and ltr[i-1]==0:
                return i
            if i>0 and i<len(nums)-1 and ltr[i-1]==rtl[i+1]:
                return i
        return -1
                
                
            