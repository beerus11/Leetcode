class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        CountText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            res = min(res,CountText[c]//balloon[c])
        return res
        