class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            while ans and i<0 and ans[-1]>0 :
                if ans[-1]<-i:
                    ans.pop()
                    continue
                elif ans[-1]==-i:
                    ans.pop()
                break
            else:
                ans.append(i)
        return ans
        