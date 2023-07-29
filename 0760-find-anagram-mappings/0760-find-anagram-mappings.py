class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(list)
        for k,v in enumerate(nums2):
            m[v].append(k)
            
        ans = []
        for i in nums1:
            ans.append(m[i].pop())
        return ans
            
            
        