class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        for n in nums:
            if len(arr)==0:
                arr.append(n)
            else:
                arr.append(arr[-1]+n)
        return arr