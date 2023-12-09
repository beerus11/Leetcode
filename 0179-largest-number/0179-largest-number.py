import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            return int(str(y)+str(x))-int(str(x)+str(y))
        arr = list(map(str,sorted(nums,key=functools.cmp_to_key(compare))))
        if arr[0]=="0":
            return '0'
        return ''.join(arr)
        