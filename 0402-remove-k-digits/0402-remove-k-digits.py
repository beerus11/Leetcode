class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in num:
            while k and st and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        ans = st[:-k] if k else st
        return "".join(ans).lstrip("0") or "0"