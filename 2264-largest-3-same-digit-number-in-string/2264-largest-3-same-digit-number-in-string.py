class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        pchar = ""
        count = 0
        for i in num:
            if i==pchar:
                count+=1
            else:
                count = 1
            pchar = i
            if count ==3:
                if ans==0:
                    ans = int(pchar)
                else:
                    ans = max(ans,int(pchar))
        if ans == -1:
            return ""
        return str(ans)*3
            