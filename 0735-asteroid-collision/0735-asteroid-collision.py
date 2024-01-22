class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while len(st)>0 and st[-1]>0 and i<0:
                prev = st.pop()
                if prev==abs(i):
                    break
                elif prev>abs(i):
                    st.append(prev)
                    break  
            else:
                st.append(i)          
        return st
        