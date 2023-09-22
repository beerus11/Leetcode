class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0, len(numbers)-1
        while a<b:
            x = numbers[a]+numbers[b]
            if x==target:
                return [a+1,b+1]
            if x<target:
                a+=1
            else:
                b-=1
        return []
            