from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        arr = sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans = []
        for i in arr:
            ans.append(i[0]*i[1])
        return "".join(ans)
            
            
        