class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)==1:
            return [0]
        ngl = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            if len(ngl)==0:
                ans.append(0)
            else:
                while len(ngl)>0 and ngl[-1][0]<=temperatures[i]:
                    ngl.pop()
                if len(ngl)==0:
                    ans.append(0)
                else:
                    ans.append(ngl[-1][1]-i)
            ngl.append((temperatures[i],i))
                
        return ans[::-1]
            
        