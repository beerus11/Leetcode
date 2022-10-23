class Solution(object):
    def containsNearbyDuplicate(self, nums, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hm = {}
        for k,v in enumerate(nums):
            if v in hm and k-hm[v]<=t:
                return True
            else:
                hm[v]=k
        return False
        
        