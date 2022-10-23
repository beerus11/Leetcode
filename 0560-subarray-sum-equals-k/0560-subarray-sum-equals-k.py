class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        s = 0
        count = 0
        m = {0:1}
        for i in range(l):
            s+=nums[i]
            if (s-k) in m:
                count+=m.get(s-k)
            m[s] = m.get(s,0)+1
        return count
            
        