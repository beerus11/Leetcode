class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        cand1,cand2 = None,None
        count1,count2 =0,0

        for i in nums:
            if i==cand1:
                count1+=1
            elif i==cand2:
                count2+=1
            elif count1==0:
                cand1 = i
                count1+=1
            elif count2==0:
                cand2 = i
                count2+=1
            else:
                count1-=1
                count2-=1
        ans = []
        for i in [cand1,cand2]:
            if nums.count(i)> len(nums)//3:
                ans.append(i)
                
        return ans
            