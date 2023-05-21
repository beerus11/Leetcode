class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s.lower():
            if i.isdigit() or (i>='a' and i<='z'):
                arr.append(i)
        return arr==arr[::-1]
        