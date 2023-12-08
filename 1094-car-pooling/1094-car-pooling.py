class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = defaultdict(int)
        drops = defaultdict(int)
        cab = 0
        
        for p,f,d in trips:
            pickups[f]+=p
            drops[d]+=p
            
        for i in range(10001):
            if i in pickups:
                cab+=pickups[i]
            if i in drops:
                cab-=drops[i]
            if cab>capacity:
                return False
        return True
        