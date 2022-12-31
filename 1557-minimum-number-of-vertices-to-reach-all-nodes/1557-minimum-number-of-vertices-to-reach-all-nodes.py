class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        g = collections.defaultdict(list)
        
        indegree = {i:0 for i in range(n)}
        for a,b in edges:
            indegree[b]+=1
        ans = []
        for k,v in indegree.items():
            if v == 0:
                ans.append(k)
        return ans
        