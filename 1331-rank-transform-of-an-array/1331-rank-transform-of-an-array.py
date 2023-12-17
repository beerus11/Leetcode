class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}
        last_ch = ""
        rank = 1
        for k,v in enumerate(sorted(arr)):
            if k==0 or v==last_ch:
                rank_map[v]=rank
            else:
                rank+=1
            rank_map[v]=rank
            last_ch = v
        for i in range(len(arr)):
            arr[i]=rank_map[arr[i]]
        return arr
        