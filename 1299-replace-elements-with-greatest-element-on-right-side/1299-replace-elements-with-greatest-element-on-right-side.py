class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx = -1
        ans  = [-1]
        for i in range(len(arr)-1,0,-1):
            e = arr[i]
            if e>mx:
                mx = e
            ans.append(mx)
        return ans[::-1]
                