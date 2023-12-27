class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        st = []
        mt  = 0
        for i in range(len(neededTime)):
            if len(st)==0 or st[-1][0]!=colors[i]:
                st.append((colors[i],neededTime[i]))
            else:
                c,t=st.pop()
                st.append((c,max(t,neededTime[i])))
                mt+=min(t,neededTime[i])
        return mt
            
        