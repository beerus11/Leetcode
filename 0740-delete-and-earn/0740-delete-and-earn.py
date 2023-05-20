class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_no = 0
        for n in nums:
            points[n]+=n
            max_no = max(max_no,n)
            
        
        @cache
        def max_points(num):
            if num ==0:
                return 0
            if num ==1:
                return points[1]
            return max(max_points(num-1),max_points(num-2)+points[num])
        return max_points(max_no)
        