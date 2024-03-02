class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        i,j=0,len(nums)-1
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                result.append(nums[i]**2)
                i+=1
            else:
                result.append(nums[j]**2)
                j-=1
        return result[::-1]
        