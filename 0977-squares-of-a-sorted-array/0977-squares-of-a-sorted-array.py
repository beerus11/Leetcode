class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            if nums[i]>=0:
                break
            i+=1
        if i>0 and abs(nums[i-1])<abs(nums[i]):
            i = i-1
        ans = []
        i,j=i,i+1
        print(i,j)
        while i>-1 or j<len(nums):
            if i==-1:
                ans.append(abs(nums[j])**2)
                j+=1
                continue
            if j== len(nums):
                ans.append(abs(nums[i])**2)
                i-=1
                continue
            
            x,y = abs(nums[i]**2),abs(nums[j]**2)
            if x<=y:
                ans.append(x)
                i-=1
            else:
                ans.append(y)
                j+=1
        return ans
            
                
            
        