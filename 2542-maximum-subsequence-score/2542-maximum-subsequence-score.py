class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = [(a,b) for a,b in zip(nums1,nums2)]
        arr.sort(key = lambda x:x[-1],reverse=True)
        
        top_k_heap = [x[0] for x in arr[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        
        answer = top_k_sum*arr[k-1][1]
        
        for i in range(k,len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += arr[i][0]
            heapq.heappush(top_k_heap,arr[i][0])
            
            answer = max(answer,top_k_sum*arr[i][1])    
        
        return answer
        