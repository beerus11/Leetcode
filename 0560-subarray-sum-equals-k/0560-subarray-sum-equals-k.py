class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count,s = 0,0
        m = {0:1}
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in m:
                count+=m[s-k]
            m[s]=m.get(s,0)+1
        return count
            