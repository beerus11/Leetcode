class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        st= {}
        ts= {}
        for i,j in list(zip(s,t)):
            if i not in st and j not in ts:
                st[i]=j
                ts[j]=i
            if st.get(i)!=j or ts.get(j)!=i:
                return False
        return True
                
        