class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l,r,c=defaultdict(int),defaultdict(int),defaultdict(int)
        for k,v in enumerate(nums):
            c[v]+=1
            if v not in l:
                l[v]=k
            r[v]=k
        degree = max(c.values())
        ans = len(nums)
        for i in nums:
            if c[i]==degree:
                ans = min(ans,r[i]-l[i]+1)
        return ans
        