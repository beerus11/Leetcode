class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'ab', 'ba'
        if y > x: 
            x, y = y, x
            a, b = 'ba', 'ab'
        if y>x:
            x,y=y,x
        st1 = []
        ans = 0
        for i in s:
            if st1 and st1[-1]==a[0] and i==a[1]:
                st1.pop()
                ans+=x
            else:
                st1.append(i)
            
        st2 = []        
        for i in st1:
            if st2 and st2[-1]==b[0] and i==b[1]:
                st2.pop()
                ans+=y
            else:
                st2.append(i)
        return ans
                
        