class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = Counter(s)
        for i in t:
            if i not in x:
                return i
            x[i]-=1
            if x[i]==0:
                del x[i]
        return ""
        