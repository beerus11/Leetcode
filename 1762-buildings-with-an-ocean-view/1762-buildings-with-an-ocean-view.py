class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = []
        ans = []
        for i in range(len(heights)-1,-1,-1):
            if i==len(heights)-1:
                ans.append(i)
            else:
                while len(st)>0 and st[-1]<heights[i]:
                    st.pop()
                if len(st)==0:
                    ans.append(i)
            st.append(heights[i])
                
            
        return ans[::-1]
        