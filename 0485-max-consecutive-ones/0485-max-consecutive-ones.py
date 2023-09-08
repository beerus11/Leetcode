class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        co = 0
        ans = 0
        for i in nums:
            if i==1:
                co+=1
            else:
                co=0
            ans = max(ans,co)
        return ans
        