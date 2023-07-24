class Solution:
    def countAndSay(self, n: int) -> str:
        arr = ["1"]
        for i in range(1,n):
            e = arr.pop()
            t = []
            f = 0
            j =  0
            no = -1
            while j < len(e):
                if j>0 and e[j]!=e[j-1]:
                    t.append(str(f))
                    t.append(str(e[j-1]))
                    f=0
                f+=1
                j+=1
            t.append(str(f))
            t.append(e[-1])
            arr.append("".join(t))
        return arr[0]
            
        