class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        count = [1]*(len(nums))
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if lis[j]+1>lis[i]:
                        lis[i] = lis[j]+1
                        count[i]=0
                    if lis[j]+1==lis[i]:
                        count[i]+=count[j]
        mx = max(lis)
        ans = 0
        for i in range(len(lis)):
            if lis[i]==mx:
                ans+=count[i]
        return ans
        