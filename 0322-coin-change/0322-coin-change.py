class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.dp ={}
        def cc(coins,amt,i):
            if i==len(coins):
                return -1
            if amt ==0:
                return 0
            if (i,amt) in self.dp:
                return self.dp[(i,amt)]
            if coins[i]>amt:
                self.dp[(i,amt)]= cc(coins,amt,i+1)
                return self.dp[(i,amt)]
            a = cc(coins,amt-coins[i],i)
            b = cc(coins,amt,i+1)
            if a==-1 and b==-1:
                self.dp[(i,amt)] =-1
            elif a==-1 or b==-1:
                self.dp[(i,amt)]= max(1+a,b)
            else:
                self.dp[(i,amt)] = min(1+a,b)
            return self.dp[(i,amt)]
        return cc(coins,amount,0)