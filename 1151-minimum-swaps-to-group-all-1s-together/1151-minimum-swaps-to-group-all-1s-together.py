class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        ones_count,max_ones = 0,0
        q = []
        for i in range(len(data)):
            q.append(data[i])
            ones_count+=data[i]
            
            if len(q)>ones:
                ones_count-=q.pop(0)
            max_ones = max(max_ones,ones_count)
        return ones-max_ones
        