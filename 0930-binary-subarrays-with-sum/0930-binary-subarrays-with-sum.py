class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        curr_sum = 0
        f = defaultdict(int)
        for n in nums:
            curr_sum+=n
            if curr_sum==goal:
                ans+=1
            if curr_sum-goal in f:
                ans += f[curr_sum-goal]
            f[curr_sum]+=1
        return ans
            
            