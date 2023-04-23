#User function Template for python3

class Solution:
    def minimumNumber(self, n, arr):
        #code here
        for i in arr:
            if i%2==1:
                return 1
        return 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends