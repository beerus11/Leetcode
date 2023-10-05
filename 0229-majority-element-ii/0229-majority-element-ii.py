class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        b = len(nums)/3
        m = defaultdict(int)
        ans = set()
        for i in nums:
            m[i]+=1
            if m[i]>b:
                ans.add(i)
        return ans
            