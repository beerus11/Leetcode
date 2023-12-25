class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            bin_str = bin(i)[2::]
            if s.find(bin_str)==-1:
                return False
        return True