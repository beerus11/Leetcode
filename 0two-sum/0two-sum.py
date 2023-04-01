class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for k,v in enumerate(nums):
            x = target -v
            if x not in m:
                m[v]=k
            else:
                return [m[x],k]
        return []
        