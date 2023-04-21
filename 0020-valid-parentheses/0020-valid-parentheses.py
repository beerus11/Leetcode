class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {")":"(","}":"{","]":"["}
        for i in s:
            if i =="(" or i =="{" or i=="[":
                st.append(i)
            elif len(st)==0:
                return False
            else:
                a = st.pop()
                if m[i]!=a:
                    return False
        return len(st)==0
        