class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        no_till_now = ""
        for i in num:
            no_till_now+=i
            if int(i)%2!=0:
                ans = no_till_now         
        return ans
        