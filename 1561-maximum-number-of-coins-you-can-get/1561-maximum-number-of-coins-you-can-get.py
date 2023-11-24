class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        for i in range(0,2*(len(piles)//3),2):
            ans+=piles[i+1]
        return ans
        