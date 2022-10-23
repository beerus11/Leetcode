class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        if t=="":
            return False
        i,j= 0,0
        while i< len(t):
            if t[i]==s[j]:
                j+=1
            if j==len(s):
                return True
            i+=1
        return False
        