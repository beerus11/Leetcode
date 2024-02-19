class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        points = defaultdict(int)
        for num in nums:
            points[num]+=num
            
        arr = sorted(points.keys())
        two_back = 0
        one_back = points[arr[0]]
        
        for i in range(1,len(arr)):
            curr = arr[i]
            if curr-1 == arr[i-1]:
                two_back,one_back = one_back, max(one_back,two_back+points[curr])
            else:
                two_back,one_back = one_back,one_back+points[curr]
        return one_back