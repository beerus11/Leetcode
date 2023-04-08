import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in tasks:
            d[t]+=1
        
        heap = []
        for k,v in d.items():
            heapq.heappush(heap,(-1*v,k))
        max_time,task = heapq.heappop(heap)
        idle_time = ((-1*max_time)-1)*n
        
        while heap and idle_time>0:
            idle_time -= min((-1*max_time)-1,-1*heapq.heappop(heap)[0])
        idle_time = max(0,idle_time)
        
        return idle_time+len(tasks)
        
        
            
        