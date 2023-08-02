class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        ans = 0
        prev_d = float('-inf')
        for c, d in pairs:
            if c > prev_d:
                ans += 1
                prev_d = d
            elif d < prev_d:
                prev_d = d
        return ans
        