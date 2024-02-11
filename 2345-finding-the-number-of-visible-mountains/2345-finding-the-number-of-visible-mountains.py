class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        if len(peaks)==1:
            return 1
        arr = [(a-b,a+b) for a,b in peaks]
        arr.sort(key =lambda x:(x[0],-1*x[1]))
        st = [arr[0]]
        i = 1
        duplicate_count = 0
        while i <len(arr):
            duplicate = False
            while st and i<len(arr) and arr[i]==st[-1]:
                duplicate = True
                i+=1
            if duplicate and st:
                duplicate_count+=1
            if i==len(arr):
                break
            if len(st)==0 or arr[i][1]>st[-1][1]:
                st.append(arr[i])
            i+=1
        return len(st)-duplicate_count
            
        