class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        ans = 0
        for right,value in enumerate(fruits):
            basket[value]+=1
            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            ans = max(ans,right-left+1)
        return ans
            
        