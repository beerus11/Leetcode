class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tg,cg = 0,0
        ans = 0
        for i in range(len(gas)):
            tg += gas[i]-cost[i]
            cg += gas[i]-cost[i]
            if cg<0:
                cg=0
                ans = i+1
        return ans if tg>=0 else -1
        