class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        isNeg = x<0
        x = abs(x)
        ans = []
        while x>0:
            ans.append(str(x%10))
            x = x//10
        x = int("".join(ans))
        if x>2**31:
            return 0
        if isNeg:
            return -1*x
        return int(x)
        