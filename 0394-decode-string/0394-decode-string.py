class Solution:
    def decodeString(self, s: str) -> str:
        dst = []
        cst = []
        i = 0
        while i < len(s):
            ch = s[i]
            no = 0
            while s[i].isdigit():
                no=no*10+ int(s[i])
                i+=1
                print(no)
            if no>0:   
                dst.append(no)
                i-=1
            elif (ch>='a' and ch<='z') or ch =="[":
                cst.append(ch)
            elif ch=="]":
                arr = []
                while cst and cst[-1]!="[":
                    arr.append(cst.pop())
                if cst:
                    cst.pop()
                if dst:
                    cst.append("".join(arr[::-1])*dst.pop())
                else:
                    cst.append("".join(arr[::-1]))
            i+=1
        return "".join(cst)
            
        