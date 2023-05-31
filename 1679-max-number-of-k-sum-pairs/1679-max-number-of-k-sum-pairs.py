class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hm = Counter(nums)
        for i in nums:
            if k-i in hm and hm[k-i]>0 and hm[i]>0:
                if k-i==i and hm[i]<2:
                    continue
                count+=1    
                hm[k-i]=hm[k-i]-1
                hm[i]=hm[i]-1
            if hm[k-i]==0 :
                del hm[k-i]
            if hm[i]==0:
                del hm[i]
        return count
        