class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ls,rs = [],[]
        p = 0
        for i in nums:
            p+=i
            ls.append(p)
        p = 0
        for i in nums[::-1]:
            p+=i
            rs.append(p)
        rs = rs[::-1]
        print(ls,rs)
        ans = []
        for k,v in enumerate(nums):
            if k==0:
                r = rs[k+1]
                d = nums[k]*(len(nums)-1)
                ans.append(r-d)
            elif k== len(nums)-1:
                l = ls[k-1]
                d = nums[k]*(k)
                ans.append(d-l)
            else:
                l = ls[k-1]
                dl = nums[k]*(k)
                r = rs[k+1]
                dr = nums[k]*(len(nums)-k-1)
                ans.append(dl-l+r-dr)
        return ans
        