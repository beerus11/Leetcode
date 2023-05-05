class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[]
        def gen(path,left_count,right_count):
            if len(path)== 2*n:
                ans.append("".join(path))
                return
            if left_count<n:
                path.append("(")
                gen(path,left_count+1,right_count)
                path.pop()
            if right_count<left_count:
                path.append(")")
                gen(path,left_count,right_count+1)
                path.pop()
        gen([],0,0)
        return ans
        