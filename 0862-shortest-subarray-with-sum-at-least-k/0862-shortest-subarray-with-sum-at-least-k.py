class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        arr = [0]
        for i in nums:
            arr.append(arr[-1]+i)
            
        ans = float('inf')
        q = deque()
        for key,v in enumerate(arr):
            while q and v<=arr[q[-1]]:
                q.pop()
                
            while q and v-arr[q[0]]>=k:
                ans = min(ans,key-q.popleft())
            q.append(key)
        
        if ans==float('inf'):
            return -1
        return ans