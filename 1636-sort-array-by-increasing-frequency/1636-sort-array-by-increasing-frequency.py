from collections import defaultdict
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        arr = sorted(d.items(),key= lambda x:(x[1],-1*x[0]))
        ans = []
        for a,b in arr:
            t = [a]*b
            ans.extend(t)
        return ans