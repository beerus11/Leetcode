class Solution:
    def find(self,arr,target):
        dct = defaultdict(int)
        dct[0] = 1
        s,c=0,0
        for i in range(len(arr)):
            s+=arr[i]
            if (s-target) in dct:
                c+=dct[s-target]
            dct[s]+=1
        return c
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n,m = len(matrix),len(matrix[0])
        ind,count = 0,0
        while ind <n:
            arr = [0]*m
            for i in range(ind,n):
                for j in range(m):
                    arr[j]+=matrix[i][j]
                count+=self.find(arr,target)      
            ind+=1
        return count