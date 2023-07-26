class Solution:
    def reverse(self, x: int) -> int:
        def rev(no):
            arr = []
            while no>0:
                arr.append(no%10)
                no=no//10
            no =0
            while len(arr)>0:
                no = no*10+arr.pop(0)   
            
            return no
        z = 2**31
        if x>=0:
            y = rev(x)
            return y if -1*z <y<z-1 else 0
        y = -1*rev(-1*x)
        return y if -1*z <y<z-1 else 0
        