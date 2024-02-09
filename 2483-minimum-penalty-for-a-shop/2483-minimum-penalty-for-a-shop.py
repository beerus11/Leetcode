class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l = [0]
        r = [0]
        for c in customers:
            if c== "N":
                l.append(l[-1]+1)
            else:
                l.append(l[-1])
        for c in customers[::-1]:
            if c=="Y":
                r.append(r[-1]+1)
            else:
                r.append(r[-1])
        r= r[::-1]
        ans = []
        for k in range(len(customers)+1):
            ans.append(l[k]+r[k])
        mn = min(ans)
        return ans.index(mn)
                
            
                
            
                
        