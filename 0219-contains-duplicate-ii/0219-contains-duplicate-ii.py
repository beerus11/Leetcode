class Solution:
    def containsNearbyDuplicate(self, nums: List[int], key: int) -> bool:
        hm = defaultdict(int)
        for k,v in enumerate(nums):
            if v in hm and k-hm[v]<=key:
                return True
            hm[v]=k