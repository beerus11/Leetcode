class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0
        for i in nums:
            if i==0:
                zeros+=1
            else:
                zeros=0
            ans+=zeros        
        return ans
        