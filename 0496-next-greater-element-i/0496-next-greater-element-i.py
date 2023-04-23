class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngl = [-1]
        st = [nums2[-1]]
        for i in range(len(nums2)-2,-1,-1):
            while len(st)>0 and nums2[i]>st[-1]:
                st.pop()
            if len(st)==0:
                ngl.append(-1)
            else:
                ngl.append(st[-1])
            st.append(nums2[i])
        ngl=ngl[::-1]
        
        m = {nums2[i]:ngl[i] for i in range(len(nums2))}
        ans = []
        for i in range(len(nums1)):
            ans.append(m[nums1[i]])
        return ans
                
            
            
        
        
        