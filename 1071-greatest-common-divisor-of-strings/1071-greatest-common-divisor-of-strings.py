class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return "" if s1 + s2 != s2 + s1  else s1[:gcd(len(s1), len(s2))]