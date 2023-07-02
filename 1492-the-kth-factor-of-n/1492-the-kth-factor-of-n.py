class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=1
        while k>0 and i<=n:
            if n%i ==0:
                k-=1
            if k==0:
                return i
            i+=1
        return -1
        
        