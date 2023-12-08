class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        ans = []
        while len(ans)<k:
            ans.append(heapq.heappop(heap)[1])
        return sorted(ans)