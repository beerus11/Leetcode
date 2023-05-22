class Solution:
    def isPalindrome(self, s: int) -> bool:
        return str(s)==str(s)[::-1]
        