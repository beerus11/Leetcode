# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def is_celeb(self,i,n):
        for j in range(n):
            if i!=j and knows(i,j) or not knows(j,i):
                return False
        return True
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(n):
            if knows(cand,i):
                cand = i
            
        if self.is_celeb(cand,n):
            return cand
        
        return -1
    

        