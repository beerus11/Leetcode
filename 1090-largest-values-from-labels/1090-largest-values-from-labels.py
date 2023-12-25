class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        mp = defaultdict(list)
        for i in range(len(values)):
            mp[values[i]].append(labels[i])
        limit_map = defaultdict(int)
        ans = 0
        values.sort(reverse=True)
        print(values)
        for i in range(len(values)):
            label = mp[values[i]].pop(0)
            print(label)
            if limit_map[label]< useLimit:
                numWanted-=1
                limit_map[label]+=1
                ans+=values[i]   
            if numWanted==0:
                break
        return ans
        
        