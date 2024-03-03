from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        slist = SortedList()
        for num in reversed(nums):
            idx = slist.bisect_left(num) 
            result.append(idx)
            slist.add(num)
        return result[::-1]
        