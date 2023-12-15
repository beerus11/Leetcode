class Solution:
    def partitionString(self, s: str) -> int:
        st = set()
        count =0
        for i in s:
            if i in st:
                count+=1
                st = set()
            st.add(i)
        return count+1
        
        