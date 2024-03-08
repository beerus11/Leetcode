class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = Counter(nums)
        mx = max(hm.values())
        count = 0
        for k,v in hm.items():
            if v==mx:
                count+=v
        return count
        