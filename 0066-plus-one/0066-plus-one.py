class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        def sd(digits,carry,i):
            if i==-1:
                if carry !=0:
                    ans.append(carry)
                return
            no = digits[i]+carry
            ans.append(no%10)
            sd(digits,no//10,i-1)    
        sd(digits,1,len(digits)-1)
        return ans[::-1]
        