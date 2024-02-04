class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        count =0
        ans = 0
        for k,v in enumerate(nums):
            if v==0:
                count+=1
            while count==2:
                no = nums[left]
                if no==0:
                    count-=1
                left+=1
                
                
            ans = max(ans,k-left+1)
        return ans
                
            
        