class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        rq = deque()
        dq = deque()
        
        for i,s in enumerate(senate):
            if s=="R":
                rq.append(i)
            else:
                dq.append(i)
                
        while rq and dq:
            rt = rq.popleft()
            dt = dq.popleft()
            
            if rt<dt:
                rq.append(rt+n)
            else:
                dq.append(dt+n)
        return "Radiant" if rq else "Dire"
        