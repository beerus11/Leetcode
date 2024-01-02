class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = Counter(nums)
        f = copy.deepcopy(m)
        ans = []
        
        while len(f)>0:
            row = []
            for k,v in m.items():
                if k in f:
                    row.append(k)
                    f[k]-=1
                    if f[k]==0:
                        del f[k]
            ans.append(row)
        return ans
        