from collections import defaultdict
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(list(range(1,len(nums)+1)))
        rep=-1
        for i in nums:  
            if i in s:
                s.remove(i)
            else:
                rep = i
        return [rep,s.pop()]