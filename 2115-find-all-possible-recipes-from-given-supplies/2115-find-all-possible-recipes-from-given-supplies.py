class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipes_set = set(recipes)
        g = defaultdict(list)
        
        indegree = defaultdict(int)
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                item = ingredients[i][j]
                g[item].append(recipes[i])
                indegree[recipes[i]]+=1
                
        q = deque(supplies)
        ans = set()
        
        while q:
            node = q.popleft()
            if node in recipes_set:
                ans.add(node)
            for nei in g[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans
                
        