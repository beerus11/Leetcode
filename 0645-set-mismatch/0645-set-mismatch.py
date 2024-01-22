class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = []
        s1 = set()
        for i in nums:
            if i in s1:
                ans.append(i)
            s1.add(i)
        s2 = set(list(range(1,l+1)))
        ans.append(list(s2-s1)[0])
        return ans
        