class Solution:
    def minOperations(self, s: str) -> int:
        z,o = 0,0
        exp = "0"
        for i in s:
            if i!=exp:
                z+=1
            if exp=="0":
                exp="1"
            else:
                exp="0"
        exp="1"
        for i in s:
            if i!=exp:
                o+=1
            if exp=="0":
                exp="1"
            else:
                exp="0"
        return min(z,o)
                
        