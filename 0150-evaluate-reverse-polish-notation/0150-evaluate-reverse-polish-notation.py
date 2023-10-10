class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        s = set(['+','-','*','/'])
        for ch in tokens:
            if ch in s:
                b = st.pop()
                a = st.pop()
                if ch=="+":
                    st.append(a+b)
                elif ch=="-":
                    st.append(a-b)
                elif ch=="*":
                    st.append(a*b)
                elif ch=="/":
                    if a==0:
                        st.append(0)
                    else:
                        sign = (a*b)/abs(a*b)
                        x = abs(a)//abs(b)
                        st.append(int(sign*x))
            else:
                st.append(int(ch))
        return st.pop()