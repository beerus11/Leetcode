class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ps = 0
        if len(arr)<k:
            return 0
        q = []
        ans = 0
        for i in range(k):
            q.append(arr[i])
            ps+=arr[i]
        if ps/k>=threshold:
            ans+=1
        for j in range(i+1,len(arr)):
            ps-=q.pop(0)
            q.append(arr[j])
            ps+=arr[j]
            if ps/k>=threshold:
                ans+=1
        return ans
            
        