class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = bank[0].count("1")
        for i in range(1,len(bank)):
            cnt = bank[i].count("1")
            if cnt>0:
                ans += cnt*prev
                prev = cnt
        return ans
        