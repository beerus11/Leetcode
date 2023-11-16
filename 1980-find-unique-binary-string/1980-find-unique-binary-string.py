class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        def gen(p,i):
            if len(p)==len(nums) and "".join(p) not in s:
                return "".join(p)
            if i == len(nums):
                return None
            p[i]="0"
            l = gen(p,i+1)
            if l:
                return l
            p[i]="1"
            return gen(p,i+1)
        return gen(["0"]*len(nums),0)
            
        