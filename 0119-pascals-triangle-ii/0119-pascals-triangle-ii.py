class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==0:
            return [1]
        if rowIndex ==1:
            return [1,1]
        arr = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            t = [1]
            for j in range(1,i):
                x = arr[i-1][j-1]+arr[i-1][j]
                t.append(x)
            t.append(1)
            arr.append(t)
        return arr[-1]
                
        