class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(no):
            ans = 0
            while no>0:
                ans = (ans*10) + no%10
                no = no//10
            return ans
        m = defaultdict(list)
        mod = 10**9 +7
        pairs = 0
        for k,v in enumerate(nums):
            x = nums[k]-rev(nums[k])
            if x in m:
                pairs+=len(m[x])%mod
                pairs%=mod
            m[x].append(k)
        return pairs
        