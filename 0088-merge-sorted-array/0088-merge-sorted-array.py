class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,c = 0,0,0
        nums,nums2 = nums1[:m],nums2[:n]
        while i<len(nums) or j<len(nums2):
            if i==len(nums):
                nums1[c]=nums2[j]
                j+=1
            elif j ==len(nums2):
                nums1[c]=nums[i]
                i+=1
            elif nums[i]<=nums2[j]:
                nums1[c]=nums[i]
                i+=1
            else:
                nums1[c]=nums2[j]
                j+=1
            c+=1
                
        