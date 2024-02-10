class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i=0
        j=0
        print(g,s)
        while i<len(g) and j<len(s):
            while j<len(s) and s[j]<g[i]:
                j+=1
            if j==len(s):
                break
            if g[i]<=s[j]:
                ans+=1
            else:
                break
                
            i+=1
            j+=1
        return ans
        