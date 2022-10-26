class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {0:0}
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in m:
                m[s%k] = i+1
            elif m[s%k]<i:
                return True
        return False
            
            