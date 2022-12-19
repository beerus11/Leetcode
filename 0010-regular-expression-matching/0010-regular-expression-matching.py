class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.dp = {}
        def dfs(i,j):
            if (i,j) in self.dp:
                return self.dp[(i,j)]
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            
            match = i<len(s) and (s[i]==p[j] or p[j]==".")
            if j+1<len(p) and p[j+1]=="*":
                self.dp[(i,j)]= dfs(i,j+2) or (match and dfs(i+1,j))
                return self.dp[(i,j)]
            
            if match:
                self.dp[(i,j)] = dfs(i+1,j+1)
                return self.dp[(i,j)]
            self.dp[(i,j)]=False
            return self.dp[(i,j)]
        return dfs(0,0)
        