class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans =0 
        st = [-1]
        for i in range(len(s)):
            if s[i]== "(":
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    ans = max(ans,i-st[-1])
        
        
        return ans
        