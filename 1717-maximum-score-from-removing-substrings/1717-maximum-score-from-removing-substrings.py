"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'ab', 'ba'
        if y > x: 
            x, y = y, x
            a, b = 'ba', 'ab'
        stack1 = []
        ans = 0
        for le in s:
            if stack1 and stack1[-1] == a[0] and le == a[1]: 
                stack1.pop()
                ans += x
            else: stack1.append(le)
        stack2 = []
        for le in stack1:
            if stack2 and stack2[-1] == b[0] and le == b[1]: 
                stack2.pop()
                ans += y
            else: stack2.append(le)
        return ans
"""
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
                
        