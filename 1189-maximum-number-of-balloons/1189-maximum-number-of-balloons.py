class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = Counter(text)
        c = Counter("balloon")

        ans = len(text)
        for k,v in c.items():
            ans = min(ans,m[k]//v)
        return ans
        