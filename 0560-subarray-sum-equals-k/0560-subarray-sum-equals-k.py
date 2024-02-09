class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        left = 0
        ans = 0
        hm = defaultdict(int)
        hm[0]=1
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in hm:
                ans+=hm[s-k]
            hm[s]+=1
        return ans
        