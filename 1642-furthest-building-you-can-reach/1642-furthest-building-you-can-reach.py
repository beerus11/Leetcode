class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            if heights[i+1]<=heights[i]:
                continue   
            d = heights[i+1]-heights[i]
            if bricks>=d:
                bricks-=d
                heappush(heap,-d)
            elif ladders>0:
                if len(heap)>0 and -1*heap[0]>d:
                    bricks+=-1*heappop(heap)
                    heappush(heap,-d)
                    bricks-=d
                ladders-=1
            else:
                return i
        
        return len(heights)-1
                