class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = 0
        st = []
        def get_last(st):
            return st.pop(),st.pop()
        for token in tokens:
            if token == "+":
                b,a = get_last(st)
                st.append(a+b)
            elif token == "-":
                b,a = get_last(st)
                st.append(a-b)
            elif token == "*":
                b,a = get_last(st)
                st.append(a*b)
            elif token == "/":
                b,a = get_last(st)
                st.append(int(a/b))
            else:
                st.append(int(token))
        return st[0]
        