class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i!="*":
                st.append(i)
            elif len(st)>0:
                    st.pop()
        return "".join(st)
        