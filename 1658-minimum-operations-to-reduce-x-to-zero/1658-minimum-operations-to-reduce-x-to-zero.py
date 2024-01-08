class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)
        n = len(nums)
        curr =0 
        l = 0
        mxi = -1
        for r in range(n):
            curr+=nums[r]
            while curr>total-x and l<=r:
                curr-=nums[l]
                l+=1
            if curr == total-x:
                mxi = max(mxi,r-l+1)
        return n-mxi if mxi!=-1 else -1
                
            
            
        