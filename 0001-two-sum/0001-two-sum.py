class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for k,i in enumerate(nums):
            if target-i in hm:
                return [hm[target-i],k]
            else:
                hm[i]=k
        return [0,0]
        