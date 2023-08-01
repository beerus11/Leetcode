class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1]*n
        count = [1]*n
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if length[j]+1>length[i]:
                        length[i] = length[j]+1
                        count[i] = 0
                    if length[j]+1== length[i]:
                        count[i]+=count[j]

        mxl = max(length)
        result = 0
        for i in range(n):
            if length[i]==mxl:
                result+=count[i]
        return result
        