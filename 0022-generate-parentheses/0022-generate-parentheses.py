class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isbalanced(arr):
            if arr[0]==")":
                return False
            st  = []
            for i in arr:
                if i==")":
                    if len(st)==0:
                        return False
                    elif st[-1]=="(":
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
                    
            return len(st)==0
            
        self.ans = []
        def generate(i,arr):
            if i == (2*n):
                if isbalanced(arr):
                    self.ans.append("".join(arr))
                return
            
            arr.append("(")
            generate(i+1,arr)
            arr.pop()
                
            arr.append(")")
            generate(i+1,arr)
            arr.pop()
            
        generate(0,[])
        return self.ans