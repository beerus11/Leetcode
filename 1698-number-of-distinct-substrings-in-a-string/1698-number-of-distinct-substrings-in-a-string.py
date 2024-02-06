class Solution:
    def countDistinct(self, s: str) -> int:
        st = set()
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                st.add(s[i:j])
        return len(st)
                
        