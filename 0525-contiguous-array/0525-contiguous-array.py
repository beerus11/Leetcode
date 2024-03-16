class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        hm[0]=-1
        mxl = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if count in hm:
                mxl = max(mxl,i-hm[count])
            else:
                hm[count]=i
        return mxl
        