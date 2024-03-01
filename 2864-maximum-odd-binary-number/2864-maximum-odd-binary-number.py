class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count("1")
        return '1'*(ones-1)+'0'*(n-ones)+'1'
        