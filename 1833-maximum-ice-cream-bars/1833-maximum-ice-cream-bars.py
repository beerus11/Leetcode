class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in costs:
            if i>coins:
                break
            coins-=i
            ans+=1
        return ans
        