class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        a = 1
        while n>0:
            if n>=7:
                ans +=(7*(2*a+(6)))//2
            else:
                ans +=(n*(2*a+(n-1)))//2
            n-=7
            a+=1
        return ans
        