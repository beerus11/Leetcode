class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        a,b = 0,0
        while a<len(g) and b<len(s):
            if s[b]>=g[a]:
                b+=1
                count+=1
            a+=1
        return count