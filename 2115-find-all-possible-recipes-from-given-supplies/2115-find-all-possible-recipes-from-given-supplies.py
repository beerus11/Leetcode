class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        indegree = {}
        ss = set(supplies)
        rs = set(recipes)
        
        for r in recipes:
            indegree[r]=0
            
        for k,items in enumerate(ingredients):
            for item in items:
                indegree[item]=0
        
        g = defaultdict(list)
        for k,items in enumerate(ingredients):
            for item in items:
                g[item].append(recipes[k])
                indegree[recipes[k]]+=1
                
        q = [k for k,v in indegree.items() if v==0 and k in ss]
        # print(q)
        # print(indegree)
        # print(g)
        
        ans = []
        while q:
            node = q.pop(0)
            if node in rs:
                ans.append(node)
            for nei in g[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        #print(indegree)
        return ans
        