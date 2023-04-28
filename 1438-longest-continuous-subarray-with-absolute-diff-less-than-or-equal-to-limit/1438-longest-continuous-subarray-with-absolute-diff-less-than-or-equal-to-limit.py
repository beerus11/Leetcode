class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mxQ,mnQ=[],[]
        mxL = 0
        
        i,j=0,0
        while j<len(nums):
            while len(mxQ)>0 and mxQ[-1]<nums[j]:
                mxQ.pop()
            mxQ.append(nums[j])
            
            while len(mnQ)>0 and mnQ[-1]>nums[j]:
                mnQ.pop()    
            mnQ.append(nums[j])
            
            while len(mxQ)>0 and len(mnQ)>0 and mxQ[0]-mnQ[0]>limit:
                if mxQ[0]==nums[i]:mxQ.pop(0)
                if mnQ[0]==nums[i]:mnQ.pop(0)
                i+=1
            
            mxL = max(mxL,j-i+1)
            j+=1
            
        return mxL
            
        