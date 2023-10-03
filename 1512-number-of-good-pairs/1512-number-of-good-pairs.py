class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        for i in nums:
            if i in d:
                count+=d[i]
            d[i]+=1
        return count
                
        