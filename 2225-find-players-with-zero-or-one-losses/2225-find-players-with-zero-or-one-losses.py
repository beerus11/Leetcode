class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lossers = defaultdict(int)
        
        for a,b in matches:
            winners.add(a)
            lossers[b]+=1
        arr = []  
        for k,v in lossers.items():
            if k in winners:
                winners.remove(k)
            if v==1:
                arr.append(k)
        return [sorted(list(winners)),sorted(arr)]
                
        