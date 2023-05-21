class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = Counter(s)
        for i in t:
            if i not in m:
                return False
            if i in m:
                m[i]-=1
            if m[i]==0:
                del m[i]
        return len(m)==0
        