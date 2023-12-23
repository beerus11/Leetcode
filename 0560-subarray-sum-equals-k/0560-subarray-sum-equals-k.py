class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        hm = defaultdict(int)
        hm[0]=1
        for i in nums:
            curr_sum+=i
            if curr_sum -k in hm:
                count+=hm[curr_sum-k]
            hm[curr_sum]+=1
        return count
        
        