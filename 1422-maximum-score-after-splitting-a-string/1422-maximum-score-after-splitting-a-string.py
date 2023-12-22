class Solution:
    def maxScore(self, s: str) -> int:
        z,o = [],[]
        count = 0
        for i in s:
            if i=="0":
                count+=1
            z.append(count)
        count = 0
        for i in s[::-1]:
            if i=="1":
                count+=1
            o.append(count)
        o = o[::-1]
        mx = -1
        for i in range(1,len(s)):
            mx = max(mx,z[i-1]+o[i])
        return mx
            
        