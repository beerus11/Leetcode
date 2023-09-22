class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        count = 0
        for ch in stones:
            if ch in j:
                count+=1
        return count
        