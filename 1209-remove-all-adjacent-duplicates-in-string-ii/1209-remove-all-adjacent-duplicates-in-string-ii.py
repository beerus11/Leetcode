class Solution:
    def removeDuplicates(self, s: str, ke: int) -> str:
        st = []
        for k in range(len(s)):
            v = s[k]
            if len(st)==0 or st[-1][0]!=v:
                st.append((v,1))
            else:
                n = st.pop()
                if n[1]<ke-1:
                    st.append((v,n[1]+1))      
        return "".join([k*v for k,v in st])
        