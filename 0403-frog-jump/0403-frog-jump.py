class Solution:
    def canCross(self, stones: List[int]) -> bool:
        hm = {}
        for i in range(len(stones)):
            hm[stones[i]]=set()
        hm[stones[0]].add(0)
        
        for i in range(len(stones)):
            for k in hm[stones[i]]:
                for s in [k-1,k,k+1]:
                    if s>0 and stones[i]+s in hm:
                        hm[stones[i]+s].add(s)
        #print(hm)
        return len(hm[stones[len(stones)-1]])>0
            
        