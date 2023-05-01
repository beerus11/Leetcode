class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = list(range(n+1))
        i=1
        while i <len(ans):
            if i%15==0:
                ans[i]="FizzBuzz"
            elif i%3==0:
                ans[i]="Fizz"
            elif i%5==0:
                ans[i]="Buzz"
            else:
                ans[i]=str(i)
            i+=1
        return ans[1::]
        
        