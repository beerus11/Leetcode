class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['-', '+'] else s
        res = 0
        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)
            if res * sign >= 2**31 - 1:
                return 2**31 - 1
            if res * sign <= -2**31:
                return -2**31
        return res * sign
        