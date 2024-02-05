class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = list(range(n))
        heapq.heapify(rooms)
        hm = defaultdict(int)
        heap = []
        
        for a,b in meetings:
            while heap and heap[0][0]<=a:
                _,r = heapq.heappop(heap)
                heapq.heappush(rooms,r)
                
            if len(rooms)>0:
                room = heapq.heappop(rooms)
                heapq.heappush(heap,(b,room))
                hm[room]+=1
            else:
                end_time,room = heapq.heappop(heap)
                diff = end_time-a
                new_end = b+diff
                heapq.heappush(heap,(new_end,room))
                hm[room]+=1
        return sorted(hm.items(),key=lambda x:x[1],reverse=True)[0][0]
                
                
            
        