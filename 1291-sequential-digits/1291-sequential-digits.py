class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        string = "".join(list(map(str,list(range(0,10)))))
        lowd,highd = len(str(low)),len(str(high))
        for i in range(lowd,highd+1):
            for j in range(1,10):
                x = string[j:j+i]
                if int(x)>high or len(x)<i:
                    break
                if int(x)>=low and int(x)<=high:
                    ans.append(int(x))
        return ans
            
        