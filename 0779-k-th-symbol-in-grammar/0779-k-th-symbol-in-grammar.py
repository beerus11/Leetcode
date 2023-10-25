class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        l = 1<<(n-2)
        if k <= l:
            return self.kthGrammar(n-1,k)
        return 1^self.kthGrammar(n-1,k-l)
        