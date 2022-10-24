class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        return self.dfs(arr,0,"")
        
    def dfs(self,arr,pos,res):
        if len(res) != len(set(res)):
            return 0
        best = len(res)
        for i in range(pos,len(arr)):
            best = max(best,self.dfs(arr,i+1,res+arr[i]))
        return best
            