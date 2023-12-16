class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for ch in operations:
            if ch=="D" and len(st)>0:
                st.append(st[-1]*2)
            elif ch=="C" and len(st)>0:
                st.pop()
            elif ch=="+":
                st.append(st[-1]+st[-2])
            else:
                st.append(int(ch))
        if len(st)==0:
            return 0
        return sum(st)
                
        