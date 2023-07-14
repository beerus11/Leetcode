class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mxl=0
        ones = 0
        zeroes = 0
        sw = []
        for i in range(len(nums)):
            sw.append(nums[i])
            if nums[i]==1:
                ones+=1
            if nums[i]==0:
                zeroes+=1
                
            if zeroes ==1:
                mxl = max(mxl,ones)
            elif zeroes ==0:
                mxl = max(mxl,ones-1)
            else:
                e = sw.pop(0)
                if e ==1:
                    ones-=1
                else:
                    zeroes-=1
        return mxl
            
                
        