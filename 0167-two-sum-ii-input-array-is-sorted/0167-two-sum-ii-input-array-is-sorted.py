class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i,j = 0, len(arr)-1
        while i<j:
            k = arr[i]+arr[j]
            if k==target:
                return [i+1,j+1]
            if k<target:
                i+=1
            else:
                j-=1
        return []