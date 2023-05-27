class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = Counter(nums1)
        m2 = Counter(nums2)
        s = set()
        for k,v in m1.items():
            if k in m2:
                s.add(k)
        return list(s)
        
        
        