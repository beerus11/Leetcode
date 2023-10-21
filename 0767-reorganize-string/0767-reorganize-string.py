import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)==1:
            return s
        if len(s)==2:
            return ""
        ans = []
        heap = [(-count,ch) for ch,count in Counter(s).items()]
        heapq.heapify(heap)
        
        while heap:
            cnf,chf = heapq.heappop(heap)
            if not ans or ans[-1]!=chf:
                ans.append(chf)
                if cnf+1!=0:
                    heapq.heappush(heap,(cnf+1,chf))
            else:
                if not heap: return ""
                cns,chs = heapq.heappop(heap)
                ans.append(chs)
                if cns+1!=0:
                    heapq.heappush(heap,(cns+1,chs))
                heapq.heappush(heap,(cnf,chf))
        
        
        return "".join(ans)
        
        