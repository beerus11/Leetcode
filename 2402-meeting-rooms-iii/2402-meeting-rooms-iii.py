import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        d = {i:0 for i in range(n)}
        rh = list(range(n))
        heap = []
        
        meetings.sort(key=lambda x:x[0])
        for a,b in meetings:
            while heap and heap[0][0]<=a:
                heapq.heappush(rh,heapq.heappop(heap)[1])
            if rh:
                room = heapq.heappop(rh)
                heapq.heappush(heap,(b,room))
            else:
                x,room = heapq.heappop(heap)
                heapq.heappush(heap,(b-a+x,room))
            d[room]+=1
        arr = sorted(d.items(),key= lambda x:(x[1],-1*x[0]),reverse=True)
        return arr[0][0]
            
        